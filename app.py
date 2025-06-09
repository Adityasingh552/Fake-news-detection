import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit App UI
st.title("📰 Fake News Detection App")

st.write("Enter a news article or headline to check whether it's **Fake** or **Real**.")

user_input = st.text_area("📝 Enter News Text Here:")

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]

        if prediction == 1:
            st.success("✅ This looks like **Real News**.")
        else:
            st.error("❌ This might be **Fake News**.")
