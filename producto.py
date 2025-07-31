from db import leer_json, guardar_json
RUTA = "data/productos.json"

def agregar_producto(nombre, precio, cantidad):
    productos = leer_json(RUTA)
    productos.append({
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    })
    guardar_json(RUTA, productos)

def obtener_productos():
    return leer_json(RUTA)

def actualizar_producto(indice, nombre, precio, cantidad):
    productos = leer_json(RUTA)
    if 0 <= indice < len(productos):
        productos[indice] = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        guardar_json(RUTA, productos)

def eliminar_producto(indice):
    productos = leer_json(RUTA)
    if 0 <= indice < len(productos):
        productos.pop(indice)
        guardar_json(RUTA, productos)
