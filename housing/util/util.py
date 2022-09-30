from array import array
import yaml 
from housing.exception import HousingException 
import os, sys 
import numpy as np

def read_yaml_file(file_path:str)->dict: 
    """
    Reads a YAML file and return the content as a dictionary. 
    file_path: str 
    """
    try:
        with open(file_path, "rb") as yaml_file: 
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise HousingException(e, sys) from e 
    
    
def save_numpy_array_data(file_path:str, array: np.array):
    """
    save numpy array data to file 
    file_path: str location of file to save
    array: np.array data to save
    
    _summary_

    Args:
        file_path (str): _description_
        array (np.array): _description_
    """
    try:
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True) 
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array) 
            
    except Exception as e:
        raise HousingException(e, sys) from e 
    
    
def load_numpy_array_data(file_path: str) -> np.array:
    
    """
    load numpy array data from file 
    file_path: str location of file to load 
    return: np.array data loaded 
    """
   
    try:
        with open(file_path, 'rb') as file_obj:
            
            return np.load(file_obj)
        
    except Exception as e:
        raise HousingException(e, sys) from e 