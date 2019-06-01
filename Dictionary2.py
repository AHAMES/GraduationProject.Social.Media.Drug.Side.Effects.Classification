# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 01:00:04 2019

@author: Ahmed
"""
import nltk
import string
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer


posts1= pandas.read_excel('askapatientLisinopril.xlsx')
posts2= pandas.read_excel('askapatientAtenolol.xlsx')

def formulate():
    postsTemp = pandas.DataFrame()
    postsTemp = pandas.concat([posts1 ,posts2])
    del postsTemp['duration']
    del postsTemp['date']
    posts = pandas.DataFrame()
    col={}
    for i in postsTemp:
        l=[]
        for j in postsTemp[i]:
            if postsTemp[i].dtype.str=='<f8':
                l.append(j)
            else:
                l.append(j.strip())
        col[i]=l
    df = pd.DataFrame.from_dict(col)
    df.to_excel('askapatient.xlsx', header=True, index=False)
        
    return col,postsTemp

col,posts=formulate()