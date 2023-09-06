import os
import sys
import urllib.request as request
import zipfile
from helmet.logger import logger
from helmet.configuration.configuration import DataIngestionConfig

from helmet.exception import HelmetException


class DataIngestion:

    def __init__(self,
                 config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """

        :return:
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, header = request.urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )

                logger.info(f"{filename} downloaded! with following info: \n{header}")
            else:
                logger.info(f"file already exists of size !!")
        except Exception as ex:
            logger.error(f"failed to download data file from given source !")
            raise HelmetException(ex, sys) from ex

    def extract_zip_file(self):
        """

        :return:
        """
        try:
            unzip_file_path = self.config.unzip_dir
            os.makedirs(unzip_file_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, mode='r') as zip_file:
                zip_file.extractall(unzip_file_path)

        except Exception as ex:
            logger.error(f"failed to extract_zip_file :: {ex}")
            raise HelmetException(ex, sys) from ex
