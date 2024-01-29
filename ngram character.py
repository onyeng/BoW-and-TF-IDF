# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:58:41 2023

@author: HP
"""

import random

text = """Rain is a natural phenomenon that occurs when water droplets in the atmosphere become heavy enough to fall to the ground. It is an essential part of the water cycle and plays a crucial role in supporting life on Earth."""

n = 5
ngrams ={}

for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
    
#testing
currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    
print(result)