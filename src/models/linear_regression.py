import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def linear_regression(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame) -> pd.DataFrame:
    """
    Linear regression model
    :param X_train: training data
    :param y_train: training target
    :param X_test: test data
    :param y_test: test target
    :return: predictions
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def save_to_csv(data: pd.DataFrame, path: str):
    """
    Save data to csv
    """
    data.to_csv(path, index=False)

if __name__ == '__main__':
    train = pd.read_csv("data/train.csv", index_col="ID")
    test = pd.read_csv('data/test.csv', index_col="ID")
    X_train = train.drop(columns=["target", "measurement_time"])
    y_train = train["target"]
    test= test.drop(columns=["measurement_time"])
    y_pred = linear_regression(X_train, y_train, test)
    save_to_csv(y_pred, 'data/mse.csv')
