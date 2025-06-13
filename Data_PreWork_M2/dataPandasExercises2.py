
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#url: https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/students_performance.csv
students_performance_data = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/students_performance.csv')
print(students_performance_data.head())

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


#histograms
#create histograms for numerical variables
numerical_variables=['math score','reading score','writing score']
for col in numerical_variables:
    sns.histplot(x=col, data=students_performance_data)
    plt.show()

#create bar plots for categorical variables
categorical_variables = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
for col in categorical_variables:
    sns.histplot(x=col, data=df)
    plt.show()