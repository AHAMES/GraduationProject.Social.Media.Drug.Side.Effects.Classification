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
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
vectorizer = CountVectorizer()

posts= pandas.read_csv('posts.csv')


for i in range(0,len(posts)-1):
    
    stop_words =  set(stopwords.words('english'))
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
        w=w.replace('!'," ")
        w=w.replace(';'," ")
        w=w.replace("’"," ") 
        w=w.replace("'"," ")
        w=w.replace('?'," ")
        if w not in stop_words: 
            filtered_sentence.append(str(stemmer.stem(w))) 
        
        tokens=' '.join(map(str,word_tokens))
        filtered=' '.join(map(str,filtered_sentence)) 
        filtered=filtered.translate(None, string.punctuation)
        posts.at[i , 'Filtered'] = filtered

listOfPosts=posts.iloc[:]['Content']
bagOfWords = vectorizer.fit(listOfPosts.tolist())
bagOfWords = vectorizer.transform(listOfPosts.tolist())
print bagOfWords

posts.to_csv('modifiedPosts.csv')