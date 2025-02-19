import subprocess
"""
venv_path = "/srv/http/github/AI_Assistant_Crowpi/crowpi-venv/bin/activate"
app_path = "/srv/http/github/AI_Assistant_Crowpi/app.py"

# Ejecutar el comando en un solo shell, activando el virtualenv y ejecutando el script
cmd = f"source {venv_path} && python {app_path}"
"""
subprocess.run(cmd, shell=True, executable="/bin/bash")
