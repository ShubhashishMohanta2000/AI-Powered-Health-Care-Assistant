import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="config/.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for dark-themed UI and background
st.markdown("""
    <style>
        /* Global styles */
        .main {
            background-image: url('https://images.unsplash.com/photo-1585435557343-3b092031a831?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            padding: 30px;
            border-radius: 12px;
            min-height: 100vh;
            position: relative;
        }
        .main::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(30, 34, 41, 0.9); /* Dark overlay for readability */
            border-radius: 12px;
        }
        .stApp {
            background: transparent;
        }
        h1 {
            color: #4fc3f7;
            font-family: 'Inter', 'Arial', sans-serif;
            text-align: center;
            margin-bottom: 25px;
            font-size: 2.8em;
            font-weight: 700;
        }
        .stTextArea textarea {
            border: 2px solid #4fc3f7;
            border-radius: 10px;
            padding: 14px;
            font-size: 16px;
            background-color: #2a2f38;
            color: #e0e0e0;
            box-shadow: 0 3px 6px rgba(0,0,0,0.2);
            transition: border-color 0.3s;
        }
        .stTextArea textarea:focus {
            border-color: #0288d1;
        }
        .stButton>button {
            background-color: #0288d1;
            color: white;
            border-radius: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            transition: background-color 0.3s, transform 0.2s;
        }
        .stButton>button:hover {
            background-color: #01579b;
            transform: translateY(-2px);
        }
        .stSidebar {
            background-color: rgba(40, 44, 52, 0.95);
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .stSidebar h2 {
            color: #4fc3f7;
            font-family: 'Inter', 'Arial', sans-serif;
            font-size: 1.8em;
        }
        .stSidebar p, .stSidebar li {
            color: #b0bec5;
            font-size: 14px;
            line-height: 1.6;
        }
        .disclaimer {
            color: #ef5350;
            font-style: italic;
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            background-color: rgba(40, 44, 52, 0.9);
            padding: 12px;
            border-radius: 8px;
        }
        .error {
            color: #ef5350;
            font-weight: bold;
            background-color: rgba(40, 44, 52, 0.9);
            padding: 12px;
            border-radius: 8px;
        }
        .stMarkdown p {
            color: #e0e0e0;
            font-size: 16px;
            line-height: 1.6;
            background-color: rgba(40, 44, 52, 0.9);
            padding: 12px;
            border-radius: 8px;
        }
        hr {
            border: 1px solid #546e7a;
            margin: 20px 0;
        }
        /* Ensure placeholder text is visible */
        .stTextArea textarea::placeholder {
            color: #90a4ae;
        }
    </style>
""", unsafe_allow_html=True)

# App title and subtitle
st.title("AI-Powered Medical Assistant")
st.markdown("Describe your symptoms below to receive AI-generated suggestions for medicines and precautions.")

# Sidebar content
with st.sidebar:
    st.header("About")
    st.markdown("""
        **AI-Powered Medical Assistant** is a web app powered by Google's Gemini AI. It provides suggestions for medicines and precautions based on your symptoms. 
        This is a prototype for educational purposes and not a substitute for professional medical advice.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Credits")
    st.markdown("""
        - Built with Streamlit
        - Powered by Google Gemini API
    """)

# Main content
symptoms = st.text_area("Describe your symptoms:", placeholder="E.g., I have a fever, cough, and feel tired, etc.", height=150)

if st.button("Get Suggestions"):
    if symptoms.strip() == "":
        st.markdown('<p class="error">Please enter your symptoms.</p>', unsafe_allow_html=True)
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

            st.markdown(result, unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f'<p class="error">An error occurred: {str(e)}</p>', unsafe_allow_html=True)

# Disclaimer
st.markdown("""
    <p class="disclaimer">
        Disclaimer: This app provides suggestions for educational purposes only. 
        Always consult a qualified healthcare professional for medical advice and diagnosis.
    </p>
""", unsafe_allow_html=True)