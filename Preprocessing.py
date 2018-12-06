import numpy
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def tokenization(source):
    source = source.lower()
    source = source[:-1]
    source = source.replace(",", "")
    source = source.split(". ")
    
    documents = []
    for document in source:
        documents.append(document.split(" "))
    
    return documents

def advanced_filtering(documents):
    pass


def filtering(documents):
    stopwords = open("stopword-list.txt", "r")
    stopwords = stopwords.read()
    stopwords = stopwords.split("\n")

    filtered = []

    for document in documents:
        #untuk setiap kata dalam dokumen, jika kata gak ada di stopwords, maka kata tsb masuk di []
        #masukin kata yg ada di [] ke filtered -> jadinya array 2D
        filtered.append([word for word in document if word not in stopwords])
        
    return filtered


def stemming(documents):
    stemmer = StemmerFactory().create_stemmer()
    stemmed = []
    for document in documents:
        words = []
        for word in document:
            words.append(stemmer.stem(word))
        stemmed.append(words)

    return stemmed


def printDocs(documents):
    for document in documents:
        print(document)


def termFromDocuments(documents):
    terms = []
    for document in documents: #untuk setiap dokumen dalam banyak dokumen
        for word in document: #untuk setiap kata dalam dokumen
            #print(word)
            if word not in terms: #jika kata tidak ada di term
                terms.append(word) #masukan kata tsn ke terms
                #print(terms)
    
    return terms


def clean_query(query):
    query = query.split(" ")