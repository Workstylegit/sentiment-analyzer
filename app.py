from textblob import TextBlob
import streamlit as st

st.set_page_config(page_title="AI Sentiment Analyzer", layout="centered")
st.title("🤖 AI Sentiment Analyzer")
st.write("Enter any text/review to check if it's Positive, Negative, or Neutral")

user_text = st.text_area("Type your text here:", height=150)

if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        analysis = TextBlob(user_text)
        polarity = round(analysis.sentiment.polarity, 2)

        if polarity > 0:
            result = "Positive 😊"
            color = "green"
        elif polarity < 0:
            result = "Negative 😞"
            color = "red"
        else:
            result = "Neutral 😐"
            color = "gray"

        st.markdown(f"### Result: <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)
        st.info(f"Score: {polarity} (Range: -1 = Most Negative, +1 = Most Positive)")