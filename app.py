import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config/.env")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


st.title("AI-Powered Medical Assistant")
st.write("Enter your symptoms to receive AI-generated suggestions for possible medicines and precautions.")

with st.sidebar:
    st.header("About")
    st.write("""
        **AI-Powered Medical Assistant** is a web app that uses Google's Gemini AI to suggest possible medicines and precautions based on your symptoms. 
        This is a prototype for educational purposes and not a substitute for professional medical advice.
        """)
    st.subheader("Credits")
    st.write("Developed using Streamlit and Google Gemini API.")

symptoms = st.text_area("Describe your symptoms:", placeholder="E.g., I have a fever, cough, and feel tired, etc.")

if st.button("Get Suggestions"):
    if symptoms.strip() == "":
        st.error("Please enter your symptoms.")
    else:
        try:
            prompt = f"""
            I am a medical assistant AI. Based on the following symptoms, suggest possible medicines and precautions. 
            Format the response clearly with sections for Medicines and Precautions. 
            Include a note that this is not professional medical advice and the user should consult a doctor.
            Symptoms: {symptoms}
            """

            response = model.generate_content(prompt)
            result = response.text

            st.write(result)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.write(
    "Disclaimer: This app provides suggestions for educational purposes only. Always consult a qualified healthcare professional for medical advice and diagnosis."
)