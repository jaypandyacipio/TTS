class VoiceStyles:
    voices_and_styles = {
        'de-DE-ConradNeural': ['cheerful'],
        'en-GB-RyanNeural': ['chat', 'cheerful'],
        'en-GB-SoniaNeural': ['cheerful', 'sad'],
        'en-IN-NeerjaNeural': ['cheerful', 'empathetic', 'newscast'],
        'en-US-AriaNeural': ['angry', 'chat', 'cheerful', 'customerservice', 'empathetic', 'excited', 'friendly', 'hopeful', 'narration-professional', 'newscast-casual', 'newscast-formal', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-DavisNeural': ['angry', 'chat', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-GuyNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'newscast', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-JaneNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-JasonNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-JennyNeural': ['angry', 'assistant', 'chat', 'cheerful', 'customerservice', 'excited', 'friendly', 'hopeful', 'newscast', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-KaiNeural': ['conversation'],
        'en-US-LunaNeural': ['conversation'],
        'en-US-NancyNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-SaraNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-TonyNeural': ['angry', 'cheerful', 'excited', 'friendly', 'hopeful', 'sad', 'shouting', 'terrified', 'unfriendly', 'whispering'],
        'en-US-AvaMultilingualNeural': ['Conversation', 'Conversation with interjection', 'Meditation', 'News', 'Poem'],
        'en-US-AndrewMultilingualNeural': ['Conversation', 'Conversation with interjection', 'Advertisement', 'News', 'Story'],
        'en-US-EmmaMultilingualNeural': ['Conversation', 'Conversation with interjection', 'e-learning', 'News'],
        'en-US-BrianMultilingualNeural': ['Conversation', 'Conversation with interjection', 'Story', 'Advertisement']
    }

    @classmethod
    def get_voices(cls):
        return list(cls.voices_and_styles.keys())

    @classmethod
    def get_styles_for_voice(cls, voice):
        return cls.voices_and_styles.get(voice, [])
    
    @classmethod
    def is_style_supported(cls, voice):
        return bool(cls.voices_and_styles.get(voice, []))
