import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class datainjestionconfig:
    train_data_path:str=os.path.join("artifact","train.csv")
    test_data_path=os.path.join("artifact","test.csv")
    raw_data_path=os.path.join("artifact","data.csv")

class data_injestion:
    def __init__(self):
        self.injestion_config=datainjestionconfig()

    def initiate_data_injestion(self):
        logging.info("data injestion method has started")

        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.injestion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiated ")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)

            logging.info("data injestion completed")
            
            return(
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__=="__main__":
    obj=data_injestion()
    obj.initiate_data_injestion()





















































