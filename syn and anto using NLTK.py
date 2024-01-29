# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:51:48 2023

@author: HP
"""

from nltk.corpus import wordnet
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
print(set(synonyms))
print(set(antonyms))
