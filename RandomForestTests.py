# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 15:17:39 2019

@author: Ahmed
"""

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_classification

#X, Y = make_blobs(n_samples=1000, n_features=10)
X, Y = make_classification(n_samples=1000, n_features=10)
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)
sel = SelectFromModel(RandomForestClassifier(n_estimators = 100))
sel.fit(X_train, Y_train)
clf= RandomForestClassifier(n_estimators=400)

clf.fit(X_train,Y_train)
pred=clf.predict(X_test)
print 'Importance 1: ' + str((clf.feature_importances_))
print 'accuracy 1: ' + str(accuracy_score(Y_test,pred))

print sel.get_support(True)
selected_feat= np.array(X_train)
selected_feat=selected_feat[:,(sel.get_support(True))]
selected_feat_Test= np.array(X_test)
selected_feat_Test=selected_feat_Test[:,(sel.get_support(True))]
len(selected_feat)

cl= RandomForestClassifier(n_estimators=400)

cl.fit(selected_feat,Y_train)
pred2=cl.predict(selected_feat_Test)
print 'Importance 2: ' + str((cl.feature_importances_))
print 'accuracy 2: ' + str(accuracy_score(Y_test,pred2))