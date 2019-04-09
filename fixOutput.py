# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:31:11 2019

@author: Ahmed
"""
def fixOutput(fil):
    
    f= open(fil+'.txt','r')
    w = open(fil+"2.txt",'w')
    j=0
    for i in f:
        x=i
        m=x[0:-1]+','
        w.write(m+'\n')
        j+=1
    print j
    w.close()  
fixOutput('Disease_Dictionary')