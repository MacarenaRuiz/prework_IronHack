
import pandas as pd

#to read from github
#url: https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/students_performance.csv
students_performance_data = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/students_performance.csv')
print(students_performance_data.head())


# to read from path in local
students_performance_data = pd.read_csv(r"C:\Users\macar\Desktop\Formación\IRONHACK\Data_PreWork_M2\students_performance.csv")
print(students_performance_data)
students_performance_data.head()
#print (vari) --> terminal
#vari.head() --> visualiza en interactive window

#Number of rows and columns
num_rows=len(students_performance_data)
print("Number of rows: ", num_rows)

num_cols=len(students_performance_data.columns)
print("Number of columns: ", num_cols)



#Number of unique values for each column (gender, race/ethinicity, parental level, level of education, lunch, test)
unique_values_gender = students_performance_data['gender'].unique()
print('Unique values in gender, are: ' ,unique_values_gender)

unique_values_race = students_performance_data['race/ethnicity'].unique()
print('Unique values in race, are: ', unique_values_race)

#to print all values of each column of the data frame
for column in students_performance_data.columns:
    unique_vals= students_performance_data[column].unique()
    print(f"\nunique values in column' {column}': ")
    print(unique_vals)


#NOT CLEAR ???
    if len(unique_vals) < 10:
        print(f"\nShow me those ones: ' {unique_vals}': ")
    else:
        print('Are more than 10 values')





#Calculate mean, median, mode, standard deviation and range for numerical variables
#math score, reading score and writing score
print('The mean for math score is: ', students_performance_data['math score'].mean())
print('The mean for reading score is: ', students_performance_data['reading score'].mean())
print('The mean for writing score is: ', students_performance_data['writing score'].mean())

#MEAN
students_performance_data_mean=students_performance_data[['math score', 'reading score', 'writing score']].mean()
print('The mean for these 3 columns, are: ', students_performance_data_mean)

#MEDIAN
students_performance_data_median= students_performance_data[['math score', 'reading score', 'writing score']].median()
print('The median for these 3 columns, are: ', students_performance_data_median)

#MODE
students_performance_mode = students_performance_data[['math score', 'reading score', 'writing score']].mode()
print('The mode of these 3 columns, are: ', students_performance_mode)

#STANDARD DEVIATION
students_performance_sd = students_performance_data[['math score', 'reading score', 'writing score']].std()
print('The standard deviation of these 3 columns, are: ',students_performance_sd)
#RANGE
range_values_max= students_performance_data[['math score', 'reading score', 'writing score']].max()    
range_values_min= students_performance_data[['math score', 'reading score', 'writing score']].min()

range_values_total=(range_values_max-range_values_min)
print('The range values, are: ',range_values_total)

# for numerical variables and frecuency counts for categorical variables
#frequency counts 

students_performance_data_counts = students_performance_data[['gender', 'race/ethnicity','parental level of education','lunch','test preparation course']].value_counts()
print('The counts for categorical valuables: ', students_performance_data_counts)
