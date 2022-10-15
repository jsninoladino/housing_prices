# %%
# Import necessary libraries for data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os

# %%
# Create reference to directories
source_dir = os.getcwd()
main_dir = os.path.abspath(os.path.join(source_dir, ".."))
data_dir = os.path.abspath(os.path.join(main_dir, "data"))

# Create references to filepaths
train_path = os.path.abspath(os.path.join(data_dir, "train.csv"))
test_path = os.path.abspath(os.path.join(data_dir, "test.csv"))

# %%
# Import dataset into pandas dataframe
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# %%
# Display train
train_df.head()


