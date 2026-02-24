from src.datascienece.config.configuration import ConfigurationManager
from src.datascienece.components.data_evaluation import ModelEvaluation
from src.datascienece import logger
import os

STAGE_NAME = "Data Evaluation Stage"

class DataEvaluationTrainigPipeline:
  def __init__(self):
    pass
  
  def initiate_data_evaluation(self):
    
    os.environ["MLFLOW_TRACKING_URI"] = "your_mlflow_tracking_uri"
    os.environ["MLFLOW_TRACKING_USERNAME"] = "your_mlflow_username"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = "your_mlflow_password"
    logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
    config = ConfigurationManager()
    model_evaluation_config = config.get_mode_evaluation_config()
    model_evaluation = ModelEvaluation(config=model_evaluation_config)
    model_evaluation.log_into_mlflow()
    