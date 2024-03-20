from schemas.common_pb2 import IKVStoreConfig
import utils as ikvutils

class ClientOptions:
    _VALID_LOG_LEVELS = {"error", "warn", "info", "debug", "trace"}

    def __init__(self, ikv_config: IKVStoreConfig):
        self.ikv_config = ikv_config

class ClientOptionsBuilder:
    def __init__(self):
        # initialize ikvconfig proto object
        ikv_config = IKVStoreConfig()
        ikv_config.stringConfigs = {}
        ikv_config.intConfigs = {}
        ikv_config.floatConfigs = {}
        ikv_config.bytesConfigs = {}
        ikv_config.booleanConfigs = {}

        # default logging options
        ikv_config.stringConfigs["rust_client_log_level"] = "info"
        ikv_config.booleanConfigs["rust_client_log_to_console"] = True

        self.ikv_config: IKVStoreConfig = ikv_config
    
    def with_mount_directory(self, dir: str) -> 'ClientOptionsBuilder':
        self.ikv_config.stringConfigs["mount_directory"] = ikvutils.is_valid_str_or_raise(dir)
        return self

    def with_store_name(self, name: str) -> 'ClientOptionsBuilder':
        self.ikv_config.stringConfigs["store_name"] = ikvutils.is_valid_str_or_raise(name)
        return self

    def with_account_id(self, id: str) -> 'ClientOptionsBuilder':
        self.ikv_config.stringConfigs["account_id"] = ikvutils.is_valid_str_or_raise(id)
        return self

    def with_account_passkey(self, passkey: str) -> 'ClientOptionsBuilder':
        self.ikv_config.stringConfigs["account_passkey"] = ikvutils.is_valid_str_or_raise(passkey)
        return self

    def with_console_logging(self, level: str) -> 'ClientOptionsBuilder':
        level = ikvutils.is_valid_str_or_raise(level).lower()
        if not level in ClientOptions._VALID_LOG_LEVELS:
            raise ValueError("not a valid log level, valid levels: " + ", ".join(ClientOptions._VALID_LOG_LEVELS))

        self.ikv_config.stringConfigs["rust_client_log_level"] = level
        self.ikv_config.booleanConfigs["rust_client_log_to_console"] = True
        return self

    def with_file_logging(self, level: str, filepath: str) -> 'ClientOptionsBuilder':
        level = ikvutils.is_valid_str_or_raise(level).lower()
        if not level in ClientOptions._VALID_LOG_LEVELS:
            raise ValueError("not a valid log level, valid levels: " + ", ".join(ClientOptions._VALID_LOG_LEVELS))
        
        self.ikv_config.stringConfigs["rust_client_log_level"] = level
        self.ikv_config.booleanConfigs["rust_client_log_to_console"] = False
        self.ikv_config.stringConfigs["rust_client_log_file"] = ikvutils.is_valid_str_or_raise(filepath)
        return self

    def build(self) -> ClientOptions:
        return ClientOptions(self.ikv_config)