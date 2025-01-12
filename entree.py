import speech_recognition as sr

def listening():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    return audio

def audio_transcription(audio):
    recognizer = sr.Recognizer()

    try:
        print("Transcription in progress...")
        text = recognizer.recognize_google(audio, language="fr-FR")
        print("Transcripted text: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Impossible to understand voice")
        return None
    except sr.RequestError as e:
        print("API Error; {0}".format(e))
        return None

if __name__ == "__main__":
    audio = listening()
    if audio:
        texte_transcrit = audio_transcription(audio)
        if texte_transcrit:
            # Use transcripted text here
            pass
        else:
            print("Transcription failed")
    else:
        print("No audio detected")