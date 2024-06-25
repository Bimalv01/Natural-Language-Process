import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

while True:
    # Input text
    text = input("Enter text: ")

    # Word Tokenization
    words = word_tokenize(text)
    print("Original Words:", words)

    # Lemmatization
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    print("Lemmatized Words:", lemmatized_words)
