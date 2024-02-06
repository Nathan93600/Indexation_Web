import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def tokenize(text):
    return [word for word in word_tokenize(text) if word not in stop_words]

def stem(tokens):
    return [stemmer.stem(token) for token in tokens]
