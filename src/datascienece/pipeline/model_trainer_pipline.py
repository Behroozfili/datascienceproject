from src.datascienece.config.configuration import ConfigurationManager
from src.datascienece.components.model_trainer import ModelTrainer
from src.datascienece import logger


STAGE_NAME = "model trainer Stage"

class ModelTrainerPipeline:
  def __init__(self):
    pass
  def initiate_model_trainer(self):
    try:
      with open("artifacts/data_validation/status.txt", "r") as f:
        status = f.read().split(" ")[-1]
      if status.strip() == "True":
          logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
          config = ConfigurationManager()
          model_trainer_config = config.get_model_trainer_config()
          model_trainer = ModelTrainer(config=model_trainer_config)
          model_trainer.train_model()
      else:
          raise Exception("Data Validation Failed. Model Training cannot proceed.")
    except Exception as e:
      logger.exception(f"Error occurred during model training: {e}")
      raise e
    