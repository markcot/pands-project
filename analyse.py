# pands-project
# GMIT project for Programming and Scripting Module 2019
# pands project - analyse.py
# Mark Cotter, V1_05, 2019-04-06

# V1_05 - 2019-04-06 (b)
# Header names changed
# Create options for plot different plots
# Figure 1 and Figure 2 plots of data created

# V1_04 - 2019-04-06 (a)
# Edit initial import if statement
# Groups variables renamed
# Rounding added

# V1_03 - 2019-04-05
# Create and edit summary csv files

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
import matplotlib.pyplot as pl
# Opens the python sys module
# Code adpted from Week 9 lecture of command line arguments in python
import sys

# Datframe df is for saving the content of the csv file

# Test to check if number of arguments supplied is = 2
# Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
if len(sys.argv) != 2:
    # print error message and the program does nothing
    # Exit the program Code adapted from https://stackoverflow.com/q/17179615
    sys.exit("Input Error: A single csv filename for input should be included.")
# End of test for second argument

# Read the csv file at the second argument called on the command line
# The formated code with {} refers to the second argument of the python
# list on the command line do the open command opens the first file on the
# command line. after >>python analyse.py ... 
# 
# Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
# and from website
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
df = pd.read_csv(f'{sys.argv[1]}', header=None)
# Add header row Code adapted from https://stackoverflow.com/a/34094058
df.columns = ['Sepal Length', 'Sepal Width',
    'Petal Length' , 'Petal Width', 'Name']

# Test print of start of the csv content
#print(df.head())

# Group the data by variant name
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
grouped = df.groupby('Name')

# Test print of the first line in each group
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
#print("\nThe following is the first entry for each group in the data set:")
#print(grouped.first())

# Split the data into groups. Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
df_set = grouped.get_group('Iris-setosa')
df_ver = grouped.get_group('Iris-versicolor')
df_vir = grouped.get_group('Iris-virginica')

# Test print of Group 1, 2 & 3
#print("\nGroup 'Iris Setosa' is the following.")
#print(df_set)
#print("\nGroup 'Iris Versicolor' is the following.")
#print(df_ver)
#print("\nGroup 'Iris Virginica' is the following.")
#print(df_vir)

# Test Print summaries of Group 1, 2 & 3
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
#print("\nGroup 'Iris Setosa' summary is as follows.")
#print(df_set.describe())
#print("\nGroup 'Iris Versicolor' summary is as follows.")
#print(df_ver.describe())
#print("\nGroup 'Iris Virginica' summary is as follows.")
#print(df_vir.describe())    

# Output decriptions to csv file. Code adapted from
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
df_set.describe().to_csv('Iris-setosa_summary.csv')
df_ver.describe().to_csv('Iris-versicolor_summary.csv')
df_vir.describe().to_csv('Iris-virginica_summary.csv')

# Import descriptions as new dataframes
df_set_des = pd.read_csv('Iris-setosa_summary.csv')
df_ver_des = pd.read_csv('Iris-versicolor_summary.csv')
df_vir_des = pd.read_csv('Iris-virginica_summary.csv')

# Add names to the first entry of the csv summary files Code adapted from
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
df_set_des.columns = ['Iris Setosa', 'Sepal Length', 'Sepal Width',
                        'Petal Length' , 'Petal Width']
df_ver_des.columns = ['Iris Versicolor', 'Sepal Length', 'Sepal Width',
                        'Petal Length' , 'Petal Width']
df_vir_des.columns = ['Iris Virginica', 'Sepal Length', 'Sepal Width',
                        'Petal Length' , 'Petal Width']

# Round summary data to 2 decimal places Code adapted from
# https://www.geeksforgeeks.org/python-pandas-dataframe-round/
df_set_des = df_set_des.round(2)
df_ver_des = df_ver_des.round(2)
df_vir_des = df_vir_des.round(2)

# Print summaries of 3 Groups
#print("\nSummary of the three groups is as follows.")
#print(df_set_des)
#print('\n', df_ver_des)
#print('\n', df_vir_des)  

# Update the csv files with the correct headers
# Code for removing index column from export adapted from
# https://stackoverflow.com/a/25230582
df_set_des.to_csv('Iris-setosa_summary.csv', index = False)
df_ver_des.to_csv('Iris-versicolor_summary.csv', index = False)
df_vir_des.to_csv('Iris-virginica_summary.csv', index = False)

# Ask user if they want plot option number they want to use Code adapted
# from Mark Cotter Exercise 1 - sumupto.py
# Set initial state for variable 'i'
i = 1
# Request user to enter a positive integer and assign the value to 'i'
# Inputted value has to be an integer type value (not a float or string)
i = (input('''\nWhat do you want to plot?
0 - Exit without plotting
1 - Sepal Length vs. Sepal Width
2 - Petal Length vs. Petal Width
Please enter the number of the option above: '''))

