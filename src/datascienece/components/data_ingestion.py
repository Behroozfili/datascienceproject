import os 
import urllib.request as request
from src.datascienece import logger
import zipfile
from src.datascienece.entity.config_entity import (DataIngestionConfig)
from src.datascienece.config.configuration import (ConfigurationManager)


## component-Data ingestion 

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    # Downloading the data from source URL to local file
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
              url=self.config.source_URL, filename=self.config.local_data_file
              )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {os.path.getsize(self.config.local_data_file)} bytes")
    def extract_zip_file(self):
      
      """
      zip_file_path : str
      Extracts the zip file into the data directory
      function returns None 
      """
      unzip_dir = self.config.unzip_dir
      os.makedirs(unzip_dir, exist_ok=True)
      with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
          zip_ref.extractall(unzip_dir)
        