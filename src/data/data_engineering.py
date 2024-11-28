import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Feature_Engineering:

    def interpolate(train: pd.DataFrame, test: pd.DataFrame):
        # interpolate missing values
        pass
    def eliminate(train: pd.DataFrame, test: pd.DataFrame):
        # eliminate radiation_perpendicular
        pass

    def log_transform(self, train: pd.DataFrame, test: pd.DataFrame):
        # log transformation of target
        pass

    def label_season(self, train: pd.DataFrame, test: pd.DataFrame):
        # add week day and hour columns
        pass

    def add_lagged_features(self, train: pd.DataFrame, test: pd.DataFrame):
        # add lagged features
        pass



if __name__ == '__main__':
    train = pd.read_csv('../../data/train.csv', index_col="ID")
    test = pd.read_csv('../../data/test.csv', index_col="ID")