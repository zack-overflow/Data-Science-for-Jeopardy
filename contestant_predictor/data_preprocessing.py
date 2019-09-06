import pandas as pd
import numpy as np
import read_data as rd

def duplicate_test(data):
    '''
    Tests if a single sample contestant (Ken Jennings) has more than one location 
    and/or more than one occupation recorded in the dataset.
    Args:
        data (dictionary): keys are dataframe names, values are dataframes
    Returns:
        none
    '''
    first_names = np.array(data['players']['first'])
    last_names = np.array(data['players']['last'])
    locations = np.array(data['players']['city'])
    occupations = np.array(data['players']['occupation'])
    counter = 0
    for first_name in first_names:
        if first_name == 'Ken' and last_names[counter] == 'Jennings':
            print(locations[counter] + " | " + occupations[counter])
        counter += 1

def init_grp(data):
    '''
    Groups the player data set (that's part of the main dataframe) by contestant name, 
    occupation, and location to combine multiple instances of the same contestant.
    Args: 
        data (dictionary): keys are dataframe names, values are dataframes of jeopardy data  
    Returns:
        Modified players dataframe
    '''
    data['players']['combined name'] = data['players']['first'] + ' ' + data['players']['last']
    data['players'] = data['players'].groupby(['combined name', 'occupation','city', 'state']).size()
    return data['players']

def preprocess(data):
    '''
    Function that preprocesses the data. [NEED TO ADD MORE DESCRIPTION]
    Args:
        data (dictionary): keys are dataframe names, values are dataframes of jeopardy data
    Returns:
        Preprocessed dataframe of training data for training.
    '''
    players = init_grp(data)
    return players