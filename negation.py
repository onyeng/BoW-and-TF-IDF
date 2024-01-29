# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:58:10 2023

@author: HP
"""

import nltk
from nltk.corpus import wordnet

sentence = "i am not agree "

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""

for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""
    if word != "not":
        new_words.append(word)
        
sentence = ' '.join(new_words)
