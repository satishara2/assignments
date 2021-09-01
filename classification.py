# -*- coding: utf-8 -*-
"""Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15vRcI5hiSNWxAaNP0chITmYEGlA9bg6x
"""

import pandas as pd
import numpy as np
from sklearn import datasets

raw_data = datasets.load_iris()

type(raw_data)

X = raw_data.data

raw_data.feature_names

raw_data.target_names

y = raw_data.target

df = pd.DataFrame(X, columns=raw_data.feature_names)

df

df['Species'] = y

df

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, shuffle=True)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=500)

model.fit(X_train, y_train)

model.predict(X_test)

model.score(X_test, y_test)

from sklearn.metrics import confusion_matrix
predictions = model.predict(X_test)
confusion_matrix(y_test, predictions)

from sklearn.metrics import recall_score
recall_score(y_test, predictions, average='weighted')

from statsmodels.discrete.discrete_model import MNLogit

model = MNLogit(y, X)

fit = model.fit()

fit.summary()

predictions = fit.predict(X_test)

threshold = 0.5

predict_class = np.zeros(predictions.shape)
predict_class[predictions>threshold] = 1
predict_class

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
model.predict(X_test)

model.predict_proba(X_test)

from sklearn.metrics import confusion_matrix
predictions = model.predict(X_test)
confusion_matrix(y_test, predictions)

model.score(X_test, y_test)

from sklearn.metrics import roc_auc_score
predictions = model.predict_proba(X_test)
roc_auc_score(y_test, predictions, multi_class='ovo')

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X_train, y_train)
model.predict(X_test)

# decisiontree
# randomforest
# SVC
# XGBClassifier

# voting classifier
# decisiontree 1 
# randomforest  1
# SVC 0
# XGBClassifier 1

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.ensemble import VotingClassifier


estimators = []

logit_model = LogisticRegression(max_iter=500)
estimators.append(('Logit', logit_model))

nb_model = GaussianNB()
estimators.append(('NB', nb_model))

rf_model = RandomForestClassifier()
estimators.append(('RF', rf_model))

xgb_model = XGBClassifier()
estimators.append(('XGB', xgb_model))

voting_model = VotingClassifier(estimators, voting='soft')
voting_model.fit(X_train, y_train)
voting_model.predict(X_test)

voting_model.score(X_test, y_test)

from sklearn.model_selection import KFold, cross_val_score
kfold = KFold(n_splits=10)

from sklearn.utils import shuffle

X_s, y_s = shuffle(X,y)

cross_val = cross_val_score(voting_model, X_s, y_s, cv=kfold)

cross_val.mean()

from sklearn.model_selection import GridSearchCV

params = {'RF__n_estimators':[20,200], 'XGB__learning_rate':[0.5,1.0]}
search = GridSearchCV(estimator=voting_model, param_grid=params, cv=5)
search.fit(X_train, y_train)
search.predict(X_test)

search.best_params_

search.best_estimator_

search.best_score_

search.score(X_test, y_test)

import pickle

model_pkl_file = 'Voting_model.pkl'

file = open(model_pkl_file, 'wb')

pickle.dump(voting_model, file)

file.close()

model_pkl_file = 'Voting_model.pkl'
file = open(model_pkl_file, 'rb')
model = pickle.load(file)

model.predict(X_test)
