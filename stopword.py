import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Get the list of English stopwords
stop_words = set(stopwords.words('english'))

while True:
    # Input text
    text = input("Enter text: ")

    # Word Tokenization
    words = word_tokenize(text)
    print("Original Words:", words)

    # Stop word removal
    filtered_words = [word for word in words if word.lower() not in stop_words]
    print("Words after Stop word removal:", filtered_words)
