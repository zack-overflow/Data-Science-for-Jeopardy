import pandas as pd
import numpy as np
import sklearn.neural_network.multilayer_perceptron
import os
import data_preprocessing as dp

df_dict = dp.rd.read_data_to_dict()
train_df = dp.preprocess(df_dict)

y = train_df.pop('Score')
X = train_df