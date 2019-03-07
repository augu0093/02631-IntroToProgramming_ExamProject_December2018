# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:26:17 2018

@author: August Andersen
"""
# Importing pandas module for dataframe-manipulation
import pandas as pd


# This function takes two pandas dataframes, 'tvec' and 'data', as inputs, and
# sums the measurements of the four different zones according to the specified
# time interval. This means, if the user chooses ex. "month" as the period 
# input, all measurements made in the same month are summed in the 'data' dataframe
# and all time-rows in 'tvec' that are in the same month are put into one row.

def aggregateMeasurements(tvec, data, period):
    
    # Put data back together to keep dates and data linked correctly
    fullDataFrame = pd.concat([tvec, data], axis = 1, ignore_index = True)
    
    #Midlertidig
    fullDataFrame.columns = ["year", "month", "day", "hour", "minute", "second", "zone1", "zone2", "zone3", "zone4"]
    
    
    # All measurements for different hour-intervals
    if period == 2:
        # Sum zone-data in dataframe with identical months, days and hours
        hourFrame = fullDataFrame.groupby(["year", "month", "day", "hour"]).agg({"year":"min", "month":"min", "day":"min", "hour":"min", "minute":"min", "second":"min", "zone1":"sum", "zone2":"sum", "zone3":"sum", "zone4":"sum"})
        
        # From the full aggregated dataframe we extract time-data and zone-data
        tvec_a = hourFrame.drop(columns = ["zone1", "zone2", "zone3", "zone4"])
        data_a = hourFrame.drop(columns = ["year", "month", "day", "hour", "minute", "second"])
    
    
    # All measurements for different day-intervals    
    elif period == 3:
        # Sum zone-data in dataframe with identical months and days
        dayFrame = fullDataFrame.groupby(["year", "month", "day"]).agg({"year":"min", "month":"min", "day":"min", "hour":"min", "minute":"min", "second":"min", "zone1":"sum", "zone2":"sum", "zone3":"sum", "zone4":"sum"})     
        
        # From the full aggregated dataframe we extract time-data and zone-data
        tvec_a = dayFrame.drop(columns = ["zone1", "zone2", "zone3", "zone4"])
        data_a = dayFrame.drop(columns = ["year", "month", "day", "hour", "minute", "second"])
    
    
    # All measurements for different month-intervals
    elif period == 4:
        # Sum zone-data in dataframe with identical months
        monthFrame = fullDataFrame.groupby(["year", "month"]).agg({"year":"min", "month":"min", "day":"min", "hour":"min", "minute":"min", "second":"min", "zone1":"sum", "zone2":"sum", "zone3":"sum", "zone4":"sum"})
    
    # From the full aggregated dataframe we extract time-data and zone-data
        tvec_a = monthFrame.drop(columns = ["zone1", "zone2", "zone3", "zone4"])
        data_a = monthFrame.drop(columns = ["year", "month", "day", "hour", "minute", "second"])
    
    
    # All measurements in 24h hour-intervals
    elif period == 5:
        
        # Divide all measurements into intervals of one hour in 24h span. 
        # Finde mean value of these intervals
        hourOfDayFrame = fullDataFrame.groupby(["hour"]).agg({"year":"min", "month":"min", "day":"min", "hour":"min", "minute":"min", "second":"min", "zone1":"sum", "zone2":"sum", "zone3":"sum", "zone4":"sum"})
        
        # From the full aggregated dataframe we extract the 24 hour-stamps and their data
        tvec_a = hourOfDayFrame.drop(columns = ["year", "month", "day", "minute", "second", "zone1", "zone2", "zone3", "zone4"])
        data_a = hourOfDayFrame.drop(columns = ["year", "month", "day", "hour", "minute", "second"])
    
    #return hourFrame
    return (tvec_a, data_a)