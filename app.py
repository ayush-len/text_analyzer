import streamlit as st
from textblob import TextBlob

# 1. UI Setup
st.title("Smart Feedback Analyzer")
st.write("This tool uses Natural Language Processing to detect the emotion in text.")

# 2. User Input
user_input = st.text_area("Paste the text you want to analyze here:")

# 3. The Trigger
if st.button("Run AI Analysis"):
    
    if user_input:
        # 4. The AI Engine at Work
        # We pass the user's text into the TextBlob model
        analysis = TextBlob(user_input)
        
        # TextBlob calculates a "Polarity" score between -1.0 (Very Negative) and 1.0 (Very Positive)
        score = analysis.sentiment.polarity
        
        # 5. Interpreting the Score
        if score > 0.1:
            sentiment_label = "Positive 😃"
            st.success(f"Result: {sentiment_label}")
        elif score < -0.1:
            sentiment_label = "Negative 😠"
            st.error(f"Result: {sentiment_label}")
        else:
            sentiment_label = "Neutral 😐"
            st.warning(f"Result: {sentiment_label}")
            
        # 6. Displaying the raw data (Judges love seeing the math behind the magic)
        st.write("### AI Confidence Metrics:")
        st.metric(label="Polarity Score (-1 to 1)", value=round(score, 2))
        
    else:
        st.warning("Please enter some text first!")