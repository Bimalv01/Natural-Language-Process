# streamlit_translator_detect.py
import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Streamlit App Title
st.title("Language Translator with Auto Language Detection")

# Input Text from the User
text_to_translate = st.text_area("Enter text to translate:", "")

# Detect the language automatically when the user enters text
detected_language = None
if text_to_translate.strip():
    detected_lang_code = translator.detect(text_to_translate).lang
    detected_language = LANGUAGES.get(detected_lang_code, "unknown")
    st.write(f"**Detected Language:** {detected_language.capitalize()}")

# Language Selection for Translation
target_language = st.selectbox("Select target language", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('es'))

# Get the target language code from the selected language
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Translate Button
if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        # Translation
        try:
            translated_text = translator.translate(text_to_translate, dest=target_language_code).text
            st.success("Translation Successful!")
            st.write(f"**Translated Text:** {translated_text}")
        except Exception as e:
            st.error(f"Error: {e}")

# Display supported languages in a collapsible section
with st.expander("Supported Languages"):
    st.write(", ".join(LANGUAGES.values()))
