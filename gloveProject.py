import nltk
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

print (5)
from glove import Corpus, Glove
posts= pandas.read_csv('CurrentPosts.csv')

listOfPosts1=posts.iloc[:]['Stemmed']
listOfPosts2=posts.iloc[:]['Filtered']
inputPosts=[]
for i in range(0,len(listOfPosts2)):
    inputPosts.append(word_tokenize(listOfPosts2[i]))
    
corpus = Corpus() 
corpus.fit(inputPosts, window=10)
glove = Glove(no_components=5, learning_rate=0.05)

glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)
glove.save('GP.model')
