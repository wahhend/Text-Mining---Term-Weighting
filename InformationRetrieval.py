import numpy

def normalization(tf_idf):
    squared_tf_idf = numpy.array(tf_idf) ** 2
    
    vector_length = list()
    vector_length = numpy.sum(squared_tf_idf, 1) ** 0.5
    
    normalized_tf_idf = list()
    for i in range(vector_length.shape[0]):
        normalized_tf_idf.append(tf_idf[i] / vector_length[i])
    
    return normalized_tf_idf

def cosine_similarity(normalized_tf_idf, query):
    cosim = query * normalized_tf_idf
    return numpy.sum(cosim, 1)

def distance(cosine_similarity):
    distances = 1 - cosine_similarity
    return numpy.where(distances > 1.0e-10, distances, 0)

def ranked_retrieval(distances):
    return numpy.sort(distances)
