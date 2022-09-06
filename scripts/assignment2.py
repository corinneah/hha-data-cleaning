import pandas as pd
import datetime as dt
import uuid
import numpy as np

# load in messy data from School Learning Modalities 
df = pd.read_csv('data/School_Learning_Modalities.csv') 

# get count of column and rows
countRows, countColumns = df.shape

df.columns
column_names = list(df)

# list column names
list(df)

# Cleaning the data

# remove all special characters and whitespace ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
list(df)

# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')
list(df)

# get list of column types, make sure strings are strings, numbers are numbers, etc
df.dtypes

# checking for strings 
df_strings = df.select_dtypes(include=['object']).columns

# cleaing each string value 
df['District_Name'] = df['District_Name'].str.replace('[^A-Za-z0-9]+', '_')
df['State'] = df['State'].str.replace('[^A-Za-z0-9]+', '_')
df['City'] = df['City'].str.replace('[^A-Za-z0-9]+', '_')
df['Learning_Modality'] = df['Learning_Modality'].str.replace('[^A-Za-z0-9]+', '_')

# convert data 
df['Week'] = pd.to_datetime(df['Week'])

# droping duplicate rows 
df.drop_duplicates()

# get a count of missing values in each column
df.isnull().sum()

# new data

df['Modality_Inperson'] = pd.np.where(df["Learning_Modality"] == 'In_Person', True, False)
df.head()