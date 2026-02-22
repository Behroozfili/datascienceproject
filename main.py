from src.datascienece import logger
from src.datascienece.pipeline.data_ingestion_pipline import DataIngestionTrainigPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e