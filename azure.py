# azure.py
# Import necessary libraries
import subprocess

# Use the subprocess module to run the pip install command
subprocess.check_call(['pip', 'install', 'transformers', 'torch==1.9.1'])

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import note_seq


# Set up your OpenAI API key
# Note: You might want to replace this with the appropriate OpenAI key setup.
# openai.api_key = os.environ.get('Bruce_Ai_Key')

# Initialize Streamlit
st.title("Hi! I am Bruce Almighty!")

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("ai-guru/lakhclean_mmmtrack_4bars_d-2048")
model = AutoModelForCausalLM.from_pretrained("ai-guru/lakhclean_mmmtrack_4bars_d-2048")

# Add a slider to control the temperature
temperature = st.slider('Temperature', min_value=0.0, max_value=1.0, value=0.7, step=0.05)
st.write(f'You selected a temperature of: {temperature}')

# Create a text input field for user queries
user_input = st.text_input("Let me generate the perfect music for you and your situation. What mood are you currently in?:")

# Generate music when user provides input
if user_input:
    # Encode the conditioning tokens.
    generated_sequence = "PIECE_START"
    input_ids = tokenizer.encode(generated_sequence, return_tensors="pt")

    # Generate more tokens.
    eos_token_id = tokenizer.encode("TRACK_END")[0]
    generated_ids = model.generate(
        input_ids,
        max_length=2048,
        do_sample=True,
        temperature=temperature,
        eos_token_id=eos_token_id,
    )
    generated_sequence = tokenizer.decode(generated_ids[0])

    # Convert generated tokens to NoteSequence
    note_sequence = token_sequence_to_note_sequence(generated_sequence)

    # Play the generated music
    synth = note_seq.fluidsynth
    st.audio(note_seq.play_sequence(note_sequence, synth), format="audio/midi")
