import nltk
import pandas
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()

from glove import Corpus, Glove
posts= pandas.read_csv('CurrentPosts.csv')

listOfPosts1=posts.iloc[:]['Stemmed']
listOfPosts2=posts.iloc[:]['Filtered']
drugs=posts.iloc[:]['Drug']
familylist=posts.iloc[:]['DrugFamily']

inputPosts=[]
inputPosts2=[]



#for i in range(0,len(listOfPosts2)):
#    inputPosts.append(word_tokenize(listOfPosts2[i]))
for i in range(len(listOfPosts1)):
    listOfPosts1[i]=stemmer.stem(word=drugs[i])+" "+stemmer.stem(word=familylist[i])+" "+listOfPosts1[i]  
    

for i in range(0,len(listOfPosts1)):
    x=word_tokenize(listOfPosts1[i])
    y=""
    j=0
    while(j in range(len(x))):
        if x[j].isdigit() and j!=len(x)-1:
            if x[j+1]=='mg' or x[j+1].isdigit():
                y+=(x[j]+x[j+1]+" ")
                j+=2
            else:
                y+=(x[j]+" ")
                j+=1
        else:
            y+=(x[j]+" ")
            j+=1
    inputPosts.append(y)

for i in range(0,len(inputPosts)):
    x=word_tokenize(inputPosts[i])
    y=[]
    j=0
    while(j in range(len(x))):
        if x[j].isdigit() and j!=len(x)-1:
            if x[j+1]=='mg' or x[j+1].isdigit():
                y.append((x[j]+x[j+1]))
                j+=2
            else:
                y.append((x[j]))
                j+=1
        else:
            y.append((x[j]))
            j+=1
    inputPosts2.append(y) 

#for i in range(0,len(listOfPosts2)):
#    inputPosts3[0]+=(word_tokenize(listOfPosts2[i]))
    
#for i in range(0,len(listOfPosts1)):
#    inputPosts4[0]+=(word_tokenize(listOfPosts1[i]))  
    


'''corpus3 = Corpus() 
corpus3.fit(inputPosts, window=10)
glove3 = Glove(no_components=100, learning_rate=0.05)

glove3.fit(corpus3.matrix, epochs=1000, no_threads=10, verbose=True)
glove3.add_dictionary(corpus3.dictionary)
glove3.save('GPOneList.model')


corpus4 = Corpus() 


corpus4.fit(inputPosts2, window=10)
glove4 = Glove(no_components=100, learning_rate=0.05)

glove4.fit(corpus4.matrix, epochs=1000, no_threads=10, verbose=True)
glove4.add_dictionary(corpus4.dictionary)
glove4.save('GPStemmedOneList.model')

corpus = Corpus() 



corpus.fit(inputPosts, window=10)
glove = Glove(no_components=100, learning_rate=0.05)

glove.fit(corpus.matrix, epochs=1000, no_threads=10, verbose=True)
glove.add_dictionary(corpus.dictionary)
glove.save('GP.model')'''


corpus2 = Corpus() 


corpus2.fit(inputPosts2, window=10)
glove2 = Glove(no_components=100, learning_rate=0.05)

glove2.fit(corpus2.matrix, epochs=1000, no_threads=10, verbose=True)
glove2.add_dictionary(corpus2.dictionary)
glove2.save('GPStemmed.model')

