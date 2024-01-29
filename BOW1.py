# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:04:24 2023

@author: HP
"""

import nltk
import re
import heapq
import numpy as np

paragraph = """Rain is a natural phenomenon that occurs when water droplets in the atmosphere become heavy enough to fall to the ground. 
            It is an essential part of the water cycle and plays a crucial role in supporting life on Earth. 
            Rain is important for agriculture, as it helps to water crops and replenish water sources. 
            It also plays a vital role in maintaining the balance of the ecosystem by providing water for plants, animals, and humans. 
            Rain comes in many different forms, from light drizzles to heavy downpours, and can be accompanied by thunder and lightning. 
            While it can sometimes be a source of inconvenience, such as during floods or storms, rain is ultimately a precious resource that we rely on for our survival."""


dataset = nltk.sent_tokenize(paragraph)

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W',' ',dataset[i])
    dataset[i] = re.sub(r'\s+',' ',dataset[i])
    
#Histogram
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
            
freq_words = heapq.nlargest(100,word2count,key=word2count.get)

#IDF matrix
word_idfs = {}

for word in freq_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count +=1
    word_idfs[word] = np.log((len(dataset)/doc_count)+1)


# TF matrix
tf_matrix = {}
for word in freq_words:
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if w == word:
                frequency += 1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
        tf_matrix[word] = doc_tf
        
        
        
# TF-idf calculation
tfidf_matrix = []
for word in tf_matrix.keys():
    tfidf = []
    for value in tf_matrix[word]:
        score = value * word_idfs[word]
        tfidf.append(score)
    tfidf_matrix.append(tfidf)
    
X = np.asarray(tfidf_matrix)

X = np.trasnpose(X)


X = []

for data in dataset:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)
    
X = np.asarray(X)


