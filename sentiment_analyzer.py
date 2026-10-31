
import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="😊",
    layout="wide"
)

analyzer = SentimentIntensityAnalyzer()

st.title("AI-Based Sentiment Analysis")
st.write("Analyze customer reviews and understand their emotions.")

st.subheader("Enter Your Text")

user_text = st.text_area(
    "Write a review or sentence:",
    placeholder="Example: This product is amazing!"
)

if st.button("Analyze Sentiment"):
    if user_text.strip():

        scores = analyzer.polarity_scores(user_text)
        compound = scores["compound"]

        if compound >= 0.05:
            sentiment = "Positive"
            emoji = "😊"
        elif compound <= -0.05:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"

        st.divider()
        st.subheader("Analysis Result")

        col1, col2 = st.columns(2)

        col1.metric("Sentiment", sentiment)
        col2.metric("Compound Score", round(compound, 3))

        st.success(f"{emoji} The text sentiment is {sentiment}.")

        st.subheader("Sentiment Scores")

        score_data = pd.DataFrame({
            "Sentiment": ["Positive", "Neutral", "Negative"],
            "Score": [
                scores["pos"],
                scores["neu"],
                scores["neg"]
            ]
        })

        st.bar_chart(
            score_data.set_index("Sentiment")
        )

        st.subheader("Detailed Scores")
        st.dataframe(score_data, use_container_width=True)

    else:
        st.warning("Please enter some text first.")

st.divider()

st.subheader("Try Sample Reviews")

samples = [
    "This product is amazing and I love it!",
    "The service is very bad and disappointing.",
    "The product is okay and works normally."
]

for sample in samples:
    st.write("•", sample)

st.caption("Powered by Python and VADER Sentiment Analysis.")
