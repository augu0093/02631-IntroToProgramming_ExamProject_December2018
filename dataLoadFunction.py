# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:10:06 2018

@author: Andreas Nilausen
"""
import numpy as np
import pandas as pd


# This function loads a CSV file consisting of dates and measurements into a dataframe
# and removes invalid data (values of -1). Depending of the chosen fmode the data is handled
# differently. The function uses the Pandas module to handle the data effectively. 
# It takes as input a CSV file and a integer describing the desired choice of data filling. 
# It outputs dataframe with measurement times and a dataframe with corrected data. 

def loadMeasurements(filename, fmode):
    
    # The data is loaded. The dtypes are changed to floats to easier filter the data
    data = pd.read_csv(filename, names = ["year", "month", "day", "hour", "minute", "second", "zone1", "zone2", "zone3", "zone4"], dtype={"year":float, "month":float, "day":float, "hour":float, "minute":float, "second":float})
    
    # All false measurements, with the value -1, are replaced with NaN-values. 
    dataNaN = data.replace(float(-1), np.nan)
    
    # If fmode is set to one (1) but there is an error in the first row the false
    # data is dropped.
    if fmode == 1 and dataNaN.iloc[0,:].isna().any():
        dataFiltered = dataNaN.dropna()
        print("An error has been detected in the first row of the selected dataset.\
              Therefore the forward fill could not be done succesfully.\nAll rows with\
              invalid measurements has been filtered from the data.")
    
    # If fmode is set to one (1), the row is replaced with the last row without measuring
    # errors using the ffill()-function.
    elif fmode == 1:
        dataFiltered = dataNaN.ffill(inplace = False)
        
        # If fmode is set to two (2) but there is an error in the last row the false
        # data is dropped.
    elif fmode == 2 and dataNaN.iloc[len(dataNaN.index)-1,:].isna().any():
        dataFiltered = dataNaN.dropna()
        print("An error has been detected in the first row of the selected dataset.\
              Therefore the forward fill could not be done succesfully.\nAll rows with\
              invalid measurements has been filtered from the data.")
    
    # If fmode is set to two (2), the row is replaced with the next row without measuring
    # errors using the bfill()-function.
    elif fmode == 2:
        dataFiltered = dataNaN.bfill(inplace = False)
        
    # If fmode is set to three (3), the data false data is dropped. 
    elif fmode == 3:
        # The comment below assures that data that exceeds natural limits such as a day with
        # 25 hours also are recognized as invalid data. Though we assume that invalid data are of
        # value negative 1 (-1).
        
        # dataFiltered = data[(data.year > 0) & (data.month > 0) & (data.month <= 12) & (data.day > 0) & (data.day <= 31) & (data.hour >= 0) & (data.hour <= 24) & (data.minute >= 0) & (data.minute <= 60) & (data.second >= 0) & (data.second <= 60) & (data.zone1 >= 0) & (data.zone2 >= 0) & (data.zone3 >= 0) & (data.zone4 >= 0)]
        
        dataFiltered = dataNaN.dropna()
        
        # The data is now filtered and is defined as two variables; tvec and data. 
        # The .copy() is used for further editing of the dataframes. 
    tvec = dataFiltered[["year", "month", "day", "hour", "minute", "second"]].copy()
    data = dataFiltered[["zone1", "zone2", "zone3", "zone4"]].copy()
    
    return (tvec, data)
        
    