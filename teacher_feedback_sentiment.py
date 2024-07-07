import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'positive'
    elif score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Streamlit App
st.title('Sentiment Analysis of Teacher Feedback')

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = load_data(uploaded_file).copy()
    
    required_columns = ['Teacher ID', 'Positive Feedback', 'Negative Feedback', 'Improvement Suggestions', 'Additional Comments']
    
    if all(col in df.columns for col in required_columns):
        # Apply sentiment analysis to the text attributes
        df['Positive Feedback Sentiment'] = df['Positive Feedback'].apply(get_sentiment)
        df['Negative Feedback Sentiment'] = df['Negative Feedback'].apply(get_sentiment)
        df['Improvement Suggestions Sentiment'] = df['Improvement Suggestions'].apply(get_sentiment)
        df['Additional Comments Sentiment'] = df['Additional Comments'].apply(get_sentiment)
        
        # Aggregate sentiment by Teacher ID
        positive_feedback = df[df['Positive Feedback Sentiment'] == 'positive'].groupby('Teacher ID').size()
        negative_feedback = df[df['Negative Feedback Sentiment'] == 'negative'].groupby('Teacher ID').size()
        total_feedback = df.groupby('Teacher ID').size()
        
        # Merge results into a single DataFrame
        feedback_summary = pd.DataFrame({
            'Positive Feedback': positive_feedback,
            'Negative Feedback': negative_feedback,
            'Total Feedback': total_feedback
        }).fillna(0)
        
        # Calculate percentage and overall performance
        feedback_summary['Positive Percentage'] = (feedback_summary['Positive Feedback'] / feedback_summary['Total Feedback']) * 100
        feedback_summary['Negative Percentage'] = (feedback_summary['Negative Feedback'] / feedback_summary['Total Feedback']) * 100
        feedback_summary['Overall Performance'] = feedback_summary['Positive Percentage'] - feedback_summary['Negative Percentage']
        
        st.write("## Overall Performance of All Teachers")
        
        # Plot overall performance of all teachers
        fig, ax = plt.subplots(1, 2, figsize=(15, 7))
        
        # Bar plot for overall performance percentages
        feedback_summary[['Positive Percentage', 'Negative Percentage']].plot(kind='bar', stacked=True, ax=ax[0])
        ax[0].set_title('Positive and Negative Feedback Percentages by Teacher')
        ax[0].set_xlabel('Teacher ID')
        ax[0].set_ylabel('Percentage')
        ax[0].legend(['Positive Percentage', 'Negative Percentage'])
        
        # Bar plot for overall performance
        feedback_summary['Overall Performance'].plot(kind='bar', ax=ax[1])
        ax[1].set_title('Overall Performance by Teacher')
        ax[1].set_xlabel('Teacher ID')
        ax[1].set_ylabel('Overall Performance (%)')
        
        st.pyplot(fig)
        
        teacher_ids = feedback_summary.index.tolist()
        selected_teacher_id = st.selectbox('Select Teacher ID:', teacher_ids)
        
        if selected_teacher_id:
            feedback_data = feedback_summary.loc[selected_teacher_id]
            
            st.write(f"### Feedback Summary for Teacher ID: {selected_teacher_id}")
            st.write(feedback_data)
            
            # Plotting the results for the selected teacher
            fig, ax = plt.subplots(figsize=(5, 5))
            
            # Pie chart for feedback percentages
            ax.pie(feedback_data[['Positive Percentage', 'Negative Percentage']], labels=['Positive Percentage', 'Negative Percentage'], autopct='%1.1f%%', startangle=50)
            ax.set_title('Feedback Percentage')
            
            st.pyplot(fig)
            
            st.write(f"### Overall Performance: {feedback_data['Overall Performance']:.2f}%")
    else:
        st.error(f"The uploaded CSV does not contain the required columns: {', '.join(required_columns)}")
else:
    st.info("Please upload a CSV file to proceed.")
