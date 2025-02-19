import openai

#Convertir audio en texto
class Transcriber:
    def __init__(self):
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def transcribe(self, audio):
        audio.save("audio.mp3")
        audio_file = open("audio.mp3", "rb")
        print("Archivo de audio guardado y listo para transcribir")  # Depuración
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        print("Texto transcrito:", transcript.text)  # Depuración
        return transcript.text
