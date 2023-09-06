from helmet.configuration.configuration import ConfigurationManager
from helmet.components.data_ingestion import DataIngestion
from helmet.logger import logger


class DataIngestionPipeline:

    def __inti__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

