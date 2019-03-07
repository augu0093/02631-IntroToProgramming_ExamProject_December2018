# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:01:17 2018

@author: August Andersen and Andreas Nilausen
"""

# Numpy is used for menu-lists.
import numpy as np

# Descriptions of the different functions can be found in the function files. 
from menuFunction import displayMenu
from dataAggregation import aggregateMeasurements
from consumptionStatistics import printStatistics
from dataLoadFunction import loadMeasurements
from dataPlotFunctions import barChart
from dataPlotFunctions import pieChart
from dataPlotFunctions import hourOfDayBarChart
from dataPlotFunctions import monthOfYearBarChart
from dataPlotFunctions import individualDayOfYear
from dataPlotFunctions import boxPlot

# Defining menu items.
menuItems = np.array(["Load Data", "Aggregate Data", "Display Statistics", "Visualize Energy Consumption", "Quit"])

# Defining available data load menu items.
dataLoadItems = np.array(["Load data filling forward", "Load data filling backwards", "Load data dropping invalid datalines", "Go back"])

# Defining available data aggregation menu items.
aggregationItems = np.array(["Minutes", "Hours", "Days", "Months", "Aggregate data for hour of day", "Delete aggregated dataset", "Go back"])

# Defining available statistical calculations as menu items.
statisticsItems = np.array(["Statistics table", "Display Box Plot", "Statistical table for Aggregated dataset", "Display Box Plot for Aggregated dataset", "Go back"])

# Choice of outliers in boxplot.
outlierItems = np.array(["No", "Yes", "Go back"])

# Defining available plots as menu items.
vizualizationItems = np.array(["Bar Chart", "Pie Chart", "Bar Chart for day-aggregation dataset", "Bar Chart for month-aggregated dataset", "Bar Chart for hour of day-aggregated dataset", "Go back"])

# Choice of either all zones seperate or together.
zoneItems = np.array(["Four zones seperate", "Four zones together", "Go back"])

# Messages to be printed if the data is filtered are made.
aggregationMessages = np.array(["Minutes", "Hours", "Days", "Months", "Hour of the Day"])


# Number that defines whether or not a dataload has been succesfully completed.
dataLoadTick = 0

# Number that defines whether or not, as well as which data aggregation has taken place.
aggregationTick = 0


# The beginning of the user input menu.
while True:
    
    print("\nMain Menu:")
    
    # In case of data-aggregation, the program prints which aggregated dataset is active.
    if aggregationTick > 0:
        print("Note: Aggregated dataset is aggregated for {0}.".format(aggregationMessages[int(aggregationTick)-1]))
    
    # Displaying main menu options.
    choice = displayMenu(menuItems)
    
    # 1. main menu option: Load data.
    if choice == 1:
        while True:
            print("\nData loading")
            
            # Displaying data load menu options.
            loadChoice = displayMenu(dataLoadItems)
            
            # The user chooses option number 1, 2 or 3.
            if 1 <= loadChoice <= 3:
                try:
                    # Asking the user to input filename and saves it in variable.
                    filename = input("Please input the name of your datafile as 'filename.csv' or enter 'B' to go back: ")
                    
                    # If the user types in "B" the program breaks and returns to
                    # the previous option menu.
                    if filename == "B":
                        print("")
                        break
                    
                    else:
                        # The dataLoad function is called.
                        (tvec, data) = loadMeasurements(filename, loadChoice)
                        
                        # dataLoadTick is set to one and the other functions are
                        # now accessible.
                        dataLoadTick = 1 
                        
                        # If data is loaded for the second time without closing,
                        # the program makes sure aggregated data from earlier 
                        # dataset is not accesible.
                        if aggregationTick > 0:
                            aggregationTick = 0
                            
                        print("\nDataload is complete.")
                        
                        break 
            
                # If no file is found an error message is printed.
                except:
                    print("\nGiven filename couldn't be matched with excisting file. Please try again.")
            
            # If the user chooses to go back, the while loop breaks.
            elif loadChoice == 4:
                break
            
    # 2. main menu option: Aggregate data.
    elif choice == 2:
        while True:
            
            # If the dataLoadTick is zero it means that no data has yet been loaded.
            if dataLoadTick == 0:
                print("\nNo data can be aggregated, as no data has been loaded. Please load data first.\n")
                break
            
            # The program will now aggregate the data.
            else:
                print("\nAggregate data for different:")
                
                # Message in interface if data has already been aggregated. 
                if aggregationTick > 0:
                    print("Note: Aggregated dataset is currently aggregated for {0}.".format(aggregationMessages[int(aggregationTick)-1]))
                
                # Aggregation options are shown.
                aggChoice = displayMenu(aggregationItems)
                
                # If the user wants to aggregate for minutes, then aggregated 
                # dataset is the same as origional dataset.
                if aggChoice == 1:
                    tvec_a = tvec
                    data_a = data
                    aggregationTick = 1
                    break
                
                # Data is aggregated via dataAggregation function.
                elif 2 <= aggChoice <= 5:
                    (tvec_a, data_a) = aggregateMeasurements(tvec, data, aggChoice)
                    aggregationTick = aggChoice
                    break
                
                # The user can choose to delete current active aggregated dataset.
                elif aggChoice == 6:
                    del(tvec_a, data_a)
                    print("\nFormer aggregated dataset is now deleted.")
                    aggregationTick = 0
                
                elif aggChoice == 7:
                    break


    # 3. main menu option: Displaying statistics.
    elif choice == 3:
        while True:
            
            # If no data is loaded
            if dataLoadTick == 0:
                print("\nNo statistical tables can be displayed without data, please load data first.\n")
                break
            
            else:
                print("\nDisplay statistical table")
                
                # Message in interface if data has been aggregated.
                if aggregationTick > 0:
                    print("Note: Aggregated dataset is aggregated for {0}.".format(aggregationMessages[int(aggregationTick)-1]))
                    
                # Options are shown.
                statChoice = displayMenu(statisticsItems)
                
                # The table for origional dataset is shown via printStatistics function.
                if statChoice == 1:
                    print("")
                    printStatistics(tvec, data)
                    print("Measurements in above table are all Watt-Hour per Minute.")
                
                # Boxplot for non-aggregated dataset
                elif statChoice == 2:
                    while True:
                        print("Show Outliers in boxplot?")
                        outlierChoice = displayMenu(outlierItems)
                        
                        if outlierChoice == 1:
                            boxPlot(data, 1)
                            break
                        
                        elif outlierChoice == 2:
                            boxPlot(data, 2)
                            break
                        
                        elif outlierChoice == 3:
                            break
                
                # Table for aggregated dataset.
                elif statChoice == 3:
                    if aggregationTick == 0:
                        print("\nAn aggregated dataset is yet to be made, please do this first.")
                    else: 
                        print("")
                        printStatistics(tvec_a, data_a)
                        # Information regarding time-interval is printed.
                        print("Measurements in above table are all Watt-Hour per {0}.".format(aggregationMessages[int(aggregationTick)-1]))
                
                
                # Boxplot for aggregated dataset
                elif statChoice == 4:
                    if aggregationTick == 0:
                        print("\nAn aggregated dataset is yet to be made, please do this first.")
                        break
                    else:
                        while True:
                            print("Show Outliers in boxplot?")
                            outlierChoice = displayMenu(outlierItems)
                            
                            if outlierChoice == 1:
                                boxPlot(data_a, 1)
                                break
                            
                            elif outlierChoice == 2:
                                boxPlot(data_a, 2)
                                break
                            
                            elif outlierChoice == 3:
                                break
                
                elif statChoice == 5:
                    break


    # 4. main menu option: Visualizing energy consumption.
    elif choice == 4:
        while True:
            
            if dataLoadTick == 0:
                print("\nNo visualization can take place without data, please load data first.\n")
                break
            
            else:
                print("\nVizualize Energy Consumption")
                if aggregationTick > 0:
                    print("Note: Aggregated dataset is aggregated for {0}.".format(aggregationMessages[int(aggregationTick)-1]))
                
                plotChoice = displayMenu(vizualizationItems)
                
                # Bar Chart plot
                if plotChoice == 1:
                    print("Show bar chart for:")
                    zoneChoice = displayMenu(zoneItems)
                    if zoneChoice == 1:
                        barChart(data, 1)
                    elif zoneChoice == 2:
                        barChart(data, 2)
                    elif zoneChoice == 3:
                        continue
            
                # Pie Chart plot 
                elif plotChoice == 2:
                    pieChart(data)
                
                # Bar Chart for day-aggregation dataset
                elif plotChoice == 3:
                    if aggregationTick != 3:
                        (tvec_a, data_a) = aggregateMeasurements(tvec, data, 3)
                        print("\nNo 'Day' aggregated dataset was found. Dataset is now aggregated for this.")
                        aggregationTick = 3
                    individualDayOfYear(tvec_a, data_a)
                    
                # Bar Chart for month-aggregated dataset
                elif plotChoice == 4:
                    if aggregationTick != 4:
                        (tvec_a, data_a) = aggregateMeasurements(tvec, data, 4)
                        print("\nNo 'Month' aggregated dataset was found. Dataset is now aggregated for this.")
                        aggregationTick = 4
                    monthOfYearBarChart(tvec_a, data_a)
                
                # Bar Chart for hour of day-aggregated dataset
                elif plotChoice == 5:
                    if aggregationTick != 5:
                        (tvec_a, data_a) = aggregateMeasurements(tvec, data, 5)
                        print("\nNo 'Hour of the Day' aggregated dataset was found. Dataset is now aggregated for this.")
                        aggregationTick = 5
                    hourOfDayBarChart(data_a)
                
                elif plotChoice == 6:
                    break

    # 5. Quit
    elif choice == 5:
        # End with goodbye message
        print("Program has been closed. Thank you for using our program.")
        break