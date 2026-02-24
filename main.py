from src.datascienece import logger
from src.datascienece.pipeline.data_ingestion_pipline import DataIngestionTrainigPipeline
from src.datascienece.pipeline.data_validation_pipline import DataValidationTrainigPipeline
from src.datascienece.pipeline.data_transformation_pipline import DataTransformationTrainigPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    data_validation = DataValidationTrainigPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    
    data_transformation = DataTransformationTrainigPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e
