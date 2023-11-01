# azure.py
# Import necessary libraries
import streamlit as st
import openai
import os
import music_gen  # Import your music generation module

# Set up your OpenAI API key
openai.api_key = os.environ.get('Bruce_Ai_Key')

# Initialize Streamlit
st.title("Hi! I am Bruce Almighty!")

# Add a slider to control the temperature
temperature = st.slider('Temperature', min_value=0.0, max_value=1.0, value=0.7, step=0.05)
st.write(f'You selected a temperature of: {temperature}')

# Create a text input field for user queries
user_input = st.text_input("Let me generate the perfect music for you and your situation. What mood are you currently in?:")

# Send the user's query to OpenAI GPT-3
if user_input:
    # Replace OpenAI GPT-3 call with your music generation function
    generated_music = music_gen.generate_music(user_input, temperature)
    st.write(generated_music)
