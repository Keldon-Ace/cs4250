#-------------------------------------------------------------------------
# AUTHOR: Keldon Davis Aceituno
# FILENAME: index.py
# SPECIFICATION: Program that applies surface level normalization and lemmatization
# FOR: CS 4250 - Assignment #1
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
lemmas = {
    "new": "new",
    "homes": "home",
    "home": "home",
    "sale": "sale",
    "sales": "sale",
    "increases": "increase",
    "increasing": "increase",
    "rising": "rise",
    "rise": "rise",
    "in": "in",
    "july": "july"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():
    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    normalizedText = text.lower()
    normalizedText = normalizedText.replace(".", "")
    normalizedText = normalizedText.replace(",", "")

    # Tokenizing the document
    tokens = normalizedText.split()

    # Applying lemmatization
    lemmatizedTokens = [lemmas.get(token, token) for token in tokens]

    # Building the inverted index
    for term in lemmatizedTokens:
        if term not in invertedIndex:
            invertedIndex[term] = []
        if docID not in invertedIndex[term]:
            invertedIndex[term].append(docID)

# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
for term in sorted(invertedIndex.keys()):
    print(term, ":", invertedIndex[term])