import openai
import json

# Clase para utilizar cualquier LLM para procesar un texto
# y regresar una función a llamar con sus parámetros
class LLM():
    def __init__(self):
        pass
   
    def process_functions(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente amable y útil para Raspberry Pi."},
                {"role": "user", "content": text},
            ],
            functions=[

                {
                    "name": "presentation",
                    "description": "El asistente GAMA se presentara",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "nombre",
                    "description": "El asistente GAMA se presentara",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "open_chrome",
                    "description": "Abrir el navegador Chrome en un sitio específico",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "El sitio al cual se desea ir"
                            }
                        }
                    }
                },
                {
                    "name": "open_epiphany",
                    "description": "Abrir el navegador Epiphany en un sitio específico",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "El sitio al cual se desea ir"
                            }
                        }
                    }
                },
                {
                    "name": "open_terminal",
                    "description": "Abrir una terminal en Raspbian",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "control_led",
                    "description": "Encender o apagar un LED conectado al GPIO",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "state": {
                                "type": "string",
                                "description": "El estado del LED (on/off)"
                            }
                        }
                    }
                },
                {
                    "name": "read_temperature",
                    "description": "Leer la temperatura de un sensor DS18B20",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "example_buzzer",
                    "description": "Ejemplo de código para controlar un buzzer",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "example_button_buzzer",
                    "description": "Ejemplo de código para controlar un buzzer con un boton",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "example_relay",
                    "description": "Ejemplo de código del uso de relay",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "example_vibration",
                    "description": "Ejemplo de código del uso de relay",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "read_distance",
                    "description": "Medir la distancia usando el sensor ultrasonico",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                },

                {
                    "name": "commands",
                    "description": "lista de todos los comandos",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            ],
            function_call="auto",
        )
       
        message = response["choices"][0]["message"]
       
        # Verificar si se debe llamar a una función
        if message.get("function_call"):
            function_name = message["function_call"]["name"]
            args = message.to_dict()['function_call']['arguments']
            print("Función a llamar: " + function_name)
            args = json.loads(args)
            return function_name, args, message
       
        return None, None, message
   
    def process_response(self, text, message, function_name, function_response):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "Eres un asistente útil para Raspberry Pi."},
                {"role": "user", "content": text},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        return response["choices"][0]["message"]["content"]