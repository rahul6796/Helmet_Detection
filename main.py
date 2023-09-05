from helmet.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from helmet.exception import HelmetException
from helmet.logger import logger
import sys


try:
    logger.info("Data-Ingestion-Started !")
    data_ingestion_pipe = DataIngestionPipeline()
    data_ingestion_pipe.main()

except Exception as ex:
    raise HelmetException(ex, sys) from ex
