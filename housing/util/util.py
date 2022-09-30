from array import array
import yaml 
from housing.exception import HousingException 
import os, sys 
import numpy as np
import pandas as pd 
from housing.constant import *

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
    
def save_object(file_path:str, obj): 
    """
    file_path: str
    obj: any sort of object
    
    _summary_

    Args:
        file_path (str): _description_
        obj (_type_): _description_
    """
    
    try:
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True) 
        with open(file_path, "wb") as file_obj:
            np.save(obj, file_obj)
            
    except Exception as e:
        raise HousingException(e, sys) from e 
    
    
def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
        try:
            
            dataset_schema = read_yaml_file(schema_file_path)
            
            schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY] 
            
            dataframe = pd.read_csv(file_path) 
            
            error_message = ""
            
            for column in dataframe.columns:
                if column in list(schema.keys()):
                    dataframe[column].astype(schema[column]) 
                else:
                    error_message = f"{error_message} \nColumn: [{column}] is not in the schema." 
            if len(error_message) > 0:
                raise Exception(error_message) 
            return dataframe
             
             
        except Exception as e:
            raise HousingException(e, sys) from e  
        