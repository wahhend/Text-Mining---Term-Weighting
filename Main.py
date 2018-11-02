import Preprocessing as pre
import TermWeighting as termW
from Output import Output

source = open("source.txt", "r")
source = source.read()
output = Output()

documents = pre.tokenization(source)
output.write_pre(documents, "tokenization")

documents = pre.filtering(documents)
output.write_pre(documents, "filtering")

documents = pre.stemming(documents)
output.write_pre(documents, "stemming")

terms = pre.termFromDocuments(documents)

output.column_number = 0

binaryWeight = termW.binaryTermWeighting(terms, documents)
output.write_term_weight(terms, binaryWeight, "Binary term frequency")

rawWeight = termW.rawTermWeighting(terms, documents)
output.write_term_weight(terms, rawWeight, "Raw term frequency")

logWeight = termW.logTermWeighting(terms, documents)
output.write_term_weight(terms, logWeight, "Log term frequency")

df = termW.documentFrequency(terms, documents)
output.write_doc_frequency(df, "Document frequencies")

idf = termW.inverseDocumentFrequency(df, documents)
output.write_doc_frequency(idf, "Inverse Document Frequencies")

tf_idf = termW.tf_idf(logWeight, idf)
output.write_term_weight(terms, tf_idf, "tf * idf")

output.save("result.xls")