# pands-project
## GMIT project for Programming and Scripting Module 2019
#### Created by: Mark Cotter, Email: g00376335@gmit.ie
#### LAST UPDATED 2019-04-30

## Introduction
This project concerns the well-known 'Fisher’s Iris data set' [1].
The project entails researching the data set, writing documentation and
code in the Python programming language [2] based on that research.

The data set has been widely investigated and written about it, much of which has
published online in the field of pattern recognition and machine learning. The data set
file 'iris-data-set.csv' is used in this project.

The python code for this project is called 'analyse.py'. The code take a second input
argument on the command line. To run the code in the current working folder for this project,
enter on the command line the following text to run the code:

#### python analyse.py iris-data-set.csv

The code displays to the screen a number of summaries of the data set contents, outputs the
summaries to additional csv files and gives the user a number of options for plotting some
Figures.

## Data set Research
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

Sepals are outermost organs of a flower that form a protective casing for the
developing flower bud inside and support the flower. They are usually green and leaf
like [4]. Petals are the organ of a flower that are often noticeably coloured to
attract pollinators [5].

Previous research [1] has shown that one class in the data set (Iris Setosa) is
easily separable from the other two linearly. There is some overlap between the other
two classes making it difficult to distinguish from each other. A previous study [6]
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

## Initial Data Investigation
I created a python program called 'analyse.py' version V1_01 to import and analyse
the Fisher's Iris data set. I added the script for the program to the folder linked
to the git repository for this project.

I decided to get started by importing the python modules numpy, pandas,
matplotlib.pyplot and sys. I abbreviated the longer modules to np, pd and pl
for ease of use in the code [A] & [B].

As used in one of my previous coding projects [C], I used the sys argument to highlight to
the user that a second additional argument after the program name was required for the csv
filename [C]. I learned how to read csv files into python on the pandas website [B] and
decided to try it using the pd.read_csv command.
In V1_04 I added a sys.exit() [H] command if the second argument was missing. This allows me
to avoid using a very long if statement or loop checking for the correct input argument.

I noticed that the test print of the data only gave 149 rows and that the first row
of the data was used for the data header so I decided to add header row to the data
from the csv file. I identified that this can be resolved using the 'header=None' command
and add the following columns using the df.column function. I added this function in V1_02
I adapted code from a website [D] to achieve this result.

    - Sepal Length, Sepal Width, Petal Length, Petal Width, Name

This gave me a dataframe with 150 rows 5 columns and with a column header row.

Investigating the python pandas module online [E], I learned how to adapt code to
filter and summarize the data using pd.groupby(), grouped.first(), grouped.get_group() and
pd.describe() functions.

Using the pd.groupby() function, I grouped the content of the data I used the by the variant
Name. Using a few test prints grouped.first() function indicated that there were three
groups 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica' included in the data set.

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

### Initial Data Review
After reading in the iris data set csv file into the python program for this project
'analyse.py', I observed that there were three variant names included within the
data set 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'.

Splitting the data into three groups based on these names allowed a description summary of
each group be generated. Over the fifty values in each group, when the minimum, maximum and
mean values for sepal length and sepal width are compared, the
values for 'Iris-setosa' were much lower than the values for the 'Iris-versicolor'
and 'Iris-virginica'.

This variation confirmed previous research [1] noting that the data for Iris Setosa
is easily separable from the other two linearly, but there is some overlap between
the other two classes making it difficult to distinguish from each other.

### Conclusion of Initial Data Review
I decided to make a table of the description data from the initial review.
In V1_03 I adapted code from a website [F] to output dataframes to a csv file and
exported the summaries to csv files. Refer to 'Iris-setosa_summary.csv', 
'Iris-versicolor_summary.csv', and 'Iris-virginica_summary.csv' included in the
github repository.

I reimported the csv files as new dataframes and added new header rows using code
adapted from a website [G]. The program re-exported the csv files updating the 
existing files with the revised header rows.

In V1_04, I rounded the values to 2 decimal place [I] and I now had clean csv file
information that can be used for producing summary tables. The program re-exported
the csv files updating the existing files with the revised header rows.

This initial data review gave me a good understanding of how to use dataframes and use python
to manipulate data outputs and inputs on a iterative basis in order to achieve the desired
output. I also learned how to display tables in the marked down file [i].

