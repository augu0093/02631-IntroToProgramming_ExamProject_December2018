# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:50:20 2018

@author: August Andersen and Andreas Nilausen
"""
# Importing pandas module for dataframe-manipulation and numpy
import pandas as pd
import numpy as np


# This function takes the loaded sets of data, and returns a table with statistics.
# It uses the pandas-function 'describe' to create a table of data, from which
# the calculations for minimum and maximum values, as well as lower quartile, 
# median and upper quartile are used.

def printStatistics(tvec, data):
    
    # Using pandas 'describe' function for convenient statistics calculation
    # Statistics for individual zones
    statFrame1234 = data.describe()
    
    # Statistics for all four zones combined
    dataAll = pd.DataFrame(np.concatenate(np.array(data), axis = None))
    statFrameAll = dataAll.describe()
    
    # Combining the statistics-dataframes and removing unnecesaary rows
    statFrame = pd.concat([statFrame1234, statFrameAll], axis = 1, ignore_index = True)
    statFrame = statFrame.drop(statFrame.index[[0,1,2]])
    
    # Changing the labels for columns and rows from panda.describe standard
    statFrame.columns = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "All Zones"]
    statFrame.index = ["Min", "1. Quart.", "2. Quart.", "3. Quart.", "Max"]
    statFrame = statFrame.T

    print(statFrame)
    
    return