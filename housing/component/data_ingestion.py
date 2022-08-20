from housing.entity.config_entity import DataIngestionConfig 
from housing.exception import HousingException 
from housing.entity.artifact_entity import DataIngestionArtifact 
from housing.logger import logging 
import sys, os 
import tarfile 
from six.moves import urllib 
import pandas as pd 
import numpy as np 




class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started. {'='*20}")
            self.data_ingestion_config = data_ingestion_config 
        except Exception as e:
            raise HousingException(e, sys) from e  
        
    def download_housing_data(self):
        try:
            #extracting remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url 
            
            #folder location to download file 
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir 
            
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            
            os.makedirs(tgz_download_dir,exist_ok=True) 
            
            housing_file_name = os.path.basename(download_url) 
            
            tgz_file_path = os.path.join(tgz_download_dir, housing_file_name) 
            
            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            
            urllib.request.urlretrieve(download_url, tgz_file_path) 
            
            logging.info(f"File : [{tgz_file_path}] has been downloaded successfully.")
            
            return tgz_file_path 
            
        except Exception as e: 
            raise HousingException(e, sys) from e 
    
    def extract_tgz_file(self, tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir 
            
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)  
                
            os.makedirs(raw_data_dir,exist_ok=True) 
            
            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir) 
                
            logging.info(f"Extraction completed")
            
        except Exception as e: 
            raise HousingException(e, sys) from e 
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            file_name = os.listdir(raw_data_dir)[0] 
            
            housing_file_path = os.path.join(raw_data_dir,file_name) 
            
            housing_data_frame = pd.read_csv(housing_file_path) 
            
            housing_data_frame['income_cat'] = pd.cut(
                housing_data_frame['median_income'],
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                labels=[1,2,3,4,5]
            )
            
            strat_train_set = None 
            strat_test_set = None 
            
        except Exception as e: 
            raise HousingException(e, sys) from e 
    
    def initiate_data_ingestion(self)->DataIngestionArtifact: 
        try:
            tgz_file_path = self.download_housing_data() 
            
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
        except Exception as e:
            raise HousingException(e, sys) from e 
    