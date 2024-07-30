import json
from azure_tts import AzureTTS
from voice_styles import VoiceStyles

class TTSGenerator:
    def __init__(self, subscription_key, region):
        self.azure_tts = AzureTTS(subscription_key, region)
        
    def generate_tts_for_segments(self, captions_json, voice, style):
        audio_files = []
        try:
            captions = json.loads(captions_json)
            for segment in captions:
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text']

                ssml = self.azure_tts.generate_ssml(start_time, end_time, text, voice, style)
                audio_stream = self.azure_tts.synthesize_ssml_to_speech(ssml)
                audio_file = self.azure_tts.save_audio_stream_to_file(audio_stream, start_time, end_time)
                audio_files.append(audio_file)
                print(f'Generated speech for segment: "{text}" saved to: {audio_file}')
        except json.JSONDecodeError:
            print('Invalid JSON format. Please enter the captions as valid JSON.')
        except Exception as e:
            print(f'An error occurred: {e}')
        
        return audio_files

# Example usage (for non-Streamlit use cases)
if __name__ == "__main__":
    subscription_key = 'f74fe7fc6f6a48879e486a5b33e1653d'
    region = 'westus'
    captions_input = '[{"start": 0, "end": 5, "text": "Hello, world!"}]'  # Example JSON input
    selected_voice = 'en-US-AriaNeural'
    selected_style = 'cheerful'

    tts_generator = TTSGenerator(subscription_key, region)
    tts_generator.generate_tts_for_segments(captions_input, selected_voice, selected_style)
