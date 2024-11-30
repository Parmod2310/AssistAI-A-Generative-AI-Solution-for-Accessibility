import pyttsx3

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    audio_path = "assets/text_to_speech.mp3"
    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    
    return audio_path
