from src.datascienece.config.configuration import ConfigurationManager
from src.datascienece.components.data_ingestion import DataIngestion
from src.datascienece import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainigPipeline:
  def __init__(self):
    pass
  
  def initiate_data_ingestion(self):
    logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.extract_zip_file()
  
if __name__ == "__main__":
  try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    object = DataIngestionTrainigPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
  except Exception as e:
    logger.exception(e)
    raise e

