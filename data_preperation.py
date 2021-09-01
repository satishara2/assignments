# -*- coding: utf-8 -*-
"""Data Preperation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18UPQwCJkvZQCB3nOvkKKPogwe_5pt5AX
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Hemanthkaruturi/python_for_datascience/master/data/Financial%20Sample.csv')

df.head()

df.columns

#df[' Profit ']

s = ' test '

s.strip()

def strip_space(s):
  return s.strip()

l = ['One', ' Two ']

list(map(strip_space, l))

l1 = []
for i in l:
  l1.append(strip_space(i))

l1

df.columns = list(map(strip_space, df.columns ))

df.columns[0] = 'Segments'

type(df.columns)

df.columns

l = list(df.columns)

l[0] = 'Segments'

l

# df.columns = l

# best way
df.rename(columns={'Segment':'Segments'}, inplace=True)

df.head()

df.describe()

df.info()

df.shape

df.shape[0]

df.shape[1]

df.ndim

df.tail()

df['Manufacturing Price'].head()

df['Manufacturing Price'].unique()

s = '$3'
s.replace('$','')

df['Manufacturing Price'] = df['Manufacturing Price'].str.replace('$','')

df['Manufacturing Price'].unique()

df['Manufacturing Price'] = df['Manufacturing Price'].str.strip()

df['Manufacturing Price'].unique()

df['Manufacturing Price'] = df['Manufacturing Price'].astype('float')

df.dtypes

columns = ['Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']

def remove_characters(column, rm_character):

  df[column] = df[column].str.replace(rm_character,'')

  return df[column]

for column in columns:
  df[column] = remove_characters(column, '$')
  df[column] = remove_characters(column, ',')
  df[column] = remove_characters(column, '(')
  df[column] = remove_characters(column, ')')

df.head()

df['Sale Price'].unique()

df['Sale Price']  = df['Sale Price'].astype('float')

df['Discounts'].unique()

df['Discounts'].str.replace('-','0')

df.dtypes

df.head()

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df['Date'].dt.month

df['Date'].dt.month_name()

df['Date'].dt.year

df['Date'].dt.dayofweek

df['Date'].dt.day_name()

df.head()

df['Segments'].unique()

df['Segments'].value_counts()

segment_dict = {'Government':1, 'Midmarket':2, 'Channel Partners':3, 'Enterprise':4, 'Small Business':5}

df.columns

pd.crosstab(df['Segment'], df['Country'])

df['Segments'].map(segment_dict)

def multiply(x):
  return x*x

df['Manufacturing Price'].apply(multiply)

df['Profit'].unique()

def str_strip(s):
  return s.strip()

df['Profit'].apply(str_strip)



df['Country'].unique()

df['Country'] = df['Country'].astype('category')

df['Country'].cat.codes

# groupby
# joins
# sqldf
# drop duplicates
# melt
# pivot tables

"""## Groupby"""

df.dtypes

df[['Segment','Units Sold']]

df[['Segment','Units Sold']].groupby('Segment').sum()

df[['Segment','Units Sold']].groupby('Segment').mean()

df[['Segment','Country','Units Sold']]

df[['Segment','Country','Units Sold']].groupby(['Segment','Country']).sum()

segment_units = df[['Segment','Units Sold']].groupby('Segment').mean()

segment_units

segment_units.columns

segment_units.index

segment_units = segment_units.reset_index()

segment_units.columns

segment_units['Segment']

df_group = df[['Segment','Country','Units Sold']].groupby(['Segment','Country']).sum()

df_group.index

df_group = df_group.reset_index()

df_group.head()

"""## Joins"""

Emp_details = {'ID':[1,2,3,4,5,6], 'Name':['Raju', 'Ravi', 'Raghav', 'Ramu', 'Lavanya', 'Ramesh']}
Emp_salary = {'ID':[1,2,3,4,5], 'Salary':[123,545,245,234,234]}

Emp_details_df = pd.DataFrame(Emp_details)
Emp_salary_df = pd.DataFrame(Emp_salary)

Emp_details_df

pd.merge(Emp_details_df, Emp_salary_df, how='left')

pd.merge(Emp_details_df, Emp_salary_df, left_on='ID',right_on='ID' ,how='left')

pd.merge(Emp_details_df, Emp_salary_df, left_on='ID',right_on='ID' ,how='inner')

!pip install pandasql

from pandasql import sqldf

whos

query = 'select * from df limit 4'

sqldf(query)

sqldf('select * from Emp_salary_df')

sqldf('select * from df where Segment = "Government"')

sqldf('select * from Emp_details_df as a left join Emp_salary_df as b on a.ID = b.ID')

df.drop_duplicates()

df.drop_duplicates(subset=['Segment', 'Country', 'Place'])

df[df.duplicated()]

df.T

df.transpose()

# melt
# pivot table (dcast)

pew = pd.read_csv('https://raw.githubusercontent.com/Hemanthkaruturi/python_for_datascience/master/data/pew.csv')

pew

pew.melt(id_vars='religion', var_name='Income', value_name='Count')

weather = pd.read_csv('weather.csv')

weather.head()

columns = range(1,32)
for column in columns:
  weather[str(column)] = weather[str(column)].str.replace('.','0')
  weather[str(column)] = weather[str(column)].str.strip()
  weather[str(column)] = weather[str(column)].astype(int)

weather.dtypes

weather_melt = weather.melt(id_vars=['Year',	'Month',	'Element'], var_name='day', value_name='temperature')

weather_melt

# Year Month Day tmin tmax

weather_pivot = pd.pivot_table(data=weather_melt, values='temperature', index=['Year', 'Month', 'day'], columns='Element')

weather_pivot.columns

weather_pivot.index

df = weather_pivot.reset_index()

df.columns

df

# statists
# supervised
## regression
## classification
# unsupervised
## clustering
# boosting algorithms

