from statistics import generate_statistics
from index_builder import build_non_positional_index, build_stemmed_index, build_positional_index

import nltk
nltk.download('stopwords')

def main():
    urls_file = 'TP2/crawled_urls.json'
    generate_statistics(urls_file)
    build_non_positional_index(urls_file)
    build_stemmed_index(urls_file)
    build_positional_index(urls_file)

if __name__ == "__main__":
    main()
