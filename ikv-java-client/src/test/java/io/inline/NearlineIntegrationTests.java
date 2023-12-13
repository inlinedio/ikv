package io.inline;

import com.inlineio.schemas.Common;
import io.inline.clients.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class NearlineIntegrationTests {
    private final static FieldAccessor USERID_ACCESSOR =
            new FieldAccessor("userid", Common.FieldType.STRING);

    private final ClientOptions _clientOptions = new ClientOptions.Builder()
            .withMountDirectory("/tmp/NearlineIntegrationTests")
            .withPrimaryKeyFieldName("userid")
            .withStoreName("testing-store")
            .withKafkaConsumerBootstrapServer("localhost:9092")
            .withKafkaConsumerTopic("testing-topic")
            .withKafkaConsumerPartition(0)
            .build();

    private final GRPCInlineKVWriter _writer = new GRPCInlineKVWriter();
    private final InlineKVReader _reader = new DefaultInlineKVReader();

    @Test
    public void upsertAndRead() throws InterruptedException {
        _writer.startup();
        _reader.startup(_clientOptions);

        IKVDocument document = new IKVDocument.Builder()
                .putStringField("userid", "firstuserid")
                .build();
        _writer.upsertFieldValues(document);

        Thread.sleep(1000 * 10);  // 5 sec sleep

        // Read

        String value = _reader.getStringValue(PrimaryKey.from("firstuserid"), USERID_ACCESSOR);
        Assertions.assertEquals(value, "firstuserid");
    }
}
