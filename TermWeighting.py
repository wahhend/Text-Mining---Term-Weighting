import math


def binaryTermWeighting(terms, documents):
    binaryWeight = []

    for document in documents:
        documentWeight = []
        for term in terms:
            if term in document:
                documentWeight.append(1)
            else:
                documentWeight.append(0)

        binaryWeight.append(documentWeight)

    return binaryWeight


def rawTermWeighting(terms, documents):
    rawWeight = []

    for document in documents:
        documentWeight = []
        for term in terms:
            documentWeight.append(document.count(term))

        rawWeight.append(documentWeight)

    return rawWeight


def logTermWeighting(terms, documents):
    logWeight = []

    for document in documents:
        documentWeight = []
        for term in terms:
            count = document.count(term)
            if count > 0:
                documentWeight.append(1 + math.log10(count))
            else:
                documentWeight.append(0)

        logWeight.append(documentWeight)

    return logWeight


def documentFrequency(terms, documents):
    df = []

    for term in terms:
        dfWeight = 0
        for document in documents:
            if term in document:
                dfWeight += 1
        df.append(dfWeight)

    return df


def inverseDocumentFrequency(dfs, documents):
    return [math.log10(len(documents) / df) for df in dfs]


def tf_idf(termFrequencies, inverseDocumentFrequencies):
    tf_idf = []

    for documentTermFrequencies in termFrequencies:
        row_tf_idf = []
        for i in range(0, len(inverseDocumentFrequencies)):
            row_tf_idf.append(documentTermFrequencies[i]*inverseDocumentFrequencies[i])
        tf_idf.append(row_tf_idf)

    return tf_idf
