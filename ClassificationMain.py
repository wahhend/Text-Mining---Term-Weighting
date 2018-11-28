import Preprocessing as pre
import TermWeighting as termW
import MultiNomialNaiveBayesClassification as mul
from MultiNomialNaiveBayesClassification import Document

# Open file
source = open("clustering-class.txt", "r")
source = source.read()

# Preprocessing
tokenized = pre.tokenization(source)
stemmed = pre.stemming(tokenized)
documents = pre.filtering(stemmed)

# Term Weighting
terms = pre.termFromDocuments(documents)
rawWeight = termW.rawTermWeighting(terms, documents)

documents = list()
documents.append(Document(rawWeight[0], 'A'))
documents.append(Document(rawWeight[1], 'B'))
documents.append(Document(rawWeight[2], 'A'))
documents.append(Document(rawWeight[3], 'B'))
documents.append(Document(rawWeight[4], 'B'))

# Classification
print(mul.all_likelihood(terms, documents)