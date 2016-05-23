# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:08:09 2016

@author: ajith
"""

import pandas as pd
import pylab as pl
import seaborn as sbn
import numpy as np
from sklearn import tree
import random
from sklearn import cross_validation

#Data directory
data_path = '/Users/ajith/bigdata/data/'

#Open file
excel_val = pd.read_excel(data_path + 'condom_study.xlsx')

#To keep Q15 as the target remove answers that does not say 4 or 8

excel_val_15 = excel_val[np.logical_or(excel_val['Q15']==4,excel_val['Q15']==8)]

#Remove ids for testing
#test_idx = random.sample(range(76),3)
#
#train_val = excel_val_15.drop(excel_val_15.index[test_idx])
#train_target = train_val['Q15']
#train_data = train_val.ix[:,:4]
#
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(train_data,train_target)
#
#test_val = excel_val_15.iloc[test_idx]
#test_target = test_val['Q15']
#test_data = test_val.ix[:,:4]
#
#scores = cross_validation.cross_val_score(clf, train_data, train_target, cv = 10)
#
#print clf.predict(test_data)
#print test_target
#print scores.mean()
#print scores.std()
X = excel_val_15.ix[:,:4]
y = excel_val_15['Q15']


from sklearn.cross_validation import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size = 0.4)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

scores = cross_validation.cross_val_score(clf, X_train, y_train, cv = 10)

print scores.mean()
print scores.std()