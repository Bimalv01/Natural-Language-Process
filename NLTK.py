import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stemmer, lemmatizer, and stop words list
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

while True:
    # Sample text
    text = input("Enter text: ")

    # Word Tokenization
    words = word_tokenize(text)
    print("Original Words:", words)

    # Stop word removal
    filtered_words = [word for word in words if word.lower() not in stop_words]
    print("Words after Stop word removal:", filtered_words)

    # Stemming
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    print("Stemmed Words:", stemmed_words)

    # Lemmatization
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    print("Lemmatized Words:", lemmatized_words)
