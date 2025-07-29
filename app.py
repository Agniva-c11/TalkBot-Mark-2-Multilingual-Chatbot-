import os
import csv
import datetime
import streamlit as st

from utils.translator import detect_language, translate_to_english, translate_from_english
from utils.chatbot_core import get_response

counter = 0

def main():
    global counter
    st.title("TalkBot Mark-2 (Multilingual Chatbot)")

    menu = ["Home", "Conversation History", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("You can now talk in any language. I'll respond in the same")

        if not os.path.exists("chat_log.csv"):
            with open('chat_log.csv', 'w', newline = '', encoding = 'utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['User Input', 'Language', 'Translated Input', 'Chatbot Response', 'Timestamp'])

            
        counter += 1
        user_input = st.text_input("You:", key = f"user_input_{counter}")

        if user_input:
            # Detect Language
            lang = detect_language(user_input)
            translated_input = translate_to_english(user_input)

            # Get responsen in english
            english_response = get_response(translated_input)

            # Translate response back to user's language
            translated_response = translate_from_english(english_response, lang)

            # Show bot response
            st.text_area("Chatbot:", value = translated_response, height = 120, key = f"chatbot_response_{counter}")

            # save to csv
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log_.csv', 'a', newline = '', encoding = 'utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([user_input, lang, translated_input, translated_response, timestamp])
    elif choice == "Conversation History":
        st.header("Chat History")

        if not os.path.exists('chat_log.csv'):
            st.warning("No conversation history found yet.")
        else:
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)
                if not headers:
                    st.warning("Chat log is empty.")
                else:
                    for row in reader:
                        if len(row) >= 5:
                            st.markdown(f"**User ({row[1]}):** {row[0]}")
                            st.markdown(f"**Bot ({row[1]}):** {row[3]}")
                            st.markdown(f"*Timestamp:* {row[4]}")
                            st.markdown("---")

    elif choice == "About":
        st.write("### Multilingual NLP Chatbot")
        st.markdown("""
        This chatbot understands any language and replies back in the same.
        It uses:
        - Logistic Rregression for intent classification
        - 'langdetect' to detect language
        - 'deep_translator' to translate
        -  Streamlit for web interface
        """)

if __name__ == '__main__':
    main()