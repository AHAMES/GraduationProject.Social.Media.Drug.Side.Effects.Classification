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
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
vectorizer = CountVectorizer()

posts= pandas.read_csv('CurrentPosts.csv')


stop_words =  set(stopwords.words('english'))
for i in range(0,len(posts)):
    
    newSentence =""
    sentence=posts.iloc[i]['Content']
    for k in sentence:
        if k.isalpha() or k.isdigit() or k==' ':
            newSentence=newSentence+k
            continue
        else:
            newSentence=newSentence+" " 
            continue
    
    word_tokens = word_tokenize(newSentence) 
    filtered_sentence = [] 
    stemmed_sentence=[]
    for w in word_tokens: 
      
        if w not in stop_words: 
            filtered_sentence.append(w) 
            stemmed_sentence.append(stemmer.stem(w))
        tokens=' '.join(map(str,word_tokens))
        filtered=' '.join(map(str,filtered_sentence)) 
        filtered=filtered.translate(None, string.punctuation)
        stemmed=' '.join(map(str,stemmed_sentence)) 
        stemmed=stemmed.translate(None, string.punctuation)
        posts.at[i ,'Filtered'] = filtered
        posts.at[i,'Stemmed'] = stemmed
listOfPosts=posts.iloc[:]['Content']
bagOfWords = vectorizer.fit(listOfPosts.tolist())
bagOfWords = vectorizer.transform(listOfPosts.tolist())
#print bagOfWords

posts.to_csv('CurrentPosts.csv')