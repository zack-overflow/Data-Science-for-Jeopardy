import pandas as pd
import numpy as np

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

def temp(data):
    '''
    Groups the player data set by contestant name, occupation, and location to combine 
    multiple instances of the same contestant.
    Args: 
        data (dictionary): keys are dataframe names, values are dataframes   
    Returns:
        none
    '''
    data['players']['combined name'] = data['players']['first'] + ' ' + data['players']['last']
    data['players'].groupby(['combined name', 'occupation','city', 'state']).size()

