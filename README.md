# pands-project
## GMIT project for Programming and Scripting Module 2019
#### Created by: Mark Cotter, Email: g00376335@gmit.ie
#### LAST UPDATED 2019-04-06

## Introduction
This project concerns the well-known 'Fisher’s Iris data set' [1].
The project entails researching the data set, writing documentation and
code in the Python programming language [2] based on that research.

The data set has been widely investigated and written about it, much of which has
published online in the field of pattern recognition and machine learning.

## Research

The data set [1] was introduced in a paper by botanist Ronald A. Fisher in 1936, but
was originally collected in 1935 and published in 1936 by botanist Edgar S. Anderson
[3]. The data set is also referred to as 'Anderson's Iris data set'.

The data relates to the classification of three variant classes of Iris flower based
on their characteristics with fifty instances of each class. Data was presented giving
four attributes relating to the variation within each class and a fifth attribute for
the class variant name, namely:

Five attributes in Fisher's Iris data set [1]

    A) Sepal Length in cm
    B) Sepal Width in cm 
    B) Petal Length in cm
    D) Petal Width in cm
    E) Class Variant Name

Three Iris flower class variant names in Fisher's Iris data set [1]

    1) Iris Setosa
    2) Iris Versicolour
    3) Iris Virginica

Sepals are outermost oragns of a flower that form a protective casing for the
developing flower bud inside and support the flower. They are usually green and leaf
like [4]. Petals are the organ of a flower that are often noticeably coloured to
attract pollinators [5].

Previous research [1] has shown that one class in the data set (Iris Setosa) is
easily separable from the other two linearly. There is some overlap between the other
two classes making it difficult to distinguish from each other. A previous report [6]
on the data set noted that two of species were all collected on the same day from the
same pasture in Gaspe Peninsula and measured by the same person with the same
apparatus.

There are known errors [1] in the 35th and 38th samples. Sample 35 has an error in
the fourth attribute and sample 38 has an error in the second and third attribute.
The corrected data set instances should be:

    Sample 35) 4.9,3.1,1.5,0.2,"Iris-setosa"
    Sample 38) 4.9,3.6,1.4,0.1,"Iris-setosa"

Fisher's Iris data set can be downloaded online [7] listed as the file labeled
'iris.data', which can be saved as a .csv extension file. The data set file has been
included in this git project folder for reference saved as 'iris-data-set.csv'.

Online observations [8] highlight the data in Fisher's Iris data set [1] is of good
quality and is based on real life data. The quantity of data is large enough to be
of use, but small enough to be portable and easily experimented with. It is also
numerical. All of which makes it an ideal data set for teaching purposes.

Typical graphs produced for reviewing the Fisher Iris data [9] plot scatter plots
and histograms of the comparing each of the four column variables.

## Investigatory python code

### Initial program code
I created a python program called 'analyse.py' version V1_01 to import and anylyse
the Fisher's Iris data set. I added the script for the program to the folder linked
to the git repository for this project.

I decided to get started by importing the python modules numpy, pandas,
matplotlib.pyplot and sys. I abbreviated the longer modules to np, pd and pl
for ease later use in the code [A] & [B].

I used the sys argument to identify that a second additional argument after the program name was required for the csv filename [C]. I read on pandas website [B]
about read csv files into python and decided to try it using the pd.read_csv command.
In V1_04 I added a sys.exit() [H] if the second argument was missing.

I noticed that the test print of the data only gave 149 rows and that the first row
of the data was used for the data header so I decided to add header row to the data
from the csv file.

I found that this can be resolved using the 'header=None' command and add the following columns using the df.column function. I added this function in V1_02
I adapted code from a website [D] to achieve this result.

    - 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Name'

This gave me a dataframe with 150 rows 5 columns and with a column header row

I adapted code for pd.groupby(), grouped.get_group() and pd.describe() modules
from a website [E].

To investigate what content was included in the data I used the pd.groupby() function
to group the data by the variant Name.
I undertook a few test prints of the results. I noted that there were three groups 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica' included in the dataset.

I split the data into 3 groups using the grouped.get_group() command.
I used the pd.describe() module to get a description of the data including the
following:

    1) count
    2) mean
    3) std - Standard Deviation
    4) min - minimum value
    5) 25% - value
    6) 50% - value
    7) 75% - value
    8) max - maximum value

## Summary of the Data Investigations

### Initial data review

After reading the iris dataset csv file into the python program for this project
'analyse.py', I observed that there were three variant names included within the
dataset 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'.

Spliting the data into three groups based on these names allowed a description summary of each group be generated. Over the fifty values in each group, when the minimum, maximum and mean values for sepal length and sepal width are compared, the
values for 'Iris-setosa' were much lower than the values for the 'Iris-versicolor'
and 'Iris-virginica'. Refer to Tables 1, 2 and 3 below.

This variation confirmed previous research [1] noting that the data for Iris Setosa
is easily separable from the other two linearly, but there is some overlap between
the other two classes making it difficult to distinguish from each other.

### Summary of initial data review

