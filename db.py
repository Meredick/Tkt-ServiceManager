import json
import os

def leer_json(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r") as f:
        return json.load(f)

def guardar_json(ruta, datos):
    with open(ruta, "w") as f:
        json.dump(datos, f, indent=2)
