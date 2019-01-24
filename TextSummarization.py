import numpy


def sum_tf(term_frequency):
    term_frequency = numpy.array(term_frequency)
    term_frequency = numpy.sum(term_frequency, 0)

    return term_frequency


def log_tf(term_frequency):
    return 1 + numpy.log10(term_frequency)


def new_tf(term_frequency, log_tf):
    term_frequency = numpy.float64(numpy.array(term_frequency))
    
    for i in range(len(term_frequency)):
        term_frequency[i] = numpy.where(term_frequency[i] > 0, log_tf, 0)

    return term_frequency


def document_weight(term_frequency):
    return numpy.sum(term_frequency, 1)
