# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:02:08 2019

@author: Ahmed
"""


f = open("TFIDFOutput.txt", "r")
import collections
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ADR_Dictionary={}
Disease_Dictionary={}
Mental_Dictionary={}
stemmer = PorterStemmer()
for line in f:
    if "[Sign or Symptom]" in line:
        word_tokens = word_tokenize(line)
        #print word_tokens
        i=3
        ADR=''
        if word_tokens[2]!='(':
            ADR=word_tokens[1].capitalize()
        else:    
            while word_tokens[i]!=')':
                ADR+=word_tokens[i]+" "
                i+=1
        if(stemmer.stem(word_tokens[1]) not in ADR_Dictionary):
            ADR_Dictionary[stemmer.stem(word_tokens[1])]=[ADR]
        else:
            if ADR in ADR_Dictionary[stemmer.stem(word_tokens[1])]:
                continue
            else:
                ADR_Dictionary[stemmer.stem(word_tokens[1])].append(ADR)
                
                
    if "[Disease or Syndrome]" in line:
        word_tokens = word_tokenize(line)
        #print word_tokens
        i=3
        ADR=''
        if word_tokens[2]!='(':
            ADR=word_tokens[1].capitalize()
        else:    
            while word_tokens[i]!=')':
                ADR+=word_tokens[i]+" "
                i+=1
        if(stemmer.stem(word_tokens[1]) not in Disease_Dictionary):
                Disease_Dictionary[stemmer.stem(word_tokens[1])]=[ADR]
        else:
            if ADR in Disease_Dictionary[stemmer.stem(word_tokens[1])]:
                continue
            else:
                Disease_Dictionary[stemmer.stem(word_tokens[1])].append(ADR)
                
    if "[Mental or Behavioral Dysfunction]" in line:  
        word_tokens = word_tokenize(line)
        #print word_tokens
        i=3
        ADR=''
        if word_tokens[2]!='(':
            ADR=word_tokens[1].capitalize()
        else:    
            while word_tokens[i]!=')':
                ADR+=word_tokens[i]+" "
                i+=1
        if(stemmer.stem(word_tokens[1]) not in Mental_Dictionary):
            Mental_Dictionary[stemmer.stem(word_tokens[1])]=[ADR]
        else:
            if ADR in Mental_Dictionary[stemmer.stem(word_tokens[1])]:
                continue
            else:
                Mental_Dictionary[stemmer.stem(word_tokens[1])].append(ADR)         
    
f.close()

w = open("ADR_Dictionary.txt",'w')
j=0
for i in sorted(ADR_Dictionary.iterkeys()):
    w.write('\''+str(i)+'\''+":"+str(ADR_Dictionary[i])+"\n")
    j+=1
print j
w.close()    
    
w = open("Disease_Dictionary.txt",'w')
j=0
for i in sorted(Disease_Dictionary.iterkeys()):
    w.write('\''+str(i)+'\''+":"+str(Disease_Dictionary[i])+"\n")
    j+=1
print j
w.close()     

w = open("Mental_Dictionary.txt",'w')
j=0
for i in sorted(Mental_Dictionary.iterkeys()):
    w.write('\''+str(i)+'\''+":"+str(Mental_Dictionary[i])+"\n")
    j+=1
print j
w.close() 