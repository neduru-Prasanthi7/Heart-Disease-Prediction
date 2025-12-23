"""
In this file we are going to load the data and other ML pipeline techniques which are needed
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import sys
import os
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from log_code import setup_logging
logger = setup_logging('main')
from var_outlier import variable_transformation_outliers
from feature_selection import complete_feature_selection
from imbalanced_data import balanced_data

class HEART_DISEASE_DATA:
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            logger.info('Data loaded successfully')
            logger.info(f'Total number of rows : {self.df.shape[0]}')
            logger.info(f'Total number of columns : {self.df.shape[1]}')
            logger.info(f'Check null values  : {self.df.isnull().sum()}')
            logger.info(f'{self.df.info()}')
            self.X = self.df.iloc[: ,:-1]
            self.y = self.df.iloc[: ,-1]
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size = 0.2,random_state = 42)
            logger.info(f'X_train columns :{self.X_train.columns}')
            logger.info(f'X_test columns : {self.X_test.columns}')



            logger.info(f'{self.y_train.sample(5)}')
            logger.info(f'{self.y_test.sample(5)}')

            logger.info(f'Total training data size : {self.X_train.shape}')
            logger.info(f'Total testing data size : {self.X_test.shape}')


        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in Line no : {error_line.tb_lineno}: due to {error_msg}')
    def var_outl(self):
        try:
            logger.info(f' Before training data :{self.X_train.columns}')
            logger.info(f'Before training data :{self.X_test.columns}')
            self.X_train,self.X_test = variable_transformation_outliers(self.X_train,self.X_test)
            logger.info(f'After training data  : {self.X_train.columns}-->{self.X_train.shape}')
            logger.info(f'After testing data  : {self.X_test.columns}-->{self.X_test.shape}')
        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in Line no : {error_line.tb_lineno}: due to {error_msg}')

    def fs(self):
        try:
            logger.info(f" Before : {self.X_train.columns} -> {self.X_train.shape}")
            logger.info(f"Before : {self.X_test.columns} -> {self.X_test.shape}")

            self.X_train,self.X_test = complete_feature_selection(self.X_train,self.X_test,self.y_train)

            logger.info(f" Before : {self.X_train.columns} -> {self.X_train.shape}")
            logger.info(f"Before : {self.X_test.columns} -> {self.X_test.shape}")
        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in Line no : {error_line.tb_lineno}: due to {error_msg}')

    def balanced_d(self):
        try:
            logger.info(f'Before number of rows for class 1:{sum(self.y_train == 1)}')
            logger.info(f'Before number of rows for class 0:{sum(self.y_train == 0)}')
            balanced_data(self.X_train,self.y_train,self.X_test,self.y_test)


        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in Line no : {error_line.tb_lineno}: due to {error_msg}')
if __name__ == '__main__':
    try:
        obj = HEART_DISEASE_DATA(f'C:\\Users\\nedur\\Downloads\\Heart_disease_prediction\\heart.csv')
        obj.var_outl()
        obj.fs()
        obj.balanced_d()
    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        logger.info(f'Error in Line no : {error_line.tb_lineno}: due to {error_msg}')
