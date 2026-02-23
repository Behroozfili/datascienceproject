from src.datascienece.config.configuration import ConfigurationManager
from src.datascienece.components.data_validation import DataValidation
from src.datascienece import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainigPipeline:
  def __init__(self):
    pass
  
  def initiate_data_validation(self):
    logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validation_all_columns()
  
if __name__ == "__main__":
  try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    object = DataValidationTrainigPipeline()
    object.initiate_data_validation()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
  except Exception as e:
    logger.exception(e)
    raise e

