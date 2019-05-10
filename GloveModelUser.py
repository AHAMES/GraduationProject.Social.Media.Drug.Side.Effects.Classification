# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:29:50 2019

@author: Ahmed
"""



from glove import Corpus, Glove
import pandas

glov=Glove.load('GP.model')
glov2=Glove.load('GPStemmed.model')
ADRs=pandas.read_csv('ADR_TFIDF3.csv').columns.tolist()
diseases=pandas.read_csv('disease_TFIDF3.csv').columns.tolist()
mental=pandas.read_csv('mental_TFIDF3.csv').columns.tolist()
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
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
            
            f.write(k+'\n')
            for j in glov2.word_vectors[glov2.dictionary[k]]:
    
                w.write(str(j)+'\t')
            w.write('\n')
    f.close()
    w.close()
printOutVectors('DrugLimited',1,0,1)