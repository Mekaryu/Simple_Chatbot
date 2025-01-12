import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import speech_recognition as sr

def load_model():
    # Charger le modèle GPT-2
    modele = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return modele, tokenizer

def generate_text(modele, tokenizer, entree_texte):
    entree_ids = tokenizer.encode(entree_texte, return_tensors="pt")
    sortie_ids = modele.generate(entree_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    reponse_texte = tokenizer.decode(sortie_ids[0], skip_special_tokens=True)
    return reponse_texte

def listen_mic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    return audio

if __name__ == "__main__":
    # Charger le modèle GPT-2
    modele, tokenizer = load_model()

    while True:
        # Écouter l'entrée vocale
        audio = listen_mic()
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
        reponse = generate_text(modele, tokenizer, texte_entree)
        print("Chatbot : {}".format(reponse))