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
