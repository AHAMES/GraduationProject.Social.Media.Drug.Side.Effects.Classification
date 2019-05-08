# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:41:23 2019

@author: Ahmed
"""

import sys
import codecs
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.manifold import TSNE
 
 
def main():
 
    embeddings_file = 'GP.model'
    wv, vocabulary = load_embeddings(embeddings_file)
 
    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(wv[:1000,:])
 
    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(vocabulary, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.show()
 
 
def load_embeddings(file_name):
 
    with codecs.open(file_name, 'r') as f_in:
        vocabulary, wv = zip(*[line.strip().split(' ', 1) for line in 
f_in])
    wv = np.loadtxt(wv)
    return wv, vocabulary
 
if __name__ == '__main__':
    main()