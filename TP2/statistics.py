import json
from data_processing import clean_text, tokenize
from bs4 import BeautifulSoup

def generate_statistics(urls_file):
    tokens_count = 0
    documents_count = 0
    with open(urls_file, 'r') as file:
        urls = json.load(file)
    for url in urls:
        with open(url['filepath'], 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            title = soup.title.string if soup.title else ''
            tokens = tokenize(clean_text(title))
            tokens_count += len(tokens)
            documents_count += 1
    average_tokens_per_document = tokens_count / documents_count if documents_count else 0
    metadata = {
        'total_documents': documents_count,
        'total_tokens': tokens_count,
        'average_tokens_per_document': average_tokens_per_document,
    }
    with open('metadata.json', 'w') as file:
        json.dump(metadata, file)
