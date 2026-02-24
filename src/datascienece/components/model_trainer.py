import pandas as pd
import os
from src.datascienece import logger
from sklearn.linear_model import ElasticNet
from src.datascienece.entity.config_entity import ModelTrainerConfig
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    def train_model(self):
        try:
            logger.info("Reading training and testing data")
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            
            logger.info("Splitting data into features and target")
            X_train = train_data.drop(columns=[self.config.target_column], axis=1)
            y_train = train_data[self.config.target_column]
            
            X_test = test_data.drop(columns=[self.config.target_column])
            y_test = test_data[self.config.target_column]
            
            logger.info("Training the model")
            model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio,random_state=42)
            model.fit(X_train, y_train)
            
            logger.info("Saving the model")
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(model, model_path)
            
        except Exception as e:
            logger.exception(f"Error in training the model: {e}")