import pyttsx3

def speak(texte):
    engine = pyttsx3.init()

    # voice speed (default=200)
    engine.setProperty('rate', 150)

    # volume (default=1.0)
    engine.setProperty('volume', 1.0)

    engine.say(texte)
    engine.runAndWait()

speak("Bonjour")

"""
if __name__ == "__main__":
    text = input("Entrez la chaîne de caractères à prononcer : ")
    speak(text)"""