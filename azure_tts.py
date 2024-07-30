import time
from azure.cognitiveservices.speech import AudioDataStream, SpeechSynthesizer, SpeechConfig, SpeechSynthesisOutputFormat

class AzureTTS:
    def __init__(self, subscription_key, region):
        self.speech_config = SpeechConfig(subscription=subscription_key, region=region)
        self.speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff16Khz16BitMonoPcm)

    def generate_ssml(self, start_time, end_time, text, voice, style):
        duration = end_time - start_time
        words_per_minute = 160 # Average speaking rate
        num_words = len(text.split())
        actual_duration = (num_words / words_per_minute) * 60  # in seconds
        speaking_rate = actual_duration / duration

        ssml = f'''
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
            <voice name="{voice}">
                <mstts:express-as style="{style}">
                    <prosody rate="{speaking_rate:.2f}">{text}</prosody>
                </mstts:express-as>
            </voice>
        </speak>
        '''
        return ssml

    def synthesize_ssml_to_speech(self, ssml):
        synthesizer = SpeechSynthesizer(speech_config=self.speech_config)
        result = synthesizer.speak_ssml_async(ssml).get()
        audio_stream = AudioDataStream(result)
        return audio_stream

    def save_audio_stream_to_file(self, audio_stream, start_time, end_time):
        audio_file = f'{int(time.time())}_speech_{start_time}_{end_time}.wav'  # Unique filename based on timestamp
        audio_stream.save_to_wav_file(audio_file)
        return audio_file
