import os 
import sys 
from dataclasses import dataclass
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("split the training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],# all rows, all columns except last
                train_array[:,-1],# all rows, only last column
                test_array[:,:-1],# all rows, all columns except last
                test_array[:,-1]# all rows, only last column
            )
            models={
                "Random Forest":RandomForestRegressor(),
                "Adaboost":AdaBoostRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Decision Tree":DecisionTreeRegressor(),    
                "KNN":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "Linear Regression":LinearRegression()            
            }
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            # to get best model score
            best_model_score=max(sorted(model_report.values()))

            #to get best model name
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No best model found")
            
            logging.info("Best training and testing model found")

            save_object(
       
                file_path= self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2=r2_score(y_test,predicted)
            return r2

        except Exception as e:
            raise CustomException(e,sys)
            