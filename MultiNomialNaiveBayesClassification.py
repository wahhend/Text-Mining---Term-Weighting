import numpy


# Document class for saving term frequencies and document classification
class Document:
    def __init__(self, term_frequencies, classification):
        self.frequencies = term_frequencies
        self.classification = classification


# ClassLikelihood class for saving likelihood of each words in every classes
# All likelihood has been calculated before counting posterior
# Likelihood saved in dictionary and accessed when counting posterior
class ClassLikelihood:
    def __init__(self, likelihood, classification):
        self.likelihood = likelihood
        self.classification = classification

    def get_likelihood(self, term):
        return self.likelihood[term]


# Calculate all likelihood of each terms in every classes
def all_likelihood(terms, documents):
    classes = [document.classification for document in documents]
    classes = set(classes)
    likelihood = []

    for c in classes:
        class_likelihood = list()
        total_terms = numpy.sum(
            [document.frequencies for document in documents if document.classification == c]) + len(terms)

        for i in range(len(terms)):
            term_frequencies = [document.frequencies[i]
                                for document in documents if document.classification == c]
            class_likelihood.append(
                (sum(term_frequencies) + 1) / total_terms)
        
        likelihood.append(ClassLikelihood(
            dict(zip(terms, class_likelihood)), c))

    return likelihood


# Calculate spesific likelihood from speeific term and class
# I don't use this function, this is just my exercise function
def count_likelihood(word, terms, documents, selected_class):
    idx = terms.index(word)
    term_frequencies = [document.frequencies[idx]
                        for document in documents if document.classification == selected_class]

    total_frequencies = sum(term_frequencies) + 1
    total_terms = numpy.sum(
        [document.frequencies for document in documents if document.classification == selected_class]) + len(terms)

    return total_frequencies / total_terms


# Calculate prior of selected class
def prior(documents, selected_class):
    return len([document for document in documents if document.classification == selected_class]) / len(documents)


# Classify query to one of the classes available
def decision(query, terms, documents):
    likelihood = all_likelihood(terms, documents)

    posterior = dict()
    for class_likelihood in likelihood:
        likely = 1

        for word in query:
            try:
                likely *= class_likelihood.likelihood[word]
            except:
                pass

        likely *= prior(documents, class_likelihood.classification)

        posterior[class_likelihood.classification] = likely
    
    return max(posterior, key=posterior.get)
