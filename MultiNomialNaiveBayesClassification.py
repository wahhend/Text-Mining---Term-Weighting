import numpy


class Document:
    def __init__(self, term_frequencies, classification):
        self.frequencies = term_frequencies
        self.classification = classification


class ClassLikelihood:
    def __init__(self, likelihood, classification):
        self.likelihood = likelihood
        self.classification = classification

    def get_likelihood(self, term):
        return self.likelihood[term]


def all_likelihood(terms, documents):
    classes = [document.classification for document in documents] #setiap dokumen didalam documents diambil klasifikasinya terus dimasukin kedalam array
    classes = set(classes) #tipe datanya gaboleh ada yg sama
    likelihood = []

    for c in classes:
        class_likelihood = list()
        total_terms = numpy.sum(
            [document.frequencies for document in documents if document.classification == c]) + len(terms)

        # for i=0 i<terms.length i++
        for i in range(len(terms)):
            # print([document.frequencies[i] for document in documents if document.classification == c])
            term_frequencies = [document.frequencies[i]
                                for document in documents if document.classification == c]
            class_likelihood.append(
                (sum(term_frequencies) + 1) / total_terms)
        
        likelihood.append(ClassLikelihood(
            dict(zip(terms, class_likelihood)), c)) #array assosiatif, zip -> buat gabung terms sama class likelihood

    return likelihood


def count_likelihood(word, terms, documents, selected_class): #hasilnya cuma 1, misalnya cari likelihood burung yang kategori A (likelihood kata tertentu di kelas tertentu)
    idx = terms.index(word)
    term_frequencies = [document.frequencies[idx]
                        for document in documents if document.classification == selected_class]

    total_frequencies = sum(term_frequencies) + 1
    total_terms = numpy.sum(
        [document.frequencies for document in documents if document.classification == selected_class]) + len(terms)

    return total_frequencies / total_terms


def prior(documents, selected_class):
    # print(selected_class)
    # print([document for document in documents if document.classification == selected_class])
    return len([document for document in documents if document.classification == selected_class]) / len(documents)


def decision(query, terms, documents):
    likelihood = all_likelihood(terms, documents)
    query = query.split(" ")

    posterior = dict()
    for class_likelihood in likelihood: #cari posterior setiap kelas
        likely = 1

        for word in query:
            likely *= class_likelihood.likelihood[word]

        likely *= prior(documents, class_likelihood.classification)

        posterior[class_likelihood.classification] = likely
    # print(posterior)
    return max(posterior, key=posterior.get)
