# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:47:14 2023

@author: HP
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

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

terms = vectorizer.get_feature_names_out()
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    print("\nConcept",i,":")
    for term in sortedTerms:
        print(term)