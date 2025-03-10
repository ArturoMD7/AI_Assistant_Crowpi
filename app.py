import os
import openai
import sys
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
import time  # Importar time para el timestamp
from transcriber import Transcriber
from llm import LLM
from tts import TTS
from pc_command import PcCommand

import time

if sys.platform.startswith("linux"):  # Si es Raspberry Pi
    from gpiozero import DistanceSensor 
      

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
        if function_name == "show_commands":
            # Llamar a la función para mostrar el código del vibrador
            with open("examples/commands.txt", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes mis comandos disponibles"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
       
        elif function_name == "presentation" or function_name == "nombre":
            final_response = "¡Hola! Soy GAMA, tu compañero de aprendizaje en el mundo de la CrowPi. Estoy aquí para enseñarte, guiarte y hacer que la electrónica y la programación sean más fáciles y divertidas."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "commands":
            # Llamar a la función para mostrar el código del vibrador
            with open("examples/commands.txt", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes la lista de mis comandos disponibles"
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
        
        elif function_name == "read_temperature":
            distance_response = PcCommand().read_temperature()
            final_response = distance_response
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        
        elif function_name == "use_buzzer":
            PcCommand().use_buzzer()
            final_response = "Listo, Se hizo sonar el buzzer"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "led_on":
            PcCommand().led_on()
            final_response = "Listo, Se encendio el led"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
            
        elif function_name == "led_off":
            PcCommand().led_off()
            final_response = "Listo, Se apago el led"
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
        
        elif function_name == "use_servomotor":
            PcCommand().use_servomotor()
            final_response = "Listo, se ah usado el servmomotor"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "show_hour":
            PcCommand().show_hour()
            final_response = "Listo, ya te mostre la hora"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "example_blinking_led":
            with open("examples/blinking_led.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo del led parpadeante"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_light_sensor":
            with open("examples/light_sensor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo de sensor de luz"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_dht_sensor":
            with open("examples/dht_sensor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para medir la temperatura y humedad"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_motion_sensor":
            with open("examples/motion_sensor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para detectar la inclinacion"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_distancia_sensor":
            with open("examples/distancia_sensor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para medir la distancia"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_screen_lcd":
            with open("examples/screen_lcd.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para mostrar texto en la pantalla LCD"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_stepmotor":
            with open("examples/stepmotor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para que funcione el stepmotor"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_servomotor":
            with open("examples/servomotor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para que funcione el servomotor"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_matrix":
            with open("examples/matrix.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para la matrix"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_segment":
            with open("examples/segment.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para controlar el display"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_touch_sensor":
            with open("examples/touch_sensor.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para el sensor touch"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_tilt":
            with open("examples/tilt.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para el movimiento del dispositivo"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_button_matrix":
            with open("examples/button_matrix.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para la matriz de teclas"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "example_remote_controller":
            with open("examples/remote_controller.py", "r") as file:
                code_content = file.read()
            final_response = "Aquí tienes el ejemplo para usar el control remoto"
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file, "code": code_content}
        
        elif function_name == "info_ultrasonico":
            final_response = "El sensor ultrasónico se utiliza para medir distancias. Emite ondas sonoras y calcula la distancia basándose en el tiempo que tarda en recibir el eco."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_temperatura":
            final_response = "El sensor de temperatura mide la temperatura ambiente en grados Celsius o Fahrenheit."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_humedad":
            final_response = "El sensor de humedad mide la cantidad de vapor de agua en el aire, expresada como un porcentaje."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_luz":
            final_response = "El sensor de luz detecta la intensidad de la luz en el ambiente. Puede usarse para ajustar el brillo de una pantalla o encender luces automáticamente."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_movimiento":
            final_response = "El sensor de movimiento (PIR) detecta cambios en la radiación infrarroja, lo que le permite detectar movimiento."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_led":
            final_response = "Los LEDs son componentes que emiten luz cuando se les aplica corriente. Pueden ser de un solo color o RGB (rojo, verde, azul)."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "info_camara":
            final_response = "La cámara permite capturar imágenes o videos. Puede usarse para vigilancia, reconocimiento facial o proyectos de visión por computadora."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "info_microfono":
            final_response = "El micrófono captura sonido y lo convierte en señales eléctricas. Puede usarse para grabación de audio o comandos de voz."
            tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
            return {"result": "ok", "text": final_response, "file": tts_file}

    else:
        final_response = "Eso no está relacionado con Crowpi"
        tts_file = TTS().process(final_response, filename=f"response_{int(time.time())}.mp3")
        return {"result": "ok", "text": final_response, "file": tts_file}