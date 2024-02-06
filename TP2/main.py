from statistics import generate_statistics
from index_builder import build_non_positional_index, build_stemmed_index, build_positional_index

def main():
    urls_file = 'urls.json'
    generate_statistics(urls_file)
    build_non_positional_index(urls_file)
    build_stemmed_index(urls_file)
    build_positional_index(urls_file)

if __name__ == "__main__":
    main()