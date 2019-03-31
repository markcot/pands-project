# pands-project
# GMIT project for Programming and Scripting Module 2019
# pands project - analyse.py
# Mark Cotter, V1_01, 2019-03-31

# V1_02 - 2019-03-31 (b)
# Column header row added to the data import
# Comment updated

# V1_01 - Program created 2019-03-31 (a)
# Import modules, import csv file and review groups

# A program to read an input from a csv file of the 'Fisher’s Iris data set'
# The program analyses the iris data set and makes a few plots.
#
# The program takes a single additional filename from an argument on the command
# line. Note that a single additional text filename has to be specified after the
# program # name. e.g. >>python analyse.py iris-data-set.csv
# The program prints an error if no additional filename is provided
# The program prints an error if two or more additional filenames are provided 

# import matplotlib pyplot, numnpy and pandas modules abbreviated to np, pd & pl
# Code from Week 9 lecture & website
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
import numpy as np
import pandas as pd
#import matplotlib.pyplot as pl
# Opens the python sys module
# Code adpted from Week 9 lecture of command line arguments in python
import sys

# Datframe df is for saving the content of the csv file

# Test to check if number of arguments supplied is = 2
# Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
if len(sys.argv) != 2:
    # print error message and the program does nothing
    print("Input Error: A single csv filename for input should be included.")
# Otherwise do the following:
else:
    # Read the csv file at the second argument called on the command line
    # The formated code with {} refers to the second argument of the python
    # list on the command line do the open command opens the first file on the
    # command line. after >>python analyse.py ... 
    # 
    # Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
    # and from websites
    # http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
    # https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
    df = pd.read_csv(f'{sys.argv[1]}', header=None)
    df.columns = ["Sepal-length", "Sepal-width",
        "Petal-length" , "Petal-width", "Name"]

    # Test print of start of the csv content
    #print(pd.head())

    # Group the data by Variant name
    # Code adapted from website
    # http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
    grouped = df.groupby('Name')

    # Test print of the first line in each group
    # Code adapted from website
    # http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
    print("\nThe following is the first entry for each group in the data set.")
    print(grouped.first())

    # Split the data into groups
    # Code adapted from website
    # http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
    groupone = grouped.get_group('Iris-setosa')
    grouptwo = grouped.get_group('Iris-versicolor')
    groupthree = grouped.get_group('Iris-virginica')

    # Test print of Group 1, 2 & 3
    #print("\nGroup 'Iris-setosa' is the following.")
    #print(groupone)
    #print("\nGroup 'Iris-versicolor' is the following.")
    #print(grouptwo)
    #print("\nGroup 'Iris-virginica' is the following.")
    #print(groupthree)

    # Print summaries of Group 1, 2 & 3
    # Code adapted from website
    # http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
    print("\nGroup 'Iris-setosa' summary is as follows.")
    print(groupone.describe())
    print("\nGroup 'Iris-versicolor' summary is as follows.")
    print(grouptwo.describe())
    print("\nGroup 'Iris-virginica' summary is as follows.")
    print(groupthree.describe())    

# End of program


# Code reference sources:
# [A] Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
#     Code adapted from the Week 9 lecture for plotting using matplotlib and numpy
#     modules and command line arguments in python.
#
# [B] Code adapted for using pandas from website
#     http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
#
# [C] Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
#     and Week 9 lecture for checking for correct input arguments.
# 
# [D] Code for editing header row to a pandas dataframe adapted from website
#     https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
#
# [E] Code adapted for grouping data, getting groups and decribing groups using
#     pandas from website
#     http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
