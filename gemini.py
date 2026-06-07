from google import genai
import os
import time
import streamlit as st

client = genai.Client(api_key=st.secrets["chatbot_key"]["api_key"])


def load_faq():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FAQ_PATH = os.path.join(BASE_DIR, "faq.txt")
    with open(FAQ_PATH, "r", encoding="utf-8") as file:
        return file.read()


def getresponse(prompt, retries=2):

    faq_content = load_faq()

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=f"FAQ:\n{faq_content}\n\n"+prompt
            )
            return response.text
        except genai.errors.ServerError as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)  # wait before retry
    return "Gemini is currently unavailable. Please try again later."

# print(getresponse("Will participating in research affect my current treatment?"))
