# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:47:09 2019

@author: Ahmed
"""

import nltk
import string
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
vectorizer = CountVectorizer()

posts= pandas.read_csv('Hypertension.csv')
phraseList=[]
stop_words =  set(stopwords.words('english'))
for i in range(0,len(posts)-1):
   
    newSentence =""
    sentence=posts.iloc[i]['Content']
    for k in sentence:
        if k.isalpha() or k.isdigit() or k==' ':
            newSentence=newSentence+k
            continue
        else:
            continue
    word_tokens = word_tokenize(newSentence) 
    
    
    filtered_sentence = [] 
    
    
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    phraseList.append(filtered_sentence)
    
while True:
    index=int(input("Index: "))
    transformed_data = vectorizer.fit_transform(phraseList[index])
    print ' '.join(phraseList[index])
    print '******************************'
    print zip(vectorizer.get_feature_names(), np.ravel(transformed_data.sum(axis=0)))