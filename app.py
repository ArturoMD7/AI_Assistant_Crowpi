import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
import time  # Importar time para el timestamp
from transcriber import Transcriber
from llm import LLM
from tts import TTS
from pc_command import PcCommand
from gpiozero import DistanceSensor
import subprocess
import time
from flask import Flask, render_template, request, redirect
from OpenSSL import SSL
import ssl

# Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="/etc/ssl/certs/apache.crt", keyfile="/etc/ssl/private/apache.key")
"""
@app.route("/start-flask")
def start_flask():
    subprocess.Popen(["python3", "/srv/http/github/AI_Assistant_Crowpi/start_flask_app.py"])
    return redirect("https://192.168.1.95:5000")
"""
@app.route("/")
def index():
    return render_template("recorder.html")

@app.route('/audio', methods=['POST'])
def audio():
    try:
        # Obtener audio grabado y transcribirlo
        audio = request.files.get("audio")
        text = Transcriber().transcribe(audio)
        print(f"Texto transcrito: {text}")

        # Utilizar el LLM para ver si llamar una función
        llm = LLM()
        function_name, args, message = llm.process_functions(text)

        if function_name is not None:
            if function_name == "show_commands":
                with open("examples/commands.txt", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes mis comandos disponibles"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}

            elif function_name == "presentation" or function_name == "nombre":
                final_response = "¡Hola! Soy GAMA, tu compañero de aprendizaje en el mundo de la CrowPi."
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}

            elif function_name == "example_buzzer":
                with open("examples/buzzer.py", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes el ejemplo de Buzzer"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}

            elif function_name == "open_chrome":
                PcCommand().open_chrome(args["website"])
                final_response = "Listo, ya abrí Chrome en el sitio " + args["website"]
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}

            elif function_name == "open_epiphany":
                PcCommand().open_epiphany(args["website"])
                final_response = "Listo, ya abrí Epiphany en el sitio " + args["website"]
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}

            elif function_name == "open_terminal":
                PcCommand().open_terminal()
                final_response = "Listo, ya abrí la terminal"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}


            elif function_name == "example_buzzer":
                # Llamar a la función para mostrar el código del buzzer
                with open("examples/buzzer.py", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes el ejemplo de Buzzer"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
            
            elif function_name == "example_button_buzzer":
                # Llamar a la función para mostrar el código del buzzer
                with open("examples/button_buzzer.py", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes el ejemplo de Buzzer con boton"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
            
            elif function_name == "example_relay":
                # Llamar a la función para mostrar el código del buzzer
                with open("examples/relay.py", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes el ejemplo de Relay"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
            
            elif function_name == "example_vibration":
                # Llamar a la función para mostrar el código del vibrador
                with open("examples/vibration.py", "r") as file:
                    code_content = file.read()
                final_response = "Aquí tienes el ejemplo de Vibration"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}

            elif function_name == "read_distance":
                distance_response = PcCommand().read_distance()
                final_response = distance_response
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}
            
            elif function_name == "use_buzzer":
                PcCommand().use_buzzer()
                final_response = "Listo, Se hizo sonar el buzzer"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}
                
            elif function_name == "use_matrix":
                PcCommand().use_matrix()
                final_response = "Listo, Mensaje mostrado en la matriz"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}
            
            elif function_name == "use_lcd":
                PcCommand().use_lcd()
                final_response = "Listo, Mensaje mostrado en la pantalla lcd"
                tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
                return {"result": "ok", "text": final_response, "file": tts_file}

        else:
            final_response = "Eso no está relacionado con Crowpi"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

    except Exception as e:
        print(f"Error en el procesamiento de audio: {str(e)}")
        return {"result": "error", "text": "Hubo un problema procesando tu solicitud.", "error": str(e)}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=context)
