import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Title of the Streamlit app
st.title("Language Translator")

# User input for the text to translate
user_text = st.text_area("Enter text to translate")

# Detect the language of the user input
if user_text:
    detected_lang = translator.detect(user_text).lang
    detected_lang_name = LANGUAGES[detected_lang]
    st.write(f"Detected input language: **{detected_lang_name.capitalize()}**")

# Dropdown to select the target language
target_lang = st.selectbox(
    "Select the language you want to translate to",
    list(LANGUAGES.values())
)

# Translate the text when the user presses the button
if st.button("Translate"):
    # Get the language code for the selected target language
    target_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)]

    # Translate the text
    translation = translator.translate(user_text, dest=target_lang_code)

    # Display the translated text
    st.write(f"Translated text: **{translation.text}**")
