from db import leer_json, guardar_json
from producto import obtener_productos

RUTA_VENTAS = "data/ventas.json"
RUTA_PRODUCTOS = "data/productos.json"

def registrar_venta(indice_producto, cantidad):
    productos = leer_json(RUTA_PRODUCTOS)
    ventas = leer_json(RUTA_VENTAS)

    if 0 <= indice_producto < len(productos):
        producto = productos[indice_producto]
        if producto["cantidad"] >= cantidad:
            producto["cantidad"] -= cantidad
            total = producto["precio"] * cantidad
            ventas.append({
                "producto": producto["nombre"],
                "cantidad": cantidad,
                "total": total
            })
            guardar_json(RUTA_PRODUCTOS, productos)
            guardar_json(RUTA_VENTAS, ventas)

def obtener_ventas():
    return leer_json(RUTA_VENTAS)