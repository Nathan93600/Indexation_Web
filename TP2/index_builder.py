import json
from data_processing import clean_text, tokenize, stem
from collections import defaultdict
from bs4 import BeautifulSoup

def build_non_positional_index(urls_file):
    index = defaultdict(set)
    with open(urls_file, 'r') as file:
        urls = json.load(file)
    for doc_id, url in enumerate(urls):
        with open(url['filepath'], 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            title = soup.title.string if soup.title else ''
            for token in tokenize(clean_text(title)):
                index[token].add(doc_id)
    with open('title.non_pos_index.json', 'w') as file:
        json.dump({token: list(docs) for token, docs in index.items()}, file)

def build_stemmed_index(urls_file):
    index = defaultdict(set)
    with open(urls_file, 'r') as file:
        urls = json.load(file)
    for doc_id, url in enumerate(urls):
        with open(url['filepath'], 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            title = soup.title.string if soup.title else ''
            for token in stem(tokenize(clean_text(title))):
                index[token].add(doc_id)
    with open('my_stemmer.title.non_pos_index.json', 'w') as file:
        json.dump({token: list(docs) for token, docs in index.items()}, file)

def build_positional_index(urls_file):
    index = defaultdict(lambda: defaultdict(list))
    with open(urls_file, 'r') as file:
        urls = json.load(file)
    for doc_id, url in enumerate(urls):
        with open(url['filepath'], 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            title = soup.title.string if soup.title else ''
            for position, token in enumerate(tokenize(clean_text(title))):
                index[token][doc_id].append(position)
    with open('title.pos_index.json', 'w') as file:
        json.dump(index, file)
