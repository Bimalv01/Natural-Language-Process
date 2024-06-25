import spacy

# Load SpaCy English model
nlp = spacy.load('en_core_web_sm')

def process_text(text):
    """
    Process the input text for tokenization, lemmatization, and stopword removal.
    
    Args:
    - text (str): Input text to process.
    
    Returns:
    - filtered_tokens (list): List of filtered tokens after stopword removal and lemmatization.
    """
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Filter tokens (remove stopwords and punctuation)
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    
    return filtered_tokens

def print_results(filtered_tokens):
    """
    Print the results of tokenization and lemmatization.
    
    Args:
    - filtered_tokens (list): List of filtered tokens after processing.
    """
    # Print filtered words after stopword removal
    print("\nFiltered Words (Stopword Removal):")
    print([token.text for token in filtered_tokens])
    
    # Print stemmed words (using lemmatizer as proxy)
    print("\nStemmed Words (using Lemmatizer as proxy):")
    print([token.lemma_ for token in filtered_tokens])

def main():
    # Sample text
    text = "Hello there! How are you doing today? This is a sample text for tokenization, stemming, lemmatization, and stopword removal."
    
    # Process the text
    filtered_tokens = process_text(text)
    
    # Print results
    print_results(filtered_tokens)

if __name__ == "__main__":
    main()
