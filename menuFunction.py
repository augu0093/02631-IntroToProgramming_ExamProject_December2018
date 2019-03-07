# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:30:43 2018

@author: August Andersen and Andreas Nilausen
"""
import numpy as np


# This function uses a while-loop to define a variable using a user input. If the 
# desired input is not met, an error message is printed and the program asks the user 
# to try again. It takes in a user input and returns a variable based on the input. 

def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print ("Menu item has to be selected as one of the above numbers. Please try again.")
            pass
    return num


# This function displays the available menu item in relation to the input. It takes 
# in an array with defined strings seperated by a comma and outputs a display menu with
# numbers and strings fitted together to form new options. 
    
def displayMenu(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Choose an item by entering a number from 1 to {0}: ".format(len(options)))
    return choice