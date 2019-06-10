# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:29:50 2019

@author: Ahmed
"""



from glove import Corpus, Glove
import pandas
import numpy as np
import nltk
glov=Glove.load('GP.model')
glov2=Glove.load('MedHelpStemmed.model')
ADRs=pandas.read_csv('ADR_TFIDF3.csv').columns.tolist()
diseases=pandas.read_csv('disease_TFIDF3.csv').columns.tolist()
mental=pandas.read_csv('mental_TFIDF3.csv').columns.tolist()
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
vectorizer = CountVectorizer()
from nltk.stem import PorterStemmer
import json
greeting_words = json.loads(open('greetings.txt', 'r').read())
posts= pandas.read_csv('CurrentPosts.csv')
listOfPosts1=posts.iloc[:]['Stemmed']
drugs=posts.iloc[:]['Drug']
familylist=posts.iloc[:]['DrugFamily']
stemmer=PorterStemmer()
for i in range(len(listOfPosts1)):
    listOfPosts1[i]=stemmer.stem(word=drugs[i])+" "+stemmer.stem(word=familylist[i])+" "+listOfPosts1[i]  
cnt = Counter()

for i in listOfPosts1.tolist():
    for word in i.split(' '):
        cnt[word] += 1
transformed_data = vectorizer.fit_transform(listOfPosts1)
print(transformed_data.toarray().sum(axis=0))
#print (transformed_data[vectorizer.vocabulary_['amlodipin']])
print (zip(vectorizer.get_feature_names(), np.ravel(transformed_data.sum(axis=0))))

del ADRs[0]
del diseases[0]
del mental[0]

drugList=["Nadolol","Amlodipine","Diltiazem","Hydrochlorothiazide","Atenolol","Lisinopril",]
DrugList=[]
for i in drugList: DrugList.append(stemmer.stem(i))
#glov3=Glove.load('GPOneList.model')
#glov4=Glove.load('GPStemmedOneList.model')

def printMostSimilar(word,numbers):
    if word in glov.dictionary:
        c1=glov.most_similar(word, number=numbers)
    
        print ('C1')
        for i in c1:print (i)
    
    if word in glov2.dictionary:
        c2=glov2.most_similar(word, number=numbers)
        print ('C2')
        for i in c2:print (i)
    
    '''print ('C3')
    for i in c3:print (i)
    
    print ('C4')
    for i in c4:print (i)'''

def printOutVectors(filename,adr,ds,men):
    f= open(filename+"Labels.txt","w+")
    w=open(filename+".txt","w+")
    
    for i in glov2.dictionary:
        k = i
        if (adr and (k in ADRs)) or (ds and (k in diseases)) or (mental and (k in mental)) or (k in DrugList) or (adr and ds and men):
        #if cnt[i]>=40 and stemmer.stem(i) not in greeting_words :    
            f.write(k+'\n')
            for j in glov2.word_vectors[glov2.dictionary[k]]:
        
                w.write(str(j)+'\t')
            w.write('\n')
    f.close()
    w.close()
printOutVectors('MedLimitedmodel',1,0,1)