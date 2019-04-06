# pands-project
# GMIT project for Programming and Scripting Module 2019
# pands project - analyse.py
# Mark Cotter, V1_04, 2019-04-06

# V1_04 - 2019-04-06
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
df.columns = ['Sepal-length', 'Sepal-width',
    'Petal-length' , 'Petal-width', 'Name']

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

# Split the data into groups. Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
df_set = grouped.get_group('Iris-setosa')
df_ver = grouped.get_group('Iris-versicolor')
df_vir = grouped.get_group('Iris-virginica')

# Test print of Group 1, 2 & 3
#print("\nGroup 'Iris-setosa' is the following.")
#print(df_set)
#print("\nGroup 'Iris-versicolor' is the following.")
#print(df_ver)
#print("\nGroup 'Iris-virginica' is the following.")
#print(df_vir)

# Test Print summaries of Group 1, 2 & 3
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
#print("\nGroup 'Iris-setosa' summary is as follows.")
#print(df_set.describe())
#print("\nGroup 'Iris-versicolor' summary is as follows.")
#print(df_ver.describe())
#print("\nGroup 'Iris-virginica' summary is as follows.")
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
df_set_des.columns = ['Iris-setosa', 'Sepal-length', 'Sepal-width',
                        'Petal-length' , 'Petal-width']
df_ver_des.columns = ['Iris-versicolor', 'Sepal-length', 'Sepal-width',
                        'Petal-length' , 'Petal-width']
df_vir_des.columns = ['Iris-virginica', 'Sepal-length', 'Sepal-width',
                        'Petal-length' , 'Petal-width']

# Round summary data to 2 decimal places Code adapted from
# https://www.geeksforgeeks.org/python-pandas-dataframe-round/
df_set_des = df_set_des.round(2)
df_ver_des = df_ver_des.round(2)
df_vir_des = df_vir_des.round(2)

# Print summaries of 3 Groups
print("\nSummary of the three groups is as follows.")
print(df_set_des)
print('\n', df_ver_des)
print('\n', df_vir_des)  

# Update the csv files with the correct headers
# Code for removing index column from export adapted from
# https://stackoverflow.com/a/25230582
df_set_des.to_csv('Iris-setosa_summary.csv', index = False)
df_ver_des.to_csv('Iris-versicolor_summary.csv', index = False)
df_vir_des.to_csv('Iris-virginica_summary.csv', index = False)

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
# [F] Code for Pandas output to csv file adapted from website
#     https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
#
# [G] Code for removing index column from export adapted from 
#     https://stackoverflow.com/a/25230582
#
# [H] Exit program Code adapted from https://stackoverflow.com/q/17179615
#
# [I] Round summary data to 2 decimal places Code adapted from
#     https://www.geeksforgeeks.org/python-pandas-dataframe-round/
