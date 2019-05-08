# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:29:50 2019

@author: Ahmed
"""



from glove import Corpus, Glove


glov=Glove.load('GP.model')
glov2=Glove.load('GPStemmed.model')
#glov3=Glove.load('GPOneList.model')
#glov4=Glove.load('GPStemmedOneList.model')

def printMostSimilar(word,numbers):
    c1=glov.most_similar(word, number=numbers)
    c2=glov2.most_similar(word, number=numbers)
    
    c3=glov.most_similar(word, number=numbers)
    c4=glov2.most_similar(word, number=numbers)
    print ('C1')
    for i in c1:print (i)
    
    print ('C2')
    for i in c2:print (i)
    
    '''print ('C3')
    for i in c3:print (i)
    
    print ('C4')
    for i in c4:print (i)'''
def printOutVectors():
    f= open("GPLabels.txt","w+")
    w=open("GP.txt","w+")
    for i in glov.dictionary:
        f.write(i+'\n')
        for j in glov.word_vectors[glov.dictionary[i]]:

            w.write(str(j)+'\t')
        w.write('\n')
    f.close()
    w.close()
        