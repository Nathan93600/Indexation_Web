import math
from nltk.corpus import stopwords

# Ensemble de stop words
stop_words = set(stopwords.words('english'))

def bm25_score(doc, processed_query, index, N, avgdl, k1=1.2, b=0.75, weight_factor=2):
    score = 0
    doc_len = len(doc['content'].split())
    for token in processed_query:
        weight = weight_factor if token not in stop_words else 1
        if token in index:
            n = len(index[token])
            f = doc['content'].lower().count(token)
            idf = max(math.log((N - n + 0.5) / (n + 0.5) + 1), 0)  # Ajustement pour éviter les valeurs négatives d'IDF
            tf = (f * (k1 + 1)) / (f + k1 * (1 - b + b * doc_len / avgdl))
            score += (idf * tf) * weight
    return score

def rank_documents(filtered_docs, processed_query, index, N, avgdl, weight_factor=2):
    ranked_docs = sorted(filtered_docs, key=lambda doc: bm25_score(doc, processed_query, index, N, avgdl, weight_factor=weight_factor), reverse=True)
    return ranked_docs