I decided to try and get make a table of the description data from the initial review
In V1_03 I adapted code from a website [F] to output dataframes to a csv file and
exported the summaries to csv files. I reimported the csv files as new dataframes and
added a new header row using code adapted from a website [G] and updated the csv 
files with the revised header rows. In V1_04, I rounded the values to 2 decimal place
[I] and I now had clean csv file information that can be used for producing summary
tables. Refer to Tables 1, 2 and 3 below.

### Detailed Analysis of the data

To compare the data in more detail I created some options to create plots of the data.
I wrote code to display plots of the data to compare 'Sepal Length vs. Sepal Width'
and 'Petal Length vs. Petal Width'. In V1_05, I used code adapted from websites ([E],
[J], [K] & [M]) to plot scatter plot for the three groups using 3 different colours.
Refer to Figure 1 and Figure 2 below.

## Supporting Tables and Graphics

### Summary Tables
Refer to layout from website reference [i]

#### Table 1 -Summary of Iris Setosa Data
| Iris Setosa | Sepal Length | Sepal Width | Petal Length | Petal Width |
| :---: | :---: | :---: | :---: | :---: |
| Count | 50.0 | 50.0 | 50.0 | 50.0 |
| Mean | 1.46 | 0.24 | 5.01 | 3.42 |
| Std | 0.17 | 0.11 | 0.35 | 0.38 |
| Min | 1.0 | 0.1 | 4.3 | 2.3 |
| Max | 1.9 | 0.6 | 5.8 | 4.4 |

#### Table 2 -Summary of Iris Versicolor Data
| Iris Versicolor | Sepal Length | Sepal Width | Petal Length | Petal Width |
| :---: | :---: | :---: | :---: | :---: |
| Count | 50.0 | 50.0 | 50.0 | 50.0 |
| mean | 4.26 | 1.33 | 5.94 | 2.77 |
| std | 0.47 | 0.2 | 0.52 | 0.31 |
| min | 3.0 | 1.0 | 4.9 | 2.0 |
| max | 5.1 | 1.8 | 7.0 | 3.4 |

#### Table 3 -Summary of Iris Virginica Data
| Iris Virginica | Sepal Length | Sepal Width | Petal Length | Petal Width |
| :---: | :---: | :---: | :---: | :---: |
| Count | 50.0 | 50.0 | 50.0 | 50.0 |
| mean | 5.55 | 2.03 | 6.59 | 2.97 |
| std | 0.55 | 0.27 | 0.64 | 0.32 |
| min | 4.5 | 1.4 | 4.9 | 2.2 |
| max | 6.9 | 2.5 | 7.9 | 3.8 |

### Figures
Refer to layout from website reference [ii]

#### Figure 1
![alt text](https://raw.githubusercontent.com/markcot/pands-project/Figure_1.jpeg)

#### Figure 2
![alt text](https://raw.githubusercontent.com/markcot/pands-project/Figure_2.jpeg)


## Research References

[1] UC Irvine Machine Learning Repository. Iris data set
    http://archive.ics.uci.edu/ml/datasets/Iris.

[2] Python Software Foundation. Welcome to python.org
    https://www.python.org/.

[3] Anderson's Iris data set
    https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/iris.html

[4] Flower anatomy: Sepal
    https://biologydictionary.net/sepal/
    
[5] Flower anatomy: Petal
    https://evolution.berkeley.edu/evolibrary/article/petal_01

[6] Report on Edgar Anderson's Iris Data Analysis
    https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis

[7] Fisher's data set download location
    http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

[8] Aspects that make the Iris data set a good teaching example
    https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching

[9] Typical graphs produced for reviewing the Fisher Iris data set from website
    https://www.digitalvidya.com/blog/top-5-data-science-projects-for-beginners/


## Code reference sources:
[A] Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
    Code adapted from the Week 9 lecture for plotting using matplotlib and numpy
    modules and command line arguments in python.

[B] Code adapted for using pandas from website
    http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

[C] Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
    and Week 9 lecture for checking for correct input arguments.

[D] Code for editing header row to a pandas dataframe adapted from website
    https://stackoverflow.com/a/34094058

[E] Code adapted for grouping data, getting groups and decribing groups using
    pandas from website
    http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby

[F] Code for Pandas output to csv file and selecting columns adapted from website
    https://www.datacamp.com/community/blog/python-pandas-cheat-sheet

[G] Code for removing index column from export adapted from 
    https://stackoverflow.com/a/25230582

[H] Exit program Code adapted from https://stackoverflow.com/q/17179615

[I] Round summary data to 2 decimal places Code adapted from
    https://www.geeksforgeeks.org/python-pandas-dataframe-round/

[J] Code adapted from Mark Cotter pands problem set Exercise 1 - sumupto.py
    to ask user if they want plot option number they want to use.

[K] Code for using code for Matplotlib scatter plot adapted from
    https://stackoverflow.com/a/47403507

[L] Code for labelling axes adapted from https://stackoverflow.com/a/12608937

[M] Code for adding legend adapted from https://stackoverflow.com/a/47668614    

## Git tools reference sources:

[i] Adding Tables and Figure to Git marked down file. Layout adapted from website
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables

[ii] Add image to Git hub Layout adpated from https://stackoverflow.com/a/14494775
