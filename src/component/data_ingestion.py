import os,sys
import pandas as pd 
import numpy as np
sys.path.append('F:\\WORK\\ml_project\\')
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    """Data Ingestion Config class"""
    # file path to the csv files
    train_filepath  = os.path.join('artifacts','train.csv')
    test_filepath  = os.path.join('artifacts','test.csv')
    raw_filepath  = os.path.join('artifacts','raw.csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    
    def inititate_data_ingestion(self):
        logging.info("DATA INGESTION STARTING....")
        try:
            logging.info("DATA READING USING PANDAS ")
            data = pd.read_csv(os.path.join("notebook\data","income_cleandata.csv"))
            
            logging.info("DATA READING COMPLETED")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_filepath),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_filepath,index=False)

            logging.info("DATA SPLITTED INTO TRAIN AND TEST")

            train_set,test_set = train_test_split(data,test_size=.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_filepath,index=False)
            test_set.to_csv(self.ingestion_config.test_filepath,index=False)

            logging.info("DATA INGESTION COMPLETED....")

            return(
                f'Training set has been saved in {self.ingestion_config.train_filepath}',
                f'Testing set has been saved in {self.ingestion_config.test_filepath}'
            
            ) 
        except Exception as e:
            logging.info("error occuredwhile ingestion stage")
            raise CustmeException(e,sys)


if __name__ =="__main__":
    obj = DataIngestion()
    obj.inititate_data_ingestion()





































































































