# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:36:11 2020

@author: psuda
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pydataset import data
data('iris')
data('mtcars')

import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package= 'datasets')
mtcars.data.head()

import os
data = mtcars.data
data.shape
data.describe
data.columns
data['am'].value_counts()
X= data[['mpg','wt']]
X
Y= data['am']
Y.value_counts()
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20)
X_train.shape
X_test.shape
7/data.shape[0]
from sklearn.tree import DecisionTreeClassifier
clsModel = DecisionTreeClassifier()  #model with parameter
clsModel.fit(X_train, Y_train)
ypred1 = clsModel.predict(X_test)
len(ypred1)
X_test.head()
X_test
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
classification_report(y_true=Y_test, y_pred= ypred1)
confusion_matrix(y_true=Y_test, y_pred=ypred1)
accuracy_score(y_true=Y_test, y_pred=ypred1)

newData = X.sample(4)
X
newData
clsModel.predict(newData)


X2= data[['mpg','wt','hp']]
X2
Y2= data['am']
Y2.value_counts()

from sklearn.model_selection import train_test_split
X2_train, X2_test, Y2_train, Y2_test = train_test_split(X2, Y2, test_size=.20, random_state=123 )
X2_train.shape
X2_test.shape
10/data2.shape[0]
from sklearn.tree import DecisionTreeRegressor #note this
regrModel = DecisionTreeRegressor()  #model with parameter
regrModel.fit(X2_train, Y2_train)
ypred2 = regrModel.predict(X2_test)
ypred2
len(ypred2)
df2 = pd.DataFrame({'Actual':Y2_test, 'Predicted': ypred2, 'diff':Y2_test-ypred2})
df2
df2.shape[0]