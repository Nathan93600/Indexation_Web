def filter_documents(processed_query, documents, mode='AND'):
    filtered_docs = []
    for doc in documents:
        doc_tokens = set(doc['content'].lower().split())  # Exemple de prétraitement
        if mode == 'AND':
            if all(token in doc_tokens for token in processed_query):
                filtered_docs.append(doc)
        elif mode == 'OR':
            if any(token in doc_tokens for token in processed_query):
                filtered_docs.append(doc)
    return filtered_docs

