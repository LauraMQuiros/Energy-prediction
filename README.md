# Energy prediction forecasting

To run the code from root
```bash
    conda create --name energy-forecasting python=3.9
    conda activate energy-forecasting
    pip install -r requirements.txt
```
For running the jupyter notebook
```bash 
    conda install ipykernel
    python -m ipykernel install --user --name=energy-forecasting
    conda install jupyter
```

## Data Analysis
- The data is hourly and spans 10 months from november 2023 to august 2024
- The data is split into 2 datasets: train and test from which only train has the target variable
- The data has 1 non-numerical feature `measurement_time` which is a datetime object
- The data has 6 temperature features, 5 solar radiation features, 2 wind features and a clouds feature

## Data Preprocessing & Feature Engineering
- We separate the `measurement_time` into month, day of the week and hour of the day, which improves the RMSE score of the basic linear regression model
- We realise that shuffling the data before splitting it into train and validation sets improves the RMSE of the basic linear regression model with PCA from $11$ to $8.1$
- Without PCA nor scaling, with minmax scaling and with standard scaling, RSME yields a value of $11.31$ while making the log of the input features gives $10.61$
- Combining minmax scaling and log of the input features gives the best RMSE of $9.86$
- Not using the year improves the RMSE from $9.86$ to $9.71$
- Using one-hot encoded seasons instead of month improves the RMSE from $9.71$ to $9.54$
- Using one-hot encoded time_of_day instead of hour improves the RMSE from $9.54$ to $8.89$
- Using lagged features improves to $8.68$

## Model Selection

## Model Evaluation


# Research 

There are plenty of energy forecasting competitions in Kaggle. I found the following
- [ASHRAE - Great Energy Predictor III](https://www.kaggle.com/c/ashrae-energy-prediction)

Their winning solution used an ensemble of 3 models (LightGBM, LMP, and CatBoost) and a feature engineering pipeline. 
This consisted of 
- Time series features including holiday flags and time of day features
- Count (frequency) features
- Lag temperature features
- Smoothed and 1st, 2nd-order differentiation temperature features using Savitzky-Golay filter
- [Bayesian target encoding](https://www.kaggle.com/code/mmotoki/hierarchical-bayesian-target-encoding)
- Cyclic encoding of periodic features; e.g., hour gets mapped to `hour_x = cos(2*pi*hour/24)` and `hour_y = sin(2*pi*hour/24)`

Other notable solutions included Neural networks with embeddings for categorical features and several optimisers
