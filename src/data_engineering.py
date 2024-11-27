import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_engineering(train: pd.DataFrame, test: pd.DataFrame):
    # interpolate missing values
    # eliminate radiation_perpendicular
    # log transformation of target
    pass



if __name__ == '__main__':
    train = pd.read_csv('../data/train.csv', index_col="ID")
    test = pd.read_csv('../data/test.csv', index_col="ID")