import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download necessary NLTK data files
nltk.download('punkt')

# Initialize the PorterStemmer
stemmer = PorterStemmer()

while True:
    # Input text
    text = input("Enter text: ")

    # Word Tokenization
    words = word_tokenize(text)
    print("Original Words:", words)

    # Stemming
    stemmed_words = [stemmer.stem(word) for word in words]
    print("Stemmed Words:", stemmed_words)
