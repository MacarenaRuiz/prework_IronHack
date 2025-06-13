
import pandas as pd

df=pd.read_csv('filename.csv')

#we can read from and online URL
titanic_data = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/prework_data/main/titanic.csv')

#display the firs few rows of the dataset
titanic_data.head()

