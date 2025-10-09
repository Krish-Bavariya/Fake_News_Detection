# 📰 Fake News Detection App 🧠  
*A Machine Learning-powered Web App built with Python & Streamlit*

---

## 🌟 Overview  
In today’s digital world, misinformation spreads faster than ever.  
This **Fake News Detection App** uses **Machine Learning (ML)** and **Natural Language Processing (NLP)** to identify whether a news article is **Real** or **Fake** based on its text content.

Built with **Python**, **Scikit-learn**, and **Streamlit**, the app provides a simple, elegant interface where users can type or paste a news article and instantly get predictions powered by AI.

---

## 🎯 Key Features  

✅ **User-friendly Streamlit interface** — no coding required  
✅ **Real-time detection** of fake news  
✅ **Machine Learning model (Logistic Regression)** trained on real datasets  
✅ **TF-IDF Vectorization** for text representation  
✅ **Customizable preprocessing pipeline** for clean text analysis  
✅ **Fast, lightweight, and deployable on the web (Streamlit Cloud, Hugging Face, etc.)**

---

## 🧠 How It Works  

1. The model is trained on two datasets:
   - **True.csv** → Real news articles  
   - **Fake.csv** → Fake or misleading articles  

2. The text is **preprocessed** (cleaned, lowercased, punctuation removed, etc.)  

3. A **TF-IDF Vectorizer** converts text into numerical features  

4. A **Logistic Regression model** classifies each input as:
   - 🟢 **Real News**
   - 🔴 **Fake News**

---
