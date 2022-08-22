from housing.pipeline.pipeline import Pipeline 
from housing.exception import HousingException 
from housing.logger import logging
from housing.config.configuration import Configuration
import sys 

def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline() 
        data_validation_config = Configuration().get_data_validation_config()
        print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        #raise HousingException(e, sys) from e 
        
        
    
if __name__ == '__main__':
    main()  