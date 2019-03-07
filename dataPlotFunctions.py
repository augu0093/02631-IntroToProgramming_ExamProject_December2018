# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:29:41 2018

@author: Andreas Nilausen and August Semrau
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# This function creates bar chart over a chosen dataset. It sums the columns of
# different zones and converts in to kW. Lastly the data is plotted as four
# individual zones or all zones together depending on user choice.
# It takes as input a dataset of measurements and outputs a bar chart with
# the different zones.

def barChart(data, zone):
    
    # Data is grouped into individual zones
    # The total power usage (sum) for each zone is calculated. This is divided
    # by 1000 to get kW as output. 
    zone1 = (data[["zone1"]].sum()) / 1000
    zone2 = (data[["zone2"]].sum()) / 1000
    zone3 = (data[["zone3"]].sum()) / 1000
    zone4 = (data[["zone4"]].sum()) / 1000
    
    # The user chooses to view all zones seperate.
    if zone == 1:
        # Creating new dataframe to use in chart.
        plotZones = pd.concat([zone1, zone2, zone3, zone4])
        plotZones.set_axis(["Zone 1", "Zone 2", "Zone 3", "Zone 4"], axis = 0, inplace = True)
        
        # Setting plotting visuals.
        plotZones.plot(kind = "bar")
        plt.ylabel("kW/h Usage")
        plt.xlabel("Zones")
        plt.title("TOTAL POWER CONSUMPTION OF INDIVIDUAL ZONES")
        plt.style.use("_classic_test")
        
        
    # The user chooses to view alle zones together as one.
    elif zone == 2:
        
        # Creating new dataframe to use in chart.
        plotZones = pd.concat([zone1, zone2, zone3, zone4])
        zoneAll = plotZones.sum()
        zoneAll = pd.DataFrame([zoneAll])
            
        # Setting plotting visuals.
        zoneAll.plot(kind = "bar")
        plt.legend("")
        plt.ylabel("kW/h Usage")
        plt.xlabel("Combined zones")
        plt.title("TOTAL POWER CONSUMPTION OF ALL ZONES COMBINED")
        plt.style.use("_classic_test")
    
    # Showing output.
    plt.show()
    
    return


# This function creates a pie chart over a dataset. It calculates the sum of
# each zone and unites them in a new dataframe. Lastly the data is plotted.
# It takes in a set of data and outputs a pie chart of the individual zones. 
    
def pieChart(data):
    
    # Data is grouped into individual zones.
    # The total power usage (sum) of each zone is calculate and divided
    # by 1000 to get kW as output. 
    zone1 = (data[["zone1"]].sum())
    zone2 = (data[["zone2"]].sum())
    zone3 = (data[["zone3"]].sum())
    zone4 = (data[["zone4"]].sum())
        
    # Creating new dataframe to use in chart. 
    plotZones = pd.concat([zone1, zone2, zone3, zone4])
    
    # Setting plotting visuals.
    plotZones.plot(kind = "pie")
    plt.ylabel("")
    plt.title("TOTAL POWER CONSUMPTION OF EACH ZONE")
    plt.style.use("_classic_test")
    
    # Showing output.
    plt.show()
    
    return


# This function shows a bar chart of the power consumption of each hour of the day. 
# It sums over the columns to compute the sum of all zones per hour and resets
# indicies of the data to insert the time as label on the x-axis.
# It takes in data aggregated by hour of the day (period = 5) and outputs a bar chart consisting
# of power usage for each hour of the day. 
    
def hourOfDayBarChart(data_a):  
    
    # Finding the sum of each row in data_a (zone1, zone2, zone3 and zone4)
    # and dividing by 1000 to have kW as output.
    zonesSum = data_a.sum(axis = 1) / 1000
    
    # The indexes are reset to insert time of day as an xtick.
    zonesSum = zonesSum.reset_index(drop = True)
    
    # Numbers for xticks fitted to time of the day.
    xnumbers = np.linspace(4, 24, 6)
    
    # Setting plotting visuals.
    zonesSum.plot.bar(stacked = False, fontsize = 15)
    plt.title("POWER USAGE BY OUR OF DAY")
    plt.grid(True)
    plt.style.use("_classic_test")
    plt.xlabel("Time of day")
    plt.ylabel("kW/h usage")
    plt.xticks(xnumbers, ["04:00", "08:00", "12:00", "16:00", "20:00"], rotation = 0)
    plt.yticks()
    plt.xlim(-1,24)

    # Showing output.
    plt.show()
    
    return


