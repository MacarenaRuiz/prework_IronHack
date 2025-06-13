
import pandas as pd
import statistics
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import jupytext



# Task 1
# 1.1
#I have tried manually 4 times with the 5 options
lst=[95,87,85,85,90,89,90,88,96]

med_median= statistics.median(lst)
print('The median is: ', med_median)

# (88,96)

#1.2
mathquizzes=[88,100,72,91,89]
mathquizzes_mean= statistics.mean(mathquizzes)
print('The mean is: ', mathquizzes_mean)
#Mean is 88, after 6 quizzes is 89

#score Sams 6 quiz= 82

mathquizzes2=[88,100,72,91,89,82]
mathquizzes2_mean = statistics.mean(mathquizzes2)
print('The mean is, after the 6th exam: ', mathquizzes2_mean)

#1.2.1 TRUE
#1.2.2 TRUE
#1.2.3 FALSE
#1.2.4 TRUE
#OPTION A

#1.3 
store1=[1,1.5,2,1,0.5]
store2=[2,2.5,4,4,1]
store3=[10,3,2,4,2]

#VARIANCE
var1=statistics.variance(store1)
print('The variance for the store1:' , var1)

var2=statistics.variance(store2)
print('The variance for the store2:' , var2)

var3=statistics.variance(store3)
print('The variance for the store2:' , var3)

#MEAN
averageStore1 = statistics.mean(store1)
print('The mean in store1: ',averageStore1)

averageStore2 = statistics.mean(store2)
print('The mean in store2, is: ', averageStore2)

averageStore3 = statistics.mean(store3)
print('The mean in store 3, is: ', averageStore3)

#MEDIAN
medStore1= statistics.median(store1)
print('The median in store1: ', medStore1)

medStore2=statistics.median(store2)
print('The median in store 2: ', medStore2)

medStore3 = statistics.median(store3)
print('The median in store 3 is: ', medStore3)

#1.4 -4.A
#1.5 Histogram
#1.6 Frequency count
#1.7 green 
#1.8 mean


#Task 2
#2.1 Imposible to answer, 2.2 Warner bros, 2.3 Universal, 2.4 Warner Bros, 2.5 Paramount

#Task 3
#3.1- 3 , 3.2 - 116, 3.3 - 11, 3.4 - 2005, 2.5 - 4

#Task 4
#4.1 - 4:5, 4.2 - 75,55%, 4.3- 82,5%, 4.4- 80%,  4.5 - 560
