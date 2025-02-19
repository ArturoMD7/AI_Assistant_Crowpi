import os
from dotenv import load_dotenv
import requests

# Texto a voz. Implementación con ElevenLabs
class TTS():
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('ELEVENLABS_API_KEY')
    
    def process(self, text, filename="response.mp3"):
        CHUNK_SIZE = 1024
        # URL de la API de ElevenLabs (usando la voz específica de Bella)
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.55
            }
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.status_code)
        print(response.text) 

        # Asegurar que la carpeta "static" existe
        os.makedirs("static", exist_ok=True)

        # Guardar el archivo con el nombre especificado
        file_path = os.path.join("static", filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        return filename  # Retorna el nombre del archivo generado
