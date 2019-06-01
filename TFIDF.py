# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:38:37 2019

@author: Ahmed
"""
from sklearn.feature_extraction.text import TfidfVectorizer


import nltk
import string
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer




#respone=vectorizer.fit_transform()
posts= pandas.read_excel('askapatient.xlsx')
vectorizer = TfidfVectorizer()
vectorizer2 = TfidfVectorizer()
listOfPosts=posts.iloc[:]['Filtered']
listOfPosts2=posts.iloc[:]['Stemmed']
TFIDF=vectorizer.fit_transform(listOfPosts)
TFIDF2=vectorizer2.fit_transform(listOfPosts2)

print (vectorizer.get_feature_names())

file_object  = open("TFIDF.txt", "w")
file_object2  = open("TFIDF2.txt", "w")
s=vectorizer.get_feature_names()


for i in s:
    file_object.write(i+'\n')
file_object.close()
s2=vectorizer2.get_feature_names()
for i in s2:
    file_object2.write(i+'\n')
file_object2.close()
