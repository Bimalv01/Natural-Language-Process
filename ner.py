import streamlit as st
import requests
import spacy
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Initialize SpaCy model
nlp = spacy.load("en_core_web_sm")

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Define a function to fetch a news article based on a headline
def fetch_news_article(api_key, headline):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': headline,
        'apiKey': api_key,
        'pageSize': 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        
        if data.get('status') == 'ok' and data['articles']:
            article = data['articles'][0]
            title = article['title']
            content = article['content']
            return title, content
        else:
            st.error("No articles found or API request failed.")
            return None, None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Define functions to extract named entities
def extract_entities_spacy(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_entities_nltk(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    chunks = ne_chunk(pos_tags)
    entities = []
    for chunk in chunks:
        if hasattr(chunk, 'label'):
            entity = ' '.join(c[0] for c in chunk)
            entities.append((entity, chunk.label()))
    return entities

def compare_entities(spacy_ents, nltk_ents):
    spacy_set = set(spacy_ents)
    nltk_set = set(nltk_ents)
    
    common_ents = spacy_set & nltk_set
    spacy_unique = spacy_set - nltk_set
    nltk_unique = nltk_set - spacy_set
    
    return common_ents, spacy_unique, nltk_unique

# Streamlit app
st.title("Named Entity Recognition Comparison")

# Sidebar for user input
st.sidebar.header("Input")
headline = st.sidebar.text_input("Enter News Headline", "")

# API key (set your own API key here)
api_key = 'e83e0f9cdb4c4864b1dae64dc627b83e'

if headline:
    st.sidebar.write(f"Fetching news for headline: {headline}")
    
    title, content = fetch_news_article(api_key, headline)
    
    if content:
        st.write(f"**Title:** {title}")
        st.write(f"**Content:** {content}")

        # Extract entities
        spacy_entities = extract_entities_spacy(content)
        nltk_entities = extract_entities_nltk(content)

        st.write("### SpaCy Entities")
        st.write(spacy_entities)

        st.write("### NLTK Entities")
        st.write(nltk_entities)

        # Compare entities
        common_ents, spacy_unique, nltk_unique = compare_entities(spacy_entities, nltk_entities)

        st.write("### Comparison Results")
        st.write(f"**Common Entities:** {common_ents}")
        st.write(f"**SpaCy Unique Entities:** {spacy_unique}")
        st.write(f"**NLTK Unique Entities:** {nltk_unique}")
    else:
        st.write("No content found for the given headline.")