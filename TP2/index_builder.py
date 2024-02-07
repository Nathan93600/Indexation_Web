import json
from data_processing import clean_text, tokenize, stem
from collections import defaultdict
from bs4 import BeautifulSoup
from collections import defaultdict
import json
from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def build_non_positional_index(urls_file):
    index = defaultdict(set)
    with open(urls_file, 'r', encoding='utf-8') as file:
        urls_data = json.load(file)
    
    for i, data in enumerate(urls_data):
        tokens = tokenize(clean_text(data['title']))
        for token in tokens:
            index[token].add(i)
    
    with open('title.non_pos_index.json', 'w', encoding='utf-8') as file:
        json.dump({token: list(doc_ids) for token, doc_ids in index.items()}, file, ensure_ascii=False)




def build_stemmed_index(urls_file):
    stemmer = PorterStemmer()
    index = defaultdict(set)
    with open(urls_file, 'r', encoding='utf-8') as file:
        urls_data = json.load(file)
    
    for i, data in enumerate(urls_data):
        title = data['title']
        # Nettoyez et tokenisez le titre
        tokens = word_tokenize(clean_text(title))
        # Appliquez le stemming sur les tokens
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        for token in stemmed_tokens:
            index[token].add(i)
    
    # Sauvegardez l'index construit
    with open('my_stemmer.title.non_pos_index.json', 'w', encoding='utf-8') as file:
        json.dump({token: list(doc_ids) for token, doc_ids in index.items()}, file, ensure_ascii=False)


def build_positional_index(urls_file):
    index = defaultdict(lambda: defaultdict(list))
    with open(urls_file, 'r', encoding='utf-8') as file:
        urls_data = json.load(file)
    
    for i, data in enumerate(urls_data):
        # Supposons que nous travaillons avec les titres pour cet exemple
        title = data['title']
        tokens = word_tokenize(clean_text(title))
        for position, token in enumerate(tokens):
            index[token][i].append(position)
    
    # Sauvegardez l'index construit
    with open('title.pos_index.json', 'w', encoding='utf-8') as file:
        json.dump(index, file, ensure_ascii=False)


