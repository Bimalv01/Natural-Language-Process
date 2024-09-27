import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download the NLTK data needed for tokenization and stemming
nltk.download('punkt')

# Input text
text = "This is an example sentence for tokenization and stemming."

# Tokenization
tokens = word_tokenize(text)
print("Tokens: ", tokens)

# Stemming
ps = PorterStemmer()
stemmed_tokens = [ps.stem(token) for token in tokens]
print("Stemmed Tokens: ", stemmed_tokens)