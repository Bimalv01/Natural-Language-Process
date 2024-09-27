import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download the NLTK data needed for tokenization, stemming, lemmatization, and stop words
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Input text
text = "This is an example sentence for tokenization, stemming, lemmatization, and stop word removal."

# Tokenization
tokens = word_tokenize(text)

# Stop word removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token not in stop_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# Output
print("Tokens: ", tokens)
print("Filtered Tokens (after stop word removal): ", filtered_tokens)
print("Lemmatized Tokens: ", lemmatized_tokens)