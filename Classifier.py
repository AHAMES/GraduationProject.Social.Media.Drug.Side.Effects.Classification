# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:01:42 2019

@author: Ahmed
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd
'''df = pd.read_excel("MLDataSet.xlsx")
df2 = pd.read_excel("ADRs.xlsx")
df3 = pd.read_excel("DS.xlsx")
df4 = pd.read_excel("Mental.xlsx")

df5=[df, df2,  df3, df4]

result = pd.concat([df,df2,df3, df4], axis=1, join_axes=[df.index])'''

imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

result=pd.read_excel('result.xlsx')

result['Gender']=imp_mean.fit_transform(result['Gender'].values.reshape(-1, 1))
for i in range(len(result)):
    if result.at[i,'ADRCount']==0:
        result.at[i,'ADRCount']=0
    if result.at[i,'ADRCount']>0 and result.at[i,'ADRCount']<=3:
        result.at[i,'ADRCount']=1
    if result.at[i,'ADRCount']>3:
        result.at[i,'ADRCount']=2
    
    if result.at[i,'MentalCount']==0:
        result.at[i,'MentalCount']=0
    if result.at[i,'MentalCount']>0 and result.at[i,'MentalCount']<=3:
        result.at[i,'MentalCount']=1
    if result.at[i,'MentalCount']>3:
        result.at[i,'MentalCount']=2
    
    
    if result.at[i,'DieaseCount']==0:
        result.at[i,'DieaseCount']=0
    if result.at[i,'DieaseCount']>0 and result.at[i,'DieaseCount']<=3:
        result.at[i,'DieaseCount']=1
    if result.at[i,'DieaseCount']>3:
        result.at[i,'DieaseCount']=2
        
    if result.at[i,'Gender']=='Male':
        result.at[i,'Gender']=0
    if result.at[i,'Gender']=='Female':
        result.at[i,'Gender']=1
result['Drug']=LabelEncoder().fit_transform(result['Drug'])
del result['Unnamed: 0']
result['DrugFamily']=LabelEncoder().fit_transform(result['DrugFamily'])
labels=result.iloc[:]['Pain']
del result['Pain']
del result['Content']
del result['Filtered']
del result['Stemmed']
del result['big1']
del result['big2']
del result['small1']
del result['small2']
del result['weights2']
del result['Height']

def getMissingPercentage(feature):
    nancount = int(result[result[feature].isnull()][feature].shape[0])
    size=int(result.shape[0])
    print (nancount)
    print ((nancount*100)/size)
imp_mean = SimpleImputer(missing_values=np.nan, strategy='median')
result['Age']=imp_mean.fit_transform(result['Age'].values.reshape(-1, 1))


kf = KFold(n_splits=10)
kf.get_n_splits(result)
X_train, X_test, Y_train, Y_test = train_test_split(result, labels, test_size=0.3, random_state=0)  


clf= RandomForestClassifier(n_estimators=400)
clf.fit(X_train,Y_train)
pred=clf.predict(X_test)
print ('Importance 1: ' + str((clf.feature_importances_)))
print ('accuracy 1: ' + str(accuracy_score(Y_test,pred)))