import os
from src.datascienece import logger 
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascienece.entity.config_entity import (DataTransformationConfig)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_split(self):
        try:
            logger.info("Reading data from csv file")
            data = pd.read_csv(self.config.data_path, header=None, names=list(self.config.schema.COLUMNS.keys()))
            
            logger.info("Splitting data into train and test")
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            
            logger.info("Saving transformed data to csv file")
            logger.info(train_set.shape)
            logger.info(test_set.shape)
            
            print(train_set.shape)
            print(test_set.shape)
            
            train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
            
            logger.info(f"Transformed data saved successfully to {self.config.root_dir}")
            
        except Exception as e:
            logger.exception(f"Error occurred during data transformation: {e}")
            raise e