# Try to check if inputted value for 'i' is a positive integer
try:
    # Try to convert 'i' to an integer type
    i = int(i)
    # If 'i' is an non-zero positive integer
    if i >= 0:
        # Exit
        if i == 0:
            # Print
            print('Exiting program')

        # Plot Option 01
        elif i == 1:
            # Temporary variables for plotting. Code adapted from
            # https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
            # Select column for 'Sepal Length' in dataframe df_set
            a = (df_set.loc[:,'Sepal Length'])
            # Select column for 'Sepal Width' in dataframe df_set
            b = (df_set.loc[:,'Sepal Width'])
            # Select column for 'Sepal Length' in dataframe df_ver
            c = (df_ver.loc[:,'Sepal Length'])
            # Select column for 'Sepal Width' in dataframe df_ver
            d = (df_ver.loc[:,'Sepal Width'])
            # Select column for 'Sepal Length' in dataframe df_vir
            e = (df_vir.loc[:,'Sepal Length'])
            # Select column for 'Sepal Width' in dataframe df_vir
            f = (df_vir.loc[:,'Sepal Width'])

            # Plot the scatter plot
            # Code adapted from https://stackoverflow.com/a/47403507 &
            # https://stackoverflow.com/a/12608937 &
            # https://stackoverflow.com/a/47668614
            fig = pl.figure(figsize=(10,5))
            ax = fig.add_subplot(111)
            ax.set_title('Figure 1 - Plot of Sepal Length vs. Sepal Width')
            ax.scatter(a, b, s=20, c='b', marker='o', label='Setosa')
            ax.scatter(c, d, s=20, c='r', marker='o', label='Versicolor')
            ax.scatter(e, f, s=20, c='g', marker='o', label='Virginica')
            ax.set_xlabel('Sepal Length')
            ax.set_ylabel('Sepal Width')
            ax.legend(loc='best')
            pl.show()
        # Plot Option 02
        elif i == 2:
            # Temporary variables for plotting. Code adapted from
            # https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
            # Select column for 'Petal Length' in dataframe df_set
            a = (df_set.loc[:,'Petal Length'])
            # Select column for 'Petal Width' in dataframe df_set
            b = (df_set.loc[:,'Petal Width'])
            # Select column for 'Petal Length' in dataframe df_ver
            c = (df_ver.loc[:,'Petal Length'])
            # Select column for 'Petal Width' in dataframe df_ver
            d = (df_ver.loc[:,'Petal Width'])
            # Select column for 'Petal Length' in dataframe df_vir
            e = (df_vir.loc[:,'Petal Length'])
            # Select column for 'Petal Width' in dataframe df_vir
            f = (df_vir.loc[:,'Petal Width'])

            # Plot the scatter plot
            # Code adapted from https://stackoverflow.com/a/47403507 &
            # https://stackoverflow.com/a/12608937 &
            # https://stackoverflow.com/a/47668614
            fig = pl.figure(figsize=(10,5))
            ax = fig.add_subplot(111)
            ax.set_title('Figure 2 - Plot of Petal Length vs. Petal Width')
            ax.scatter(a, b, s=20, c='b', marker='o', label='Setosa')
            ax.scatter(c, d, s=20, c='r', marker='o', label='Versicolor')
            ax.scatter(e, f, s=20, c='g', marker='o', label='Virginica')
            ax.set_xlabel('Petal Length')
            ax.set_ylabel('Petal Width')
            ax.legend(loc='best')
            pl.show()
        # Prints a VALUE error message if 'i' is not an integer > 0
        else:
            print("Input Error: -->", i, "<-- is not a option.")

# Prints a TYPE exception error if 'i' not an integer
except:
    print("Input Error: -->", i, "<-- is not an integer type.")


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
#     https://stackoverflow.com/a/34094058
#
# [E] Code adapted for grouping data, getting groups and decribing groups using
#     pandas from website
#     http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
#
# [F] Code for Pandas output to csv file and selecting columns adapted from website
#     https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
#
# [G] Code for removing index column from export adapted from 
#     https://stackoverflow.com/a/25230582
#
# [H] Exit program Code adapted from https://stackoverflow.com/q/17179615
#
# [I] Round summary data to 2 decimal places Code adapted from
#     https://www.geeksforgeeks.org/python-pandas-dataframe-round/
#
# [J] Code adapted from Mark Cotter pands problem set Exercise 1 - sumupto.py
#     to ask user if they want plot option number they want to use.
#     
# [K] Code for using code for Matplotlib scatter plot adapted from
#     https://stackoverflow.com/a/47403507
#
# [L] Code for labelling axes adapted from https://stackoverflow.com/a/12608937
#
# [M] Code for adding legend adapted from https://stackoverflow.com/a/47668614