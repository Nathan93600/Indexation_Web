import json
from query_processor import process_query
from document_filter import filter_documents
from ranking import rank_documents, bm25_score
from results_writer import write_results

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def calculate_avgdl(documents):
    total_length = sum(len(doc['content'].split()) for doc in documents)
    return total_length / len(documents)

def main():
    # Chargement des données
    documents = load_json('TP3/documents.json')
    index = load_json('TP2/technology documentindex.json')
    
    # Calcul de N et avgdl
    N = len(documents)
    avgdl = calculate_avgdl(documents)
    
    # Requête utilisateur
    user_query = input("Entrez votre requête : ")
    mode = input("Choisissez le mode de filtrage (AND/OR): ").strip().upper()
    
    # Prétraitement de la requête
    processed_query = process_query(user_query)
    
    # Filtrage des documents
    filtered_docs = filter_documents(processed_query, documents, mode)
    
    # Classement des documents
    ranked_docs = rank_documents(filtered_docs, processed_query, index, N, avgdl)
    
    # Écriture des résultats
    write_results(ranked_docs)

if __name__ == "__main__":
    main()
