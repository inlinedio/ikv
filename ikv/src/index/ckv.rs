use crate::schema::{self, field::Field};

use super::ckv_segment::CKVIndexSegment;
use std::{
    collections::HashMap,
    fs::{self, OpenOptions},
    io::{self, BufReader, BufWriter, Error, Read, Write},
    sync::RwLock,
};

const NUM_SEGMENTS: usize = 16;

/// Memmap based columnar key-value index.
pub struct CKVIndex {
    // hash(key) -> PrimaryKeyIndex
    segments: Vec<RwLock<CKVIndexSegment>>,

    // field-name -> Field
    fieldname_field_table: HashMap<String, Field>,
}

impl CKVIndex {
    pub fn new(mount_directory: &str, schema_file_path: &str) -> io::Result<CKVIndex> {
        // ensure mount_directory exists
        fs::create_dir_all(mount_directory.clone())?;

        // copy and persist schema file
        let mount_schema_file_path = format!("{}/schema", mount_directory);
        fs::copy(schema_file_path, format!("{}/schema", mount_directory))?;

        let schema_string = schema::read_schema_file(&mount_schema_file_path)?;

        let mut segments = vec![];
        for index_id in 0..NUM_SEGMENTS {
            let segment = CKVIndexSegment::new(mount_directory, index_id)?;
            segments.push(RwLock::new(segment));
        }

        let mut fieldid_field_table = schema::load_yaml_schema(&schema_string);
        schema::sort_by_field_id(&mut fieldid_field_table);
        let fieldname_field_table = schema::to_map(&fieldid_field_table);

        Ok(Self {
            segments,
            fieldname_field_table,
        })
    }

    pub fn open(mount_directory: String) -> io::Result<CKVIndex> {
        // read persisted schema into String
        let schema_file_path = format!("{}/schema", mount_directory);
        let schema_string = schema::read_schema_file(&schema_file_path)?;

        let mut fieldid_field_table = schema::load_yaml_schema(&schema_string);
        schema::sort_by_field_id(&mut fieldid_field_table);
        let fieldname_field_table = schema::to_map(&fieldid_field_table);

        // open index segments
        let mut segments = Vec::with_capacity(NUM_SEGMENTS);
        for index_id in 0..NUM_SEGMENTS {
            let segment = CKVIndexSegment::open(&mount_directory, index_id)?;
            segments.push(RwLock::new(segment));
        }

        Ok(Self {
            segments,
            fieldname_field_table,
        })
    }

    pub fn close(&self) {
        for segment in self.segments.iter() {
            segment.read().unwrap().close();
        }
    }

    /// Fetch by field name
    pub fn get_field_value_by_name(&self, document_id: &[u8], field_name: &str) -> Option<Vec<u8>> {
        let field = self.fieldname_field_table.get(field_name)?;
        self.get_field_value(document_id, field)
    }

    /// Fetch and append by field name.
    /// Returns size of value iff non-empty, else 0.
    pub fn append_field_value_by_name(
        &self,
        document_id: &[u8],
        field_name: &str,
        dest: &mut Vec<u8>,
    ) -> usize {
        let maybe_field = self.fieldname_field_table.get(field_name);
        if maybe_field == None {
            return 0;
        }

        self.append_field_value(document_id, maybe_field.unwrap(), dest)
    }

    fn get_field_value(&self, document_id: &[u8], field: &Field) -> Option<Vec<u8>> {
        let mut dest = vec![];
        let value_len = self.append_field_value(document_id, field, &mut dest);
        if value_len == 0 {
            return None;
        }

        Some(dest)
    }

    // Fetch and append field value as bytes into the destination vector.
    // Return length (non-zero) as a result iff the field's value exists, or 0.
    fn append_field_value(&self, document_id: &[u8], field: &Field, dest: &mut Vec<u8>) -> usize {
        let index_id: usize = fxhash::hash(document_id) % NUM_SEGMENTS;
        let primary_key_index: std::sync::RwLockReadGuard<'_, CKVIndexSegment> =
            self.segments[index_id].read().unwrap();
        primary_key_index.read(&document_id, field, dest)
    }

    /// Write APIs
    /// 1. upsert multiple fields for a document
    /// 2. delete multiple fields for a document
    /// 3. delete a document
    /// Batch APIs ie above for multiple documents - todo

    pub fn upsert_field_values(
        &self,
        primary_key: &[u8],
        field_names: Vec<String>,
        field_values: Vec<Vec<u8>>,
    ) -> io::Result<()> {
        if primary_key.len() == 0 {
            return Ok(());
        }

        if primary_key.len() > u16::MAX as usize {
            return Err(Error::new(
                std::io::ErrorKind::Unsupported,
                "primary_key larger than 64KB is unsupported",
            ));
        }

        if field_names.len() != field_values.len() {
            return Err(Error::new(
                std::io::ErrorKind::InvalidData,
                "field name and value lengths mismatch",
            ));
        }

        // filter out unknown fields
        let mut final_fields = Vec::with_capacity(field_names.len());
        let mut final_field_values = Vec::with_capacity(field_values.len());
        for i in 0..field_names.len() {
            if let Some(field) = self.fieldname_field_table.get(&field_names[i]) {
                final_fields.push(field);
                final_field_values.push(field_values[i].as_slice());
            }
        }

        if final_fields.len() == 0 {
            return Ok(());
        }

        let index_id = fxhash::hash(primary_key) % NUM_SEGMENTS;
        let mut ckv_index_segment = self.segments[index_id].write().unwrap();
        ckv_index_segment.upsert_field_values(primary_key, final_fields, final_field_values)
    }

    pub fn delete_field_values(
        &self,
        primary_key: &[u8],
        field_names: Vec<String>,
    ) -> io::Result<()> {
        if primary_key.len() == 0 {
            return Ok(());
        }

        let mut final_fields = Vec::with_capacity(field_names.len());
        for i in 0..field_names.len() {
            if let Some(field) = self.fieldname_field_table.get(&field_names[i]) {
                final_fields.push(field);
            }
        }

        if final_fields.len() == 0 {
            return Ok(());
        }

        let index_id = fxhash::hash(primary_key) % NUM_SEGMENTS;
        let mut ckv_index_segment = self.segments[index_id].write().unwrap();
        ckv_index_segment.delete_field_values(primary_key, final_fields)
    }

    pub fn delete_document(&self, primary_key: &[u8]) -> io::Result<()> {
        if primary_key.len() == 0 {
            return Ok(());
        }

        let index_id = fxhash::hash(primary_key) % NUM_SEGMENTS;
        let mut ckv_index_segment = self.segments[index_id].write().unwrap();
        ckv_index_segment.delete_document(primary_key)
    }
}

#[cfg(test)]
mod tests {
    use super::CKVIndex;

    #[test]
    fn open() {
        let yaml_str = "
        document:
        - name: firstname
          id: 0
          type: string
        - name: age
          id: 1
          type: i32
        - name: profile
          id: 2
          type: bytes";
        let index = CKVIndex::new("/tmp/basic", yaml_str);
        assert!(index.is_ok());
    }
}
