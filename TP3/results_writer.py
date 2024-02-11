import json

def write_results(ranked_docs):
    results = {'documents': ranked_docs, 'total_docs': len(ranked_docs)}
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)
