import json
from query_processor import process_query
from document_filter import filter_documents
from ranking import rank_documents
from results_writer import write_results

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    user_query = input("Entrez votre requête : ")
    processed_query = process_query(user_query)
    documents = load_json('TP3/documents.json')
    index = load_json('TP2/index.json')
    
    filtered_docs = filter_documents(processed_query, documents, index, mode='AND')
    ranked_docs = rank_documents(filtered_docs, processed_query)
    write_results(ranked_docs)

if __name__ == "__main__":
    main()
