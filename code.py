import os
import streamlit as st
import google.generativeai as genai

# Retrieve the API key from environment variables
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the Gemini API
genai.configure(api_key=api_key)

# Set up the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit app
def main():
    # Set the page layout
    st.set_page_config(page_title="Code Generator", page_icon=":computer:", layout="wide")
    
    # Header section with custom styling
    st.markdown(
        """
        <div style="background-color:#4A90E2;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">AI-Powered Code Generator</h1>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Sidebar with language selection
    st.sidebar.header("Configuration")
    language = st.sidebar.selectbox("Select Programming Language", ["Python", "JavaScript", "C++", "Java"])
    
    # User input section
    st.write("### Describe the Code You Want to Generate")
    user_input = st.text_area(
        "Enter your description here...",
        placeholder="e.g., Create a Python function that sorts a list of numbers using bubble sort."
    )
    
    # Button to generate code
    if st.button("Generate Code :rocket:"):
        if user_input:
            # Start a chat session with the model
            chat_session = model.start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": [
                            f"Generate code in {language} and explain it. Here is the description: {user_input}"
                        ],
                    },
                ]
            )

            # Send the message and get the response
            response = chat_session.send_message(user_input)
            
            # Display the generated code and explanation
            st.write("### Generated Code")
            st.code(response.text, language.lower())
        else:
            st.warning("Please provide a description for the code generation.")
    
    # Footer with additional information
    st.markdown(
        """
        <hr>
        <div style="text-align:center;">
            <small>Powered by <strong>Google Gemini API</strong> | Created by Bimal Babu</small>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
