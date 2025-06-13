
import pandas as pd


#we can read from and online URL
studente_Perfomance_Data = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/students_performance.csv')


#display the firs few rows of the dataset
studente_Perfomance_Data.head()
print(studente_Perfomance_Data.head())

#Numerical Variables: 
# Continuous: 
# Discrete:math score, reading sccore, writing score

#Categorical variables: 
# Ordinal: gender, parent level of education, test preparation 
# Nominal:gender,race/ethnicity




                                                                                                        