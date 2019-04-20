# pands-project
# GMIT project for Programming and Scripting Module 2019
# pands project - analyse.py
# Mark Cotter, V1_08, 2019-04-20

# V1_08 - 2019-04-20
# Add comparison of Ratio of Sepal Length/Sepal Width vs Petal Length/Petal Width
# and Ratio of Sepal/Petal Length vs Sepal/Petal Width

# V1_07 - 2019-04-06 (d)
# Figure ploting made into a function
# Print statements and comments edited 

# V1_06 - 2019-04-06 (c)
# Update to Figure sizes made

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
# The program analyses the iris data set, outputs a number of csv summary files
# and gives the user an option to create a number of different scatter plots.
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

# Function for creating a scatter plot Figure
# Take as input the a 3 dataframes names, 3 data labels strings
# 2 column names strings and 1 figure title string.
def plot_df_sca_comp(df1, df2, df3, lab1, lab2, lab3, col1, col2, figtitle):
    # Temporary variables for plotting. Code adapted from
    # https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
    # Select column for 'col1' in dataframe df1
    a = (df1.loc[:,str(col1)])
    # Select column for 'col2' in dataframe df1
    b = (df1.loc[:,str(col2)])
    # Select column for 'col1' in dataframe df2
    c = (df2.loc[:,str(col1)])
    # Select column for 'col2' in dataframe df2
    d = (df2.loc[:,str(col2)])
    # Select column for 'col1' in dataframe df3
    e = (df3.loc[:,str(col1)])
    # Select column for 'col2' in dataframe df3
    f = (df3.loc[:,str(col2)])
    # Plot the scatter plot
    # Code adapted from https://stackoverflow.com/a/47403507 &
    # https://stackoverflow.com/a/12608937 &
    # https://stackoverflow.com/a/47668614
    # Size of the Figure
    fig = pl.figure(figsize=(7,5))
    ax = fig.add_subplot(111)
    # Title of the Figure
    ax.set_title(str(figtitle))
    # Add scatter points for variable 'a' and 'b' with label 'lab1'
    ax.scatter(a, b, s=20, c='b', marker='o', label=str(lab1))
    # Add scatter points for variable 'c' and 'd' with label 'lab2'
    ax.scatter(c, d, s=20, c='r', marker='o', label=str(lab2))
    # Add scatter points for variable 'e' and 'f' with label 'lab3'
    ax.scatter(e, f, s=20, c='g', marker='o', label=str(lab3))
    # Add x-axis label 'col1'
    ax.set_xlabel(str(col1))
    # Add x-axis label 'col2'
    ax.set_ylabel(str(col2))
    # Add legens labels 'lab1', 'lab2' & 'lab3'
    ax.legend(loc='best')
    # Plot the Figure to an image
    pl.show()    
# End of Function

# Dataframe df is for saving the content of the csv file
# Test to check if number of arguments supplied is = 2
# Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
if len(sys.argv) != 2:
    # print error message and the program does nothing
    # Exit the program Code adapted from https://stackoverflow.com/q/17179615
    sys.exit('''\nInput Error: A single csv filename for input should be included.
            \nEnd of program
            ''')
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
print('\nThe first few lines in the data set are as follows:\n',
        df.head())

# Group the data by variant name
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
grouped = df.groupby('Name')

# Test print of the first line in each group
# Code adapted from website
# http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
print("\nThe first entry for each group in the data set are as follows:")
print(grouped.first())

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
print('\nThere are three groups in the data set',
        '\nA summary of the three groups is as follows:')
print('\n', df_set_des)
print('\n', df_ver_des)
print('\n', df_vir_des)  

# Update the csv files with the correct headers
# Code for removing index column from export adapted from
# https://stackoverflow.com/a/25230582
df_set_des.to_csv('Iris-setosa_summary.csv', index = False)
df_ver_des.to_csv('Iris-versicolor_summary.csv', index = False)
df_vir_des.to_csv('Iris-virginica_summary.csv', index = False)

