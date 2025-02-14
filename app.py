import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
import time  # Importar time para el timestamp

from transcriber import Transcriber
from llm import LLM
from weather import Weather
from tts import TTS
from pc_command import PcCommand

# Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    # Obtener audio grabado y transcribirlo
    audio = request.files.get("audio")
    text = Transcriber().transcribe(audio)
   
    # Utilizar el LLM para ver si llamar una función
    llm = LLM()
    function_name, args, message = llm.process_functions(text)
    if function_name is not None:
        # Si se desea llamar una función de las que tenemos
        if function_name == "get_weather":
            # Llamar a la función del clima
            function_response = Weather().get(args["ubicacion"])
            function_response = json.dumps(function_response)
            print(f"Respuesta de la función: {function_response}")
           
            final_response = llm.process_response(text, message, function_name, function_response)
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
       
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

        elif function_name == "control_led":
            PcCommand().control_led(args["state"])
            final_response = f"Listo, el LED está {args['state']}"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "read_temperature":
            temperature_response = PcCommand().read_temperature()
            final_response = temperature_response
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "example_buzzer":
            # Llamar a la función para mostrar el código del buzzer
            with open("buzzer.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo de Buzzer"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}

    else:
        final_response = "Eso no está relacionado con Raspberry Pi"
        tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
        return {"result": "ok", "text": final_response, "file": tts_file}