# -*- coding: utf-8 -*-
"""Pandas dataframes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GBIlcqXVmiPV3XBx2D8aF8oM-KvUAKAR
"""

import pandas as pd

weather = pd.read_csv('https://raw.githubusercontent.com/Hemanthkaruturi/python_for_datascience/master/data/weather.csv', low_memory=False)

weather.head()

RFM = pd.read_excel('https://github.com/Hemanthkaruturi/python_for_datascience/blob/master/data/RFM%20part2.xlsx?raw=true')

RFM.head()

RFM = RFM.iloc[:,:3]

RFM.head()

"""#### Handling missing values"""

RFM.isnull().sum()

import pandas as pd
adv = pd.read_csv('https://raw.githubusercontent.com/Hemanthkaruturi/python_for_datascience/master/data/Advertising_Missing.csv')

adv.head()

adv.isnull().sum()

adv = adv.drop(columns=['Unnamed: 0'])

adv[adv['TV'].isnull()]

adv[adv['TV'].isnull() == False]

adv_no_missing = adv.loc[adv['TV'].isnull() == False,:]

adv_no_missing.isnull().sum()

adv_no_nulls = adv.dropna()

adv_no_nulls.isnull().sum()

adv[adv['TV'].isnull()]

adv.loc[adv['TV'].isnull(), 'TV']

import numpy as np

adv.loc[adv['TV'].isnull(), 'TV'] = np.mean(adv['TV'])

adv.isnull().sum()

# from sklearn.preprocessing.impute from SimpleImputer
from sklearn.impute import SimpleImputer

impute = SimpleImputer(strategy='mean')
adv_simple = impute.fit_transform(adv)

adv_simple

type(adv_simple)

adv_simple = pd.DataFrame(adv_simple, columns=adv.columns)

adv_simple.isnull().sum()

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

np.nan

impute = IterativeImputer(max_iter=10)

adv_iim = impute.fit_transform(adv)

adv_iim = pd.DataFrame(adv_iim, columns=adv.columns)

from sklearn.impute import KNNImputer
impute = KNNImputer(n_neighbors=2)
impute.fit_transform(adv)

"""#### Outlier Detection"""

boston = pd.read_csv('https://raw.githubusercontent.com/Hemanthkaruturi/python_for_datascience/master/data/Boston_housing_train.csv')

boston.head()

boston['age'].skew(axis=0)

boston.skew(axis=0)

Q1 = boston['crim'].quantile(0.25)

Q3 = boston['crim'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5*IQR

upper_limit = Q3 + 1.5*IQR

lower_limit

upper_limit

data_iqr = boston.copy()

data_iqr['crim'] = data_iqr['crim'][data_iqr['crim'] > lower_limit]

data_iqr['crim'] = data_iqr['crim'][data_iqr['crim'] < upper_limit]

data_iqr['crim'].skew(axis=0)

"""#### Zscore"""

data_zscore = boston.copy()

import numpy as np
from scipy.stats import zscore
np.abs(zscore(data_zscore['crim'])) > 3

data_zscore['crim'] = data_zscore['crim'][np.abs(zscore(data_zscore['crim'])) < 3]

data_zscore['crim'].skew(axis=0)

from sklearn.covariance import EllipticEnvelope
outs = EllipticEnvelope(contamination=0.2)
output = outs.fit_predict(boston)

output != -1

data_elliptic = boston[output != -1]

data_elliptic.skew(axis=0)

from sklearn.ensemble import IsolationForest
outs = IsolationForest(contamination=0.5)
output = outs.fit_predict(boston)

data_isf = boston[output != -1]

data_isf.skew(axis=0)

"""### Normalization"""

from sklearn.preprocessing import normalize
data_normalize = normalize(boston)

from sklearn.preprocessing import scale
scale(boston)

from sklearn.preprocessing import MaxAbsScaler
MaxAbsScaler(boston)

# MinMaxScaler
# StandardScaler

from sklearn.preprocessing import QuantileTransformer
Q_transform = QuantileTransformer()
Q_transform.fit_transform(boston)

np.log(boston['crim'])

"""#### Visualization"""

import matplotlib.pyplot as plt
plt.boxplot(boston['crim'])
plt.show()

plt.plot(boston['ID'], boston['age'])

simple_data = pd.DataFrame({'Cricketer':['Rohit', 'Dhoni', 'Dhawan'], 'Score':[45,45,23]})

simple_data

plt.bar(x=simple_data['Cricketer'], height=simple_data['Score'])

plt.scatter(x=boston['ID'], y=boston['crim'])

plt.hist(boston['crim'])
plt.title("crim")
plt.show()

plt.figure(figsize=(10,10))
plt.hist(boston['crim'])
plt.title("crim")
plt.show()

# seaborn