# Add 4 new columns to the 3 grouped dataframes
# 1) Ratio of Sepal Length/Sepal Width
# 2) Ratio of Petal Length/Petal Width
# 3) Ratio of Sepal Length/Petal Length
# 4) Ratio of Sepal Width/Petal Width
# 5) Ratio of Sepal Length/Petal Width
# 6) Ratio of Sepal Width/Petal Length
# Code adapted from website https://thispointer.com/python-pandas-how-to-add-new-columns-in-a-dataframe-using-or-dataframe-assign/
# and https://www.interviewqs.com/ddi_code_snippets/add_new_col_df_default_value
# Ratios for Iris Setosa
df_set.insert(4, 'R_SpL_SpW', df_set.loc[:,'Sepal Length'] / df_set.loc[:,'Sepal Width'])
df_set.insert(5, 'R_PeL_PeW', df_set.loc[:,'Petal Length'] / df_set.loc[:,'Petal Width'])
df_set.insert(6, 'R_SpL_PeL', df_set.loc[:,'Sepal Length'] / df_set.loc[:,'Petal Length'])
df_set.insert(7, 'R_SpW_PeW', df_set.loc[:,'Sepal Width'] / df_set.loc[:,'Petal Width'])
df_set.insert(8, 'R_SpL_PeW', df_set.loc[:,'Sepal Length'] / df_set.loc[:,'Petal Width'])
df_set.insert(9, 'R_SpW_PeL', df_set.loc[:,'Sepal Width'] / df_set.loc[:,'Petal Length'])

# Ratios for Iris Versicolor
df_ver.insert(4, 'R_SpL_SpW', df_ver.loc[:,'Sepal Length'] / df_ver.loc[:,'Sepal Width'])
df_ver.insert(5, 'R_PeL_PeW', df_ver.loc[:,'Petal Length'] / df_ver.loc[:,'Petal Width'])
df_ver.insert(6, 'R_SpL_PeL', df_ver.loc[:,'Sepal Length'] / df_ver.loc[:,'Petal Length'])
df_ver.insert(7, 'R_SpW_PeW', df_ver.loc[:,'Sepal Width'] / df_ver.loc[:,'Petal Width'])
df_ver.insert(8, 'R_SpL_PeW', df_ver.loc[:,'Sepal Length'] / df_ver.loc[:,'Petal Width'])
df_ver.insert(9, 'R_SpW_PeL', df_ver.loc[:,'Sepal Width'] / df_ver.loc[:,'Petal Length'])

# Ratios for Iris Virginica
df_vir.insert(4, 'R_SpL_SpW', df_vir.loc[:,'Sepal Length'] / df_vir.loc[:,'Sepal Width'])
df_vir.insert(5, 'R_PeL_PeW', df_vir.loc[:,'Petal Length'] / df_vir.loc[:,'Petal Width'])
df_vir.insert(6, 'R_SpL_PeL', df_vir.loc[:,'Sepal Length'] / df_vir.loc[:,'Petal Length'])
df_vir.insert(7, 'R_SpW_PeW', df_vir.loc[:,'Sepal Width'] / df_vir.loc[:,'Petal Width'])
df_vir.insert(8, 'R_SpL_PeW', df_vir.loc[:,'Sepal Length'] / df_vir.loc[:,'Petal Width'])
df_vir.insert(9, 'R_SpW_PeL', df_vir.loc[:,'Sepal Width'] / df_vir.loc[:,'Petal Length'])

# Test print of dataframe contents
#print('\n', df_set)
#print('\n', df_ver)
#print('\n', df_vir)

# Ask user if they want plot option number they want to use Code adapted
# from Mark Cotter Exercise 1 - sumupto.py
# Set initial state for variable 'i'
i = 1
# Request user to enter a positive integer and assign the value to 'i'
# Inputted value has to be an integer type value (not a float or string)
i = (input('''\nDo you want to plot a Figure?
0 - Exit without plotting
1 - Sepal Length vs. Sepal Width
2 - Petal Length vs. Petal Width
3 - Sepal Length vs. Petal Length
4 - Sepal Width vs. Petal Width
5 - Ratio Sepal Length/Width vs. Petal Length/Width
6 - Ratio Sepal Length/Petal Length vs. Sepal Width/Petal Width
7 - Ratio Sepal Length/Petal Width vs. Sepal Width/Petal Length\n
Please enter the number of an option listed above: '''))

