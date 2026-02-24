from src.datascienece.config.configuration import ConfigurationManager
from src.datascienece.components.data_transformation import DataTransformation
from src.datascienece import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainigPipeline:
  def __init__(self):
    pass
  def initiate_data_transformation(self):
    
    try:
      with open(Path("artifacts/data_validation/status.txt"), "r") as f:
        status = f.read().split(" ")[-1]
      if status.strip() == "True":
          logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
          config = ConfigurationManager()
          data_transformation_config = config.get_data_transformation_config()
          data_transformation = DataTransformation(config=data_transformation_config)
          data_transformation.train_test_split()
      else:
          raise Exception("Data Validation Failed. Data Transformation cannot proceed.")
    except Exception as e:
      logger.exception(f"Error occurred during data transformation: {e}")
      raise e