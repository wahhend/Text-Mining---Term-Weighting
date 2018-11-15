import Preprocessing as pre
import TermWeighting as termW
import InformationRetrieval as IR
import numpy
from Output import Output

source = open("clustering-class.txt", "r")
source = source.read()
output = Output()

tokenized = pre.tokenization(source)
stemmed = pre.stemming(tokenized)
documents = pre.filtering(stemmed)

terms = pre.termFromDocuments(documents)
# binaryWeight = termW.binaryTermWeighting(terms, documents)
# rawWeight = termW.rawTermWeighting(terms, documents)
logWeight = termW.logTermWeighting(terms, documents)

df = termW.documentFrequency(terms, documents)
idf = termW.inverseDocumentFrequency(df, documents)
tf_idf = termW.tf_idf(logWeight, idf)
wtd_normalized = IR.normalization(tf_idf)

query = pre.tokenization('burung terbang.')
query = pre.stemming(query)
query = pre.filtering(query)

query_weight = termW.logTermWeighting(terms, query)
query_weight = termW.tf_idf(query_weight, idf)
query_normalized = IR.normalization(query_weight)
query_normalized = numpy.array(query_normalized[0])

cosine_similarity = IR.cosine_similarity(wtd_normalized, query_normalized)
distances = IR.distance(cosine_similarity)
ranked = IR.ranked_retrieval(distances)

print('similarity')
distances = list(distances)
for similarity in ranked:
    print(distances.index(similarity))


# output.write_pre(documents, "tokenization")
# output.write_pre(documents, "stemming")
# output.write_pre(documents, "filtering")
# output.column_number = 0

# output.write_term_weight(terms, binaryWeight, "Binary term frequency")
# output.write_term_weight(terms, rawWeight, "Raw term frequency")
# output.write_term_weight(terms, logWeight, "Log term frequency")

# output.write_doc_frequency(df, "Document frequencies")
# output.write_doc_frequency(idf, "Inverse Document Frequencies")
# output.write_term_weight(terms, tf_idf, "tf * idf")

# output.save("result.xls")