Using data from the summary csv files I generated Table 1, Table 2 and Table 3 below. These
tables include summaries of each of the three variants with instance count, mean values,
standard deviation (std) values, minimum (min) values and maximum (max) values for each of
the four characteristics in the data set. 

## Detailed Data Investigation
To compare the data in more detail, I created some options to create plots of the
data. I wrote code to ask the user if they wanted to display some different type of
plots to compare 'Sepal Length vs. Sepal Width' and 'Petal Length vs. Petal Width'. In
V1_05, I used code adapted from websites ([E], [J], [K] & [M]) to plot scatter plot for
the three groups using 3 different colours. Refer to Figure 1 and Figure 2 as described
below. This was my first experience in using scatter plots and I found that they give a
good impression of the data.

In V1_06, I edited the size of the graphs. In V1_07 I add a function
plot_df_sca_comp() to shorten the program code and reuse the plotting code within the
function. I also added Figure 3 and Figure 4 as described below. I found that once the
function was written, it really helped to speed up writing code for additional scatter plots.

In V1_08, using code adapted from websites ([N]), I created additional columns
in the dataframes comparing ratios of Sepal Length/Width versus Petal Length/Width,
Sepal/Petal Length versus Sepal/Petal Width and Sepal Length/Petal Width versus
Sepal Width/Petal Length. The results are displayed in Figures 5, 6 and 7.

In V1_09, using code adapted from websites ([O] & [P]), I created overlapping histogram plots
to compare the frequency of each parameter in the data set. The results are displayed in
Figures 8, 9, 10 and 11. I found that importing the seaborn module slows down he running
of the program noticeable. Seborn can generate a deprecated warnings when using the distplot
function. Insofar as the histograms plotted correctly, I was able to turn off this warning
using code from website reference [Q]. In future I may limit use of importing the seaborn
module, as it appears to slow the run time of the program.

An example of a typical 'analyse.py' code run is indicated in Figure 12 and an example of the
input error code run is indicated in Figure 13.

### Detailed Data Analysis

#### Sepal Length versus Sepal Width
Comparing 'Sepal Length' to 'Sepal Width' as shown in Figure 1, 'Iris-setosa' is
easily distinguishable from the other two. 'Iris-virginica' and 'Iris-versicolor' have
significant overlap making this a poor comparison method for these three iris
variants.

####  Petal Length versus Petal Width
When the 'Petal Length' is compared with the 'Petal Width' in Figure 2, there is a
notable separation between all three variants. 'Iris-setosa' is at the bottom left of the
plot, 'Iris-virginica' is at the top right of the plot and 'Iris-versicolor' is
in the centre of the plot. There is some minor overlap between the 'Iris-virginica'
data and the 'Iris-versicolor' data. However 'Petal Length' related to 'Petal Width'
appears to be a good differentiating method for these three iris variants.

#### Sepal Length versus Petal Length
Figure 3 indicates the comparison of 'Sepal Length' and 'Petal Length' and has similar
properties to Figure 2. 'Iris-setosa' is well defined as a separate entity. 
'Iris-virginica' and 'Iris-versicolor' are separated, but with more overlap than 
shown in Figure 2. This comparison method is average, but not as accurate as 'Petal
Length' versus 'Petal Width' shown in Figure 2.

#### Sepal Width versus Petal Width
A comparison of 'Sepal Width' and 'Petal Width' shown in Figure 4 provides 
similar results as seen in Figure 2. 'Iris-setosa' is well defined as a separate
entity. 'Iris-virginica' and 'Iris-versicolor' are separated, but have an overlap very
similar to the overlap shown in Figure 2. This comparison method appears just as
accurate as the 'Petal Length' versus 'Petal Width' comparison method.

#### Ratio of Sepal Length/Sepal Width versus Ratio of Petal Length/Petal Width
The division of the Sepal Length by Sepal Width is compared to the division of
Petal Length by Petal Width is shown in Figure 5. Except for a single
entry (Sample 40) 'Iris-setosa' is well defined as a separate entity, but
'Iris-virginica' and 'Iris-versicolor' are mixed together. This comparison is
inconclusive.

#### Ratio of Sepal Length/Sepal Width versus Ratio of Petal Length/Petal Width
The division of the Sepal Length by Petal Length is compared to the division of
Sepal Width by Petal Width is shown in Figure 6. 'Iris-setosa' is well defined as a
separate entity, but 'Iris-virginica' and 'Iris-versicolor' are close with some
overlap. 'Iris-virginica' display is concentrated at the lower left of the plot and
'Iris-versicolor' displayed close, but slightly above and to the right. This comparison
is inconclusive.

