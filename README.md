# pands-project
## GMIT project for Programming and Scripting Module 2019
#### Created by: Mark Cotter, Email: g00376335@gmit.ie
### LAST UPDATED 2019-03-31

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

The data relates to the classification of 3 variant classes of Iris flower based on
their characteristics with fifty instances of each class. Data was presented giving
four attributes relating to the variation within each class and a fifth attribute for
the class variant name, namely:

Five attributes in Fisher's Iris data set [1]

    A) Sepal length in cm
    B) Sepal width in cm 
    B) Petal length in cm
    D) Petal width in cm
    E) Class variant name

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

Fisher's Iris data set can be downloaded online [7] as the file labeled 'iris.data',
which can be saved as a .csv file. The data set file has been included in this
project folder for reference saved as 'iris-data-set.csv'.

Online observations [8] highlight the data in Fisher's Iris data set [1] is of good
quality and is based on real life data. The quantity of data is large enough to be
of use, but small enough to be portable and easily experimented with. It is also
numerical. All of which makes it an ideal data set for teaching purposes.


## Investigatory python code

### 2019-03-31 Initial program code
I created a python program called 'analyse.py' version V1_01 to import and anylyse
the Fisher's Iris data set. I added the script for the program to the folder linked
to the git repository for this project.

As I might need them, I decided to get started by importing the python modules numpy,
pandas, matplotlib.pyplot and sys. I abbreviated the longer modules to np, pd and pl
for ease later use in the code.

I used the sys argument to identify that a second additional argument after the program name was required for the csv filename. I read on pandas website
http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
about read csv files into python and decided to try it using the pd.read_csv command.

I noticed that the test print of the data only gave 149 rows and that the first row
of the data was used for the data title so I decided to add title row in the csv file.
I added the following title row before the first row in the dataset for the following
data

    - Sepal-length,Sepal-width,Petal-length,Petal-width,Variant-name

This gave me a dataframe with 150 rows 5 columns and with column row titles

To investigate what content was included in the data I used the pd.groupby() function
to group the data by the variant Name and undertook a few test prints of
the results. I found that there were three groups 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'.

I split the data into 3 groups using the grouped.get_group() command.
I used the pd.describe() module to get a description of the data including

    1) count
    2) mean
    3) std - Standard Deviation
    4) min - minimum value
    5) 25% - value
    6) 50% - value
    7) 75% - value
    8) max - maximum value

## Code reference sources:
1. Dr Ian McLoughlin, GMIT: H Dip in Data Analytics lecture notes,
   Code adapted from the Week 9 lecture for plotting using matplotlib and numpy
   modules and command line arguments in python.

2. Code adapted for using pandas from website
   http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

3. Code adapted from Mark Cotter pands problem set Exercise 9 - second.py
   and Week 9 lecture for checking for correct input arguments.
 
4. Code adapted for grouping data using pandas from website
   http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby

## Summary of the data investigations

### Initial data review

After reading the iris dataset csv file into the python program for this project
'analyse.py', I observed that there were three variant names included within the
dataset 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'.

Spliting the data into three groups based on these names allowed a description summary of each group be generated. Over the fifty values in each group, when the minimum, maximum and mean values for petal length and petal width are compared, the
values for 'Iris-setosa' were much lower than for the 'Iris-versicolor' and 'Iris-virginica'.

This variation confirmed previous research [1] noting that the data for Iris Setosa)
is easily separable from the other two linearly, but there is some overlap between
the other two classes making it difficult to distinguish from each other.


## Supporting tables and graphics




## References

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