# Try to check if inputted value for 'i' is a positive integer
try:
    # Try to convert 'i' to an integer type
    i = int(i)
    # If 'i' is an non-zero positive integer
    if i >= 0:
        # Exit program
        if i == 0:
            # Note to user that the program is finished
            print('\nEnd of program')

        # Plot Option 01
        elif i == 1:
            # Plot function for Figure 1 - Plot of Sepal Length vs. Sepal Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'Sepal Length', 'Sepal Width',
                'Figure 1 - Plot of Sepal Length vs. Sepal Width')
            # Note to user that the program is finished
            print('\nEnd of program')

        # Plot Option 02
        elif i == 2:
            # Plot function for Figure 2 - Plot of Petal Length vs. Petal Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'Petal Length', 'Petal Width',
                'Figure 2 - Plot of Petal Length vs. Petal Width')
            # Note to user that the program is finished
            print('\nEnd of program')

        # Plot Option 03
        elif i == 3:
            # Plot function for Figure 3 - Sepal Length vs. Petal Length
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.            
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'Sepal Length', 'Petal Length',
                'Figure 3 - Plot of Sepal Length vs. Petal Length')
            # Note to user that the program is finished
            print('\nEnd of program')
        
        # Plot Option 04
        elif i == 4:
            # Plot function for Figure 4 - Sepal Width vs. Petal Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.  
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'Sepal Width', 'Petal Width',
                'Figure 4 - Plot of Sepal Width vs. Petal Width')  
            print('\nEnd of program')

        # Plot Option 05
        elif i == 5:
            # Plot function for Figure 5 - Ratio of Sepal Length/Width vs. Petal Length/Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.  
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'R_SpL_SpW', 'R_PeL_PeW',
                'Figure 5 - Plot of ratio Sepal Length/Width vs. Petal Length/Width')  
            print('\nEnd of program')

        # Plot Option 06
        elif i == 6:
            # Plot function for Figure 6 - Ratio Sepal/Petal Length vs. Sepal/Petal Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.  
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'R_SpL_PeL', 'R_SpW_PeW',
                'Figure 6 - Plot of ratio Sepal/Petal Length vs. Sepal/Petal Width')  
            print('\nEnd of program')

        # Plot Option 07
        elif i == 7:
            # Plot function for Figure 7 - Ratio Sepal Length/Petal Width vs. Sepal Length/Petal Width
            # Take as input 3 dataframes names, 3 data labels strings
            # 2 column names strings and 1 figure title string.  
            plot_df_sca_comp(df_set, df_ver, df_vir,
                'Setosa', 'Versicolor', 'Virginica',
                'R_SpL_PeW', 'R_SpW_PeL',
                'Figure 7 - Plot of ratio Sepal Length/Petal Width vs. Sepal Length/Petal Width')  
            print('\nEnd of program')

        # Prints a VALUE error message if 'i' is not an integer > 0
        # Note to user that the program is finished
        else:
            print('\nInput Error: -->', i, '<-- is not a option listed above.\n',
                    '\nEnd of program')
    # Prints a VALUE error message if 'i' is not an integer > 0
    # Note to user that the program is finished
    else:
        print('\nInput Error: -->', i, '<-- is not a option listed above.\n',
                '\nEnd of program')
# Prints a TYPE exception error if 'i' not an integer
# Note to user that the program is finished
except:
    print('\nInput Error: -->', i, '<-- is not an number type listed above.\n',
            '\nEnd of program')

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
#
# [N] Code for adding dataframe column adapted from websites
#     https://thispointer.com/python-pandas-how-to-add-new-columns-in-a-dataframe-using-or-dataframe-assign/
#     and https://www.interviewqs.com/ddi_code_snippets/add_new_col_df_default_value
# [O] Code for seaborn adapted from website
#     https://seaborn.pydata.org/examples/scatterplot_matrix.html