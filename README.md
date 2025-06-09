# Fake-News-Detection-Machine-Learning

# 📰 Fake News Detection Web App

This is a **machine learning-powered web app** built using **Streamlit** that predicts whether a given news article is **fake** or **real**.

---

## 💡 Overview

The app uses:
- Natural Language Processing (NLP)
- Logistic Regression for classification
- TF-IDF vectorization
- Google Drive integration for dataset loading

---

## 📁 Dataset Source

The dataset (`train.csv`) is loaded directly from **Google Drive** to avoid GitHub's 25MB file size limit.

- 🔗 **Google Drive Dataset Link**: [Download train.csv](https://drive.google.com/uc?export=download&id=1sMnZbqBl0sCVU6UZ4BSRGnYUOFwt_0L4)

# In app.py  
url = 'https://drive.google.com/uc?export=download&id=1sMnZbqBl0sCVU6UZ4BSRGnYUOFwt_0L4'
news_df = pd.read_csv(url)


🚀 How to Run

Step 1: Clone the Repository
        git clone https://github.com/your-username/fake-news-detector.git
        cd fake-news-detector

Step 2: Install Dependencies
        pip install -r requirements.txt

Step 3: Run the App
        streamlit run app.py
        
Make sure you are connected to the internet so the dataset and NLTK resources can load.


🧠 Model Details
. Model: Logistic Regression
. Feature Extraction: TF-IDF Vectorizer
. Text Cleaning: Lowercasing, punctuation removal, stopword removal, stemming (Porter Stemmer)
. Evaluation: Accuracy score

🛠 Troubleshooting
. ModuleNotFoundError: No module named 'nltk': Run pip install nltk
. LookupError: stopwords not found: Add nltk.download('stopwords') to your code
. train.csv not found: Ensure your internet is working and the URL is valid

✅ Sample Inputs
Real News:
Pfizer COVID-19 vaccine shows 95% efficacy in Phase 3 trials.

Fake News:
NASA confirms Earth will go dark for six days in December 2025.


Accessable Link:- https://fake-news-detection-94jqtzk8gfw3wn2kwq9b7w.streamlit.app/
