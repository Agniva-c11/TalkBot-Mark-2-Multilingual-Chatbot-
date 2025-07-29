# 🗣️ TalkBot Mark-2 — Multilingual Chatbot using NLP & Streamlit

This project is a **language-aware chatbot** that allows users to interact in **any language** and receive responses in the **same language**. It uses **machine learning-based intent classification** along with **language detection and translation** to support multilingual communication through a clean and interactive **Streamlit** web interface.

---
# Live Demo

🚀 Try the chatbot live here:  
👉TalkBot Mark-2 Streamlit App : (https://g66gdbmmatazkcam3usgwx.streamlit.app/)

## 📌 Project Structure

- `app.py` – Main Streamlit app with sidebar navigation, multilingual chat, and conversation history.
- `main.ipynb` – Jupyter notebook version for testing and training the chatbot.
- `intents.json` – Intent patterns and responses used to train the chatbot.
- `chat_log.csv` – Automatically stores all conversation logs with language, timestamps, and responses.
- `requirements.txt` – All dependencies to run the project.
- `utils/`
  - `chatbot_core.py` – Model training and prediction logic using Tfidf and Logistic Regression.
  - `translator.py` – Language detection and bi-directional translation using Deep Translator.

---

## 🚀 Features

- Supports **any human language** (e.g., Bengali, Hindi, Spanish, French, etc.)
- Detects user's language automatically and responds in the **same language**
- Uses **TfidfVectorizer + LogisticRegression** for intent classification
- Includes **Streamlit interface** for user-friendly interaction
- Stores **chat history with language and timestamp**
- Easy to extend with more intents via `intents.json`

---

## 🧠 NLP Model Details

- **Vectorization** – Uses TF-IDF to convert input text into feature vectors
- **Classification Model** – Trained Logistic Regression classifier to predict user intent
- **Training Data** – Sourced from `intents.json` file with labeled intent patterns and responses

---

## 🌐 Language Intelligence

- **Language Detection** – Implemented using `langdetect`
- **Translation Engine** – Powered by `deep-translator` with Google Translate backend
- User input is auto-translated to English for processing, then responses are translated back to the **original language**

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
