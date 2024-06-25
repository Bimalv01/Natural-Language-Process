import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS, preprocess_string
import spacy

# Sample Text
text = "NLTK is a leading platform for building Python programs to work with human language data. It's very useful for text processing."

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Tokenize using spaCy
doc = nlp(text)
words = [token.text for token in doc]
print("\nOriginal Words (spaCy):", words)

# Remove stop words using gensim
filtered_words_gensim = [word for word in words if word.lower() not in STOPWORDS]
print("\nFiltered Words (gensim):", filtered_words_gensim)

# Remove stop words using spaCy
filtered_words_spacy = [token.text for token in doc if not token.is_stop]
print("\nFiltered Words (spaCy):", filtered_words_spacy)

# Stemming using gensim
stemmer = gensim.parsing.porter.PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemmed Words (gensim):", stemmed_words)

# Lemmatization using spaCy
lemmatized_words = [token.lemma_ for token in doc]
print("\nLemmatized Words (spaCy):", lemmatized_words)