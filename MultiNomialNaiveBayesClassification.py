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
    classes = [document.classification for document in documents]
    classes = set(classes)
    likelihood = list()

    for c in classes:
        class_term_frequencies = list()
        total_terms = numpy.sum(
            [document.frequencies for document in documents if document.classification == c]) + len(terms)

        for i in range(len(terms)):
            term_frequencies = [document.frequencies[i]
                                for document in documents if document.classification == c]
            class_term_frequencies.append(
                (sum(term_frequencies) + 1) / total_terms)

        likelihood.append(ClassLikelihood(
            dict(zip(terms, class_term_frequencies)), c))

    return likelihood


def count_likelihood(word, terms, documents, selected_class):
    idx = terms.index(word)
    term_frequencies = [document.frequencies[idx]
                        for document in documents if document.classification == selected_class]

    total_frequencies = sum(term_frequencies) + 1
    total_terms = numpy.sum(
        [document.frequencies for document in documents if document.classification == selected_class]) + len(terms)

    return total_frequencies / total_terms


def prior(documents, selected_class):
    return len([document for document in documents if document.classification == selected_class]) / len(documents)


def decision(query, terms, documents):
    likelihood = all_likelihood(terms, documents)
    query = query.split(" ")

    posterior = dict()
    for class_likelihood in likelihood:
        likely = 1

        for word in query:
            likely *= class_likelihood.likelihood[word]

        likely *= prior(documents, class_likelihood.classification)

        posterior[class_likelihood.classification] = likely

    return max(posterior, key=posterior.get)
