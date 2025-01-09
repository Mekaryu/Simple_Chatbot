import pyttsx3

def prononcer_texte(texte):
    engine = pyttsx3.init()

    # Vous pouvez ajuster la vitesse de la voix (par défaut=200)
    engine.setProperty('rate', 150)

    # Vous pouvez ajuster le volume de la voix (par défaut=1.0)
    engine.setProperty('volume', 1.0)

    engine.say(texte)
    engine.runAndWait()

prononcer_texte("Bonjour")

"""
if __name__ == "__main__":
    texte_a_prononcer = input("Entrez la chaîne de caractères à prononcer : ")
    prononcer_texte(texte_a_prononcer)"""