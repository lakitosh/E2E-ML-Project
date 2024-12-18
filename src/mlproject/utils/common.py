import os
from box.exceptions import BoxValueError
import yaml
from mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        print(f"Attempting to read YAML file from: {os.path.abspath(path_to_yaml)}")
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")
    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path) 
    logger.info(f"json file loaded from: {path}")
    

@ensure_annotations
def save_bin(data: any, path: Path):
    data = joblib.dump(value = data, filename = path) 
    logger.info(f"json file loaded from: {path}")
    

@ensure_annotations
def get_size(path: Path) -> Any:
    size_in_kb = round(os.path.getsize(path))
    return f"siize in KB: {size_in_kb}"
    
                