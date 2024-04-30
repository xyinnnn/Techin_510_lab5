import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API with the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Define the prompt template for the travel plans
prompt_template = """
You are an expert at planning overseas trips.

Please take the user's request and plan a comprehensive trip for them.

Please include the following details:
- The destination
- The duration of the trip
- The activities that will be done
- The accommodation

The user's request is:
{prompt}
"""

# Function to generate content based on a user's prompt using the configured AI model
def generate_content(user_prompt):
    complete_prompt = prompt_template.format(prompt=user_prompt)
    response = model.generate_content(complete_prompt)
    if len(response.candidates[0].content.parts) > 0:
        return response.candidates[0].content.parts[0].text
    else: 
        return response.text

# Streamlit UI setup
st.title("🌏 Travel Planner")
st.write("Enter your travel preferences and receive a customized travel plan!")

prompt = st.text_area("Enter where you want to go and any specific preferences you have:", height=150)
if st.button("Generate Travel Plan"):

    reply = generate_content(prompt)
    try:
        reply = generate_content(prompt)
        st.write(reply)
        if isinstance(reply, str) and (reply.startswith("Error") or reply.startswith("Invalid")):
            st.error(reply)
        else:
            st.success("Here's your travel plan:")
            st.write(reply)
    except Exception as e:
        st.error(f"Failed to generate travel plan: {str(e)}")





