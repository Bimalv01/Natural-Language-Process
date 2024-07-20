from textblob import TextBlob
import streamlit as st

def correct_spelling(text):
    """Correct the spelling of the input text."""
    word = TextBlob(text)
    return word.correct()

# Set the title of the app
st.title("Automatic Spelling Correction")

# Get user input
user_input = st.text_input("Enter your text here...")

# Button to trigger spelling correction
if st.button("Click here to correct your words"):
    corrected_text = correct_spelling(user_input)
    # Display the corrected text
    st.subheader("Corrected Text:")
    st.write(str(corrected_text))