#### Ratio of Sepal Length/Petal Width versus Ratio of Sepal Width/Petal Length
The division of the Sepal Length by Petal Width is compared to the division of
Sepal Width by Petal Length is shown in Figure 7. Similar to Figure 6 'Iris-setosa' is
well defined as a separate entity, but 'Iris-virginica' and 'Iris-versicolor' are close
with some overlap. 'Iris-virginica' display is concentrated at the lower left of the plot
and 'Iris-versicolor' displayed close, but slightly above and to the right. This
comparison is inconclusive.

#### Frequency of Sepal Length and Sepal Width
Overlapping histograms of the various frequencies of Sepal Length and Sepal Width are
indicated in Figure 8 and Figure 9. The frequencies of each variant for these parameters
form identifiable zones, but there is some overlap of all three variants. These
comparisons are inconclusive.

#### Frequency of Petal Length and Petal Width
Various frequencies of Petal Length and Petal Width are compared using overlaid histograms 
in Figure 10 and Figure 11. The frequencies of each variant for these parameters
form identifiable zones. 'Iris-setosa' is well defined as a separate entity, with
'Iris-virginica' and 'Iris-versicolor' adjacent to each other with minor overlap. These
comparisons appears to be a good defining factor in separating the three variants.

### Summary of Detailed Data Analysis
The most accurate comparison methods identified for assessing for these three iris variants
('setosa', 'virginica' and 'versicolor') are the 'Petal Length', 'Petal Width', how
'Petal Length' relates to 'Petal Width' and how 'Sepal Width' relates to 'Petal Width' as
shown in Figure 10, Figure 11, Figure 2 and Figure 4 respectively.

'Iris-setosa' is easily separable linearly from the other two with the other two
having some overlap of characteristics.

This overlap between 'Iris-virginica' and 'Iris-versicolor' leads to the conclusion,
of the three variants, these two variants were more than likely, the variants picked from the
same pasture on the same day as identified in the previous study [6]. The overlap in
characteristics between these two variants is probable due to the similar
growing conditions and been measured by the same person with the same instrument.

The known errors in the data set for sample 35 and 38 for the 'Iris-setosa' variant
do not appear to have affected the results of the analysis undertaken. As such, these values
were not corrected during this analysis.

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

![Figure 1](https://github.com/markcot/pands-project/blob/master/Figure_1.jpeg)

![Figure 2](https://github.com/markcot/pands-project/blob/master/Figure_2.jpeg)

![Figure 3](https://github.com/markcot/pands-project/blob/master/Figure_3.jpeg)

![Figure 4](https://github.com/markcot/pands-project/blob/master/Figure_4.jpeg)

![Figure 5](https://github.com/markcot/pands-project/blob/master/Figure_5.jpeg)

![Figure 6](https://github.com/markcot/pands-project/blob/master/Figure_6.jpeg)

![Figure 7](https://github.com/markcot/pands-project/blob/master/Figure_7.jpeg)

![Figure 8](https://github.com/markcot/pands-project/blob/master/Figure_8.jpeg)

![Figure 9](https://github.com/markcot/pands-project/blob/master/Figure_9.jpeg)

![Figure 10](https://github.com/markcot/pands-project/blob/master/Figure_10.jpeg)

![Figure 11](https://github.com/markcot/pands-project/blob/master/Figure_11.jpeg)

![Figure 12](https://github.com/markcot/pands-project/blob/master/Figure_12.jpeg)

![Figure 13](https://github.com/markcot/pands-project/blob/master/Figure_13.jpeg)

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

[N] Code for adding dataframe columns adapted from websites
    https://thispointer.com/python-pandas-how-to-add-new-columns-in-a-dataframe-using-or-dataframe-assign/
    and https://www.interviewqs.com/ddi_code_snippets/add_new_col_df_default_value

[O] Code for plotting scatterplots using matplotlib adapted from
    https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf

[P] Code for plotting Histograms using seaborn adapted from
    http://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/

[Q] Code for removing seaborn warnings verbatim from https://stackoverflow.com/a/54856457

## Git tools reference sources:

[i] Adding Tables and Figure to Git marked down file. Layout adapted from website
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables

[ii] Add image to Git hub Layout adpated from https://stackoverflow.com/a/14494775
