import pandas as pd
import numpy as np

def read_data_to_dict():
    data_dict = {}
    data_dict['board'] = pd.read_csv('data_files/board.csv')
    data_dict['doubles'] = pd.read_csv('data_files/doubles.csv')
    data_dict['order'] = pd.read_csv('data_files/order.csv')
    data_dict['players'] = pd.read_csv('data_files/players.csv')
    data_dict['scores'] = pd.read_csv('data_files/scores.csv')
    data_dict['summary'] = pd.read_csv('data_files/summary.csv')
    return data_dict
