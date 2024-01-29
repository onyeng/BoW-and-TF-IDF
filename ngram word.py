# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:11:46 2023

@author: HP
"""

import random
import nltk

text = """Rain is a natural phenomenon that occurs when water droplets in the atmosphere become heavy enough to fall to the ground. It is an essential part of the water cycle and plays a crucial role in supporting life on Earth."""

n = 3
ngrams ={}

words = nltk.word_tokenize(text)
for i in range(len(text)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
    

currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
print(result)