import speech_recognition as sr

def ecouter_micro():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    return audio

def transcrire_audio(audio):
    recognizer = sr.Recognizer()

    try:
        print("Transcription en cours...")
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print("Texte transcrit : {}".format(texte))
        return texte
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
        return None
    except sr.RequestError as e:
        print("Erreur lors de la requête à l'API de reconnaissance vocale ; {0}".format(e))
        return None

if __name__ == "__main__":
    audio = ecouter_micro()
    if audio:
        texte_transcrit = transcrire_audio(audio)
        if texte_transcrit:
            # Vous pouvez utiliser le texte_transcrit comme vous le souhaitez ici
            pass
        else:
            print("La transcription a échoué.")
    else:
        print("Aucun audio n'a été détecté.")