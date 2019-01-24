import Preprocessing as pre
import TermWeighting as termW
import MultiNomialNaiveBayesClassification as mul
from MultiNomialNaiveBayesClassification import Document

# read csv file
# each row contains text and its classification
def read_file(filename):
    documents = []
    with open(filename) as inputfile:
        for line in inputfile:
            line = line.split(",")
            document = ""
            for i in range(len(line) - 1):
                document += line[i]
            classification = line[len(line)-1]
            documents.append(Document(document, classification))

    return documents


def read_test_data(filename):
    # read csv file
    documents = []
    with open(filename) as inputfile:
        for line in inputfile:
            # line = line.split(",")
            # document = ""
            # for i in range(len(line) - 1):
            #     document += line[i]
            # classification = line[len(line)-1]
            documents.append(line)

    return documents



def print_documents(documents):
    for document in documents:
        print(document.frequencies, document.classification)


def return_processed_data(documents, data):
    for i in range(len(documents)):
        documents[i].frequencies = data[i]


def print_array(documents):
    for document in documents:
        print(document)


documents = read_file("sms.csv")
print(len(documents))

# Preprocessing
texts = pre.tokenization([document.frequencies for document in documents])
texts = pre.advanced_filtering(texts)
texts = pre.filtering(texts)
texts = pre.stemming(texts)
texts = pre.filtering(texts)
terms = pre.termFromDocuments(texts)

# Term Weighting
rawWeight = termW.rawTermWeighting(terms, texts)
# Insert term frequencies to each document
for i in range(len(documents)):
    documents[i].frequencies = rawWeight[i]

# Read test data
test_data = read_test_data("test_data.csv")
test_data = pre.tokenization(test_data)
test_data = pre.advanced_filtering(test_data)
test_data = pre.filtering(test_data)
test_data = pre.stemming(test_data)
test_data = pre.filtering(test_data)

# Classification
i = 1
for test in test_data:
    print(i, mul.decision(test, terms, documents))
    i+=1
