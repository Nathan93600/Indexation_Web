def rank_documents(filtered_docs, processed_query):
    ranked_docs = sorted(filtered_docs, key=lambda doc: sum(doc['content'].lower().count(token) for token in processed_query), reverse=True)
    return ranked_docs
