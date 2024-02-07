import json
from data_processing import clean_text, tokenize
from bs4 import BeautifulSoup

import json

def generate_statistics(urls_file):
    with open(urls_file, 'r', encoding='utf-8') as file:
        urls_data = json.load(file)

    total_titles_length = sum(len(data['title']) for data in urls_data)
    total_documents = len(urls_data)
    average_title_length = total_titles_length / total_documents if total_documents else 0

    print(f"Total documents: {total_documents}")
    print(f"Total length of all titles: {total_titles_length}")
    print(f"Average title length: {average_title_length}")

