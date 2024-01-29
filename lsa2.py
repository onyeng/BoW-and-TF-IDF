# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:36:31 2023

@author: HP
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

dataset = ["The sun rose over the horizon, casting a warm glow over the countryside",
           "She walked through the forest, listening to the rustling leaves and chirping birds",
           "The waves crashed against the shore, creating a soothing melody",
           "The city streets were bustling with people and the sound of honking horns",
           "The scent of freshly baked bread wafted through the air, making her mouth water",
           "The snow-covered mountains sparkled in the sunlight, a breathtaking sight",
           "The baby giggled as she played with her toys, filling the room with joy"]

dataset = [line.lower() for line in dataset]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

print(X[0])

lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)

rowl = lsa.components_[0]
concept_words = {}

terms = vectorizer.get_feature_names_out()
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    concept_words["Concept "+str(i)] = sortedTerms

for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)