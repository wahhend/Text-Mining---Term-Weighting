import numpy


class Document:
    def __init__(self, term_frequencies, classification):
        self.frequencies = term_frequencies
        self.classification = classification


def all_likelihood(terms, documents):
    return

def likelihood(word, terms, documents, selected_class):
    idx = terms.index(word)
    term_frequencies = [document.frequencies[idx]
                        for document in documents if document.classification == selected_class]

    total_frequencies = sum(term_frequencies) + 1
    total_terms = numpy.sum(
        [document.frequencies for document in documents if document.classification == selected_class]) + len(terms)

    return total_frequencies / total_terms


def prior()