# This function shows a bar chart of the power usage of each month. It sums over
# the columns in an aggregated set of data and divides this by 1000 to have kW as
# output. 
# It takes in data aggregated by month of the year and outputs are bar chart 
# of power usage of different months. 

def monthOfYearBarChart(tvec_a, data_a):
    # Finding the sum of each row in data_a (zone1, zone2, zone3 and zone4)
    # The sums are divided by 1000 to have kW as output. 
    zonesSum = data_a.sum(axis = 1) / 1000
    
    # The indicies are reset to insert months as an xtick.
    zonesSum = zonesSum.reset_index(drop = True)
    
    # Calling anonymous lambda-function returning the month and year of the time vector
    labels = pd.to_datetime(tvec_a).map(lambda d : str(d.year) + " " + str(d.month_name()))
    
    # Numbers for xticks fitted for different months.
    xnumbers = np.arange(len(labels))
    
    # Setting plotting visuals.
    zonesSum.plot.bar(fontsize = 15)
    plt.title("POWER USAGE BY MONTH OF YEAR")
    plt.grid(True)
    plt.style.use("_classic_test")
    plt.xlabel("Month")
    plt.ylabel("kWh usage")
    plt.xticks(xnumbers, labels)
    plt.yticks()
    plt.xlim(-1,12)
    
    # Showing output.
    plt.show()
    
    return   


# This function displays the power usage for each day of the year united in 12
# points. This is done individually for each zone. It converts the input data to kW
# and resets the indicies to use months as xticks. 
# It takes as input data aggregated by days of the year and outputs a plot with graphs
# for each zone. 

def individualDayOfYear(tvec_a, data_a):
    # Data is divided by 1000 to have output as kWh
    data_a = data_a / 1000
    
    # Indicies are reset for the xtick
    data_a = data_a.reset_index(drop = True)
    
    # Calling anonymous lambda-function returning the month and year of the time vector
    labels = pd.to_datetime(tvec_a).map(lambda d : str(d.year) + " " + str(d.day) + "/" + str(d.month))
    
    # Numbers for xticks fitted for the lenght of the dataset.
    xnumbers = np.arange(len(labels), step = 20)

    # Plotting visuals
    data_a.plot(stacked = False, fontsize = 15)
    plt.grid(True)
    plt.style.use("_classic_test")
    plt.xlabel("Date")
    plt.ylabel("kWh usage")
    plt.xticks(xnumbers, labels[::20], rotation = 90)
    plt.yticks()
    plt.xlim(0, len(labels))

    # Showing output. 
    plt.show()
    
    return
    

# This function creates a boxplot to accompany the statistical tables.
def boxPlot(data, outlier):
    
    # An outlier is a datapoint that is mathematically too far out to be 
    # included in the boxplot, and the user is able to not show these.
    if outlier == 1:
        data.boxplot(column = ["zone1", "zone2", "zone3", "zone4"], 
                       whiskerprops = {'linewidth' : 2},
                       medianprops = {'linewidth' : 2},
                       boxprops = {'linewidth' : 2},
                       fontsize = 15,
                       showfliers = False)
    elif outlier == 2:
        # Define look of outliers in case user wants to see these
        squares = dict(markerfacecolor = 'g', marker = 'D')
        data.boxplot(column = ["zone1", "zone2", "zone3", "zone4"], 
                       whiskerprops = {'linewidth' : 2},
                       medianprops = {'linewidth' : 2},
                       boxprops = {'linewidth' : 2},
                       fontsize = 15,
                       flierprops = squares)
    
    plt.title("Box Plot")
    plt.xlabel("Zones")
    plt.ylabel("Watt-hours")
    plt.style.use("_classic_test")
    plt.show()

    return