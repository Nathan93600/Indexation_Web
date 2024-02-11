def filter_documents(processed_query, documents, index, mode='AND'):
    filtered_docs = []
    for doc in documents:
        doc_tokens = set(doc['content'].lower().split()) # Simuler le prétraitement des documents
        if (mode == 'AND' and all(token in doc_tokens for token in processed_query)) or \
           (mode == 'OR' and any(token in doc_tokens for token in processed_query)):
            filtered_docs.append(doc)
    return filtered_docs
