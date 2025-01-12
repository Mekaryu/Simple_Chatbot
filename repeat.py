import entree
import sortie

audio = entree.listening()
if audio:
    text = entree.audio_transcription(audio)
    if text:
        sortie.speak(text)
    else:
        print("Transcription failed")
else:
    print("No audio detected")