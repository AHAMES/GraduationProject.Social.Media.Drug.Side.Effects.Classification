# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:30:54 2019

@author: Ahmed
"""

import nltk
import string
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

posts= pandas.read_csv('posts.csv')

for i in range(0,len(posts)-1):
    
    stop_words =  set(stopwords.words('english'))

    word_tokens = word_tokenize(posts.iloc[i]['Content']) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
        
        tokens=' '.join(map(str,word_tokens))
        filtered=' '.join(map(str,filtered_sentence)) 
        filtered=filtered.translate(None, string.punctuation)
        posts.at[i , 'Content'] = filtered
posts.to_csv('modifiedPosts.csv')