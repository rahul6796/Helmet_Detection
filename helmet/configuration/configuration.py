from helmet.constants import CONFIG_FILE_PATH
from helmet.utils.common import read_yaml, create_directory
from helmet.entity import DataIngestionConfig


class ConfigurationManager:

    def __init__(self,
                 config_path=CONFIG_FILE_PATH):
        self.config = read_yaml(config_path)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion


