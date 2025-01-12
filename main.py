import entree
import processing
import sortie

# Charger le modèle GPT-2
modele, tokenizer = load_model()

while True:
    # Écouter l'entrée vocale
    audio = listening()
    input_text = ""

    try:
        input_text = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : {}".format(input_text))
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError as e:
        print("Erreur lors de la requête à l'API de reconnaissance vocale ; {0}".format(e))

    if input_text.lower() == "stop":
        print("Arrêt du chatbot.")
        break

    # Générer une réponse
    reponse = generate_text(modele, tokenizer, input_text)
    speak("Chatbot : {}".format(reponse))