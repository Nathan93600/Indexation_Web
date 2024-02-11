from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def process_query(query):
    # Tokenisation et mise en minuscules
    tokens = word_tokenize(query.lower())
    
    # Filtrer les tokens qui ne sont pas des stop words ou de la ponctuation
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english') and token not in string.punctuation]
    
    return filtered_tokens
