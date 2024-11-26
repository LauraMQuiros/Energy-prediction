import pandas as pd
import numpy as np

train = pd.read_csv("data/train.csv", index_col="ID")
test = pd.read_csv('data/test.csv', index_col="ID")

# get mean of target column in train
mean = train['target'].mean()

# len of test
len_test = len(test)

# create a list of mean values
mean_list = [mean] * len_test

# add gaussian noise to the mean values
noise = np.random.normal(0, 1, len_test)
mean_list = mean_list + noise

# create a dataframe with ID and target columns
df = pd.DataFrame({'ID': test.index, 'target': mean_list})
# save the dataframe to a csv file
df.to_csv('data/mean_w_noise.csv', index=False)