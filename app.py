import streamlit as st
from textblob import TextBlob

# Function to analyze clothing reviews
def analyze_review(text):
    score = round(TextBlob(str(text)).sentiment.polarity, 2)
    if score > 0:
        sentiment = "Positive 😊"
    elif score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    t = str(text).lower()
    topics = []
    if any(word in t for word in ["size", "fit", "small", "large", "tight", "loose"]):
        topics.append("Size & Fit")
    if any(word in t for word in ["fabric", "material", "soft", "rough", "thin"]):
        topics.append("Fabric Quality")
    if any(word in t for word in ["color", "fade", "shade"]):
        topics.append("Color & Look")
    if any(word in t for word in ["price", "cost", "worth", "expensive"]):
        topics.append("Price")
    if any(word in t for word in ["delivery", "shipping", "arrive", "late"]):
        topics.append("Delivery")

    topic = ", ".join(topics) if topics else "General"
    return sentiment, score, topic

# App interface
st.set_page_config(page_title="Wear Style Analyzer", layout="centered")
st.title("👕 Wear Style — Review Analyzer")
st.write("Paste any clothing review to check sentiment and what it is about.")

user_input = st.text_area("Enter your review here:", height=180)

if st.button("Analyze Review"):
    if user_input.strip():
        res, scr, top = analyze_review(user_input)
        st.success(f"**Result:** {res}")
        st.info(f"**Score:** {scr} | **Topic:** {top}")
    else:
        st.warning("⚠️ Please type or paste a review first!")
    
