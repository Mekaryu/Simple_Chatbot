import entree
import processing
import sortie

# Charger le modèle GPT-2
    modele, tokenizer = charger_modele()

    while True:
        # Écouter l'entrée vocale
        audio = ecouter_micro()
        texte_entree = ""

        try:
            texte_entree = recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit : {}".format(texte_entree))
        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio")
        except sr.RequestError as e:
            print("Erreur lors de la requête à l'API de reconnaissance vocale ; {0}".format(e))

        if texte_entree.lower() == "stop":
            print("Arrêt du chatbot.")
            break

        # Générer une réponse
        reponse = generer_texte(modele, tokenizer, texte_entree)
        prononcer_texte.("Chatbot : {}".format(reponse))