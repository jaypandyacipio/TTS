import streamlit as st
import json
from azure_tts import AzureTTS
from voice_styles import VoiceStyles
from tts_generator import TTSGenerator

# Azure TTS subscription key and region
subscription_key = 'f74fe7fc6f6a48879e486a5b33e1653d'
region = 'westus'

# Initialize the TTS generator
tts_generator = TTSGenerator(subscription_key, region)

# Streamlit UI
st.title('Text-to-Speech Generator')

# Input field for captions
captions_input = st.text_area('Enter the captions as JSON', height=200)

# Dropdown menu for selecting voice
selected_voice = st.selectbox('Select Voice', VoiceStyles.get_voices())

# Check if the selected voice supports styles
style_supported = VoiceStyles.is_style_supported(selected_voice)

# Dropdown menu for selecting style based on selected voice
selected_style = None
if style_supported:
    selected_style = st.selectbox('Select Speaking Style', VoiceStyles.get_styles_for_voice(selected_voice))
else:
    st.text('This voice does not support specific styles.')

# Button to generate speech
generate_button = st.button('Generate Speech')

# Function to display generated audio
def display_generated_audio(audio_file):
    with open(audio_file, 'rb') as f:
        st.download_button(
            label=f'Download {audio_file}',
            data=f,
            file_name=audio_file,
            mime='audio/mp3'
        )
    st.success(f'Generated speech saved to: {audio_file}')

# Generate speech for all segments if button is clicked
if generate_button:
    try:
        captions = json.loads(captions_input)
        if style_supported and not selected_style:
            st.error('Please select a speaking style.')
        else:
            combined_audio_file = tts_generator.generate_tts_for_segments(captions_input, selected_voice, selected_style)
            if combined_audio_file:
                display_generated_audio(combined_audio_file)
    except json.JSONDecodeError:
        st.error('Invalid JSON format. Please enter the captions as valid JSON.')
    except Exception as e:
        st.error(f'An error occurred: {e}')
