import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from src.datascienece import logger
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """Reads a yaml file and returns a Box object.

    Args:
        path (Path): Path to the yaml file.
        
    raises:
        value error if the yaml file is empty.
        e: empty yaml file: {path}
    Returns:
        configBox : ConfigBox type
    """
    
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError(f"Empty yaml file: {path}")
    except Exception as e:
        raise e
      
      
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True) :
    """Creates directories from a list of directories.

    Args:
        path_to_directories (list): List of directories to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
          logger.info(f"Directory created at: {path}")
          
@ensure_annotations
def save_json(path: Path, data: dict) :
    """Saves a dictionary as a json file.

    Args:
        path (Path): Path to the json file.
        data (dict): Data to be saved as json.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")  
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file

    Args:
        path (Path): Path to the json file.
    Returns:
        configBox : data as class attributes instead of dictionary keys.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)
  
@ensure_annotations
def save_bin(data: Any, path: Path) :
    """Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.   
    Returns:
        data (Any): Data loaded from the binary file. 
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data