import Preprocessing as pre
import TermWeighting as termW
import MultiNomialNaiveBayesClassification as mul
from MultiNomialNaiveBayesClassification import Document

def read_file(filename):
    # read csv file
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

# Open file
# source = open("clustering-class.txt", "r")
# source = source.read()
documents = read_file("sms.csv")
print(len(documents))
# documents = documents[0:4] + documents[10:14] + documents[20:24]
# documents = documents[0:6] + documents[10:16] + documents[20:26]
# documents = documents[0:8] + documents[10:18] + documents[20:28]
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
# print_array(rawWeight)

for i in range(len(documents)):
    documents[i].frequencies = rawWeight[i]
# print_documents(documents)

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
