import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora

# Sample text
text = "Hello there! How are you doing today? This is a sample text for tokenization, stemming, lemmatization, and stopword removal."

# Tokenization
def tokenize(text):
    return [token for token in simple_preprocess(text)]

# Remove stopwords
def remove_stopwords(tokens):
    return [token for token in tokens if token not in STOPWORDS]

# Create a dictionary and corpus
def create_corpus(tokens):
    dictionary = corpora.Dictionary([tokens])
    corpus = [dictionary.doc2bow(tokens)]
    return dictionary, corpus

# Lemmatization (Gensim doesn't have a built-in stemmer, so we'll focus on lemmatization)
def lemmatize(tokens, dictionary):
    return [dictionary[word_id] for word_id, _ in tokens]

# Perform the steps
tokens = tokenize(text)
filtered_tokens = remove_stopwords(tokens)
dictionary, corpus = create_corpus(filtered_tokens)
lemmatized_tokens = lemmatize(corpus[0], dictionary)

# Print results
print("Tokens after tokenization:")
print(tokens)
print("\nFiltered Tokens (after stopword removal):")
print(filtered_tokens)
print("\nLemmatized Tokens:")
print(lemmatized_tokens)