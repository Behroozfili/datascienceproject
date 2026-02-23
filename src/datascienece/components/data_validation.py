import os 
import pandas as pd
from src.datascienece import logger
from src.datascienece.entity.config_entity import ( DataValidationConfig)
from src.datascienece.config.configuration import (ConfigurationManager)



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validation_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir, header=None, names=self.config.all_schema.keys())
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            validation_status = True

            if len(all_cols) != len(all_schema):
                validation_status = False
            else:
                for col in all_cols:
                    if col not in all_schema:
                        validation_status = False
                        break

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation_status: {validation_status}")
            
            return validation_status

        except Exception as e:
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation_status: False")
            raise e