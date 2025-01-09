import entree
import sortie

audio = entree.ecouter_micro()
if audio:
    texte_transcrit = entree.transcrire_audio(audio)
    if texte_transcrit:
        # Vous pouvez utiliser le texte_transcrit comme vous le souhaitez ici
        sortie.prononcer_texte(texte_transcrit)
    else:
        print("La transcription a échoué.")
else:
    print("Aucun audio n'a été détecté.")