from helmet.constants import CONFIG_FILE_PATH
from helmet.utils.common import read_yaml, create_directory
from helmet.entity import DataIngestionConfig, DataTransformationConfig


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

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transform
        create_directory([config.root_dir])

        data_transform_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_transform_train_dir=config.data_transform_train_dir,
            data_transform_test_dir=config.data_transform_test_dir,
            data_transform_train_file_name=config.data_transform_train_file_name,
            data_transform_test_file_name=config.data_transform_test_file_name,
            data_transform_train_split = config.data_transform_train_split,
            data_transform_test_split =config.data_transform_test_split
        )
        return data_transform_config


