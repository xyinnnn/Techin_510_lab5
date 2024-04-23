import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import json

# Set your Gemini API key and API secret
API_KEY = 'your_gemini_api_key'


def get_gemini_price():
    """Fetch the current price of Bitcoin from Gemini."""
    url = "https://api.gemini.com/v1/pubticker/btcusd"
    response = requests.get(url, auth=HTTPBasicAuth(API_KEY))
    if response.status_code == 200:
        data = response.json()
        return data['last']
    else:
        return "API Error"

# Streamlit UI setup
st.title('Resume and Crypto Market Coach')
st.write("This app helps tailor your resume based on job descriptions and keeps you updated with the latest Bitcoin price from Gemini.")

# Displaying Bitcoin price
bitcoin_price = get_gemini_price()
st.header(f"Current Bitcoin Price: ${bitcoin_price}")

# Text areas for job description and resume
job_description = st.text_area("Enter the job description here:", height=150)
user_resume = st.text_area("Paste your resume here:", height=150)

if st.button('Analyze Resume'):
    if job_description and user_resume:
        # Assuming you implement a function that analyzes the resume
        # results = analyze_resume(job_description, user_resume)
        # For demo, let's just echo inputs
        st.subheader("Analysis Results:")
        st.write("### Job Description:")
        st.write(job_description)
        st.write("### Your Resume:")
        st.write(user_resume)
        st.write("Implement actual resume analysis logic here.")
    else:
        st.error("Please fill in both fields to perform the analysis.")
