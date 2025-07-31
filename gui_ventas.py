import tkinter as tk
from tkinter import messagebox
from producto import obtener_productos
from venta import registrar_venta, obtener_ventas

def cargar_lista_productos(lista):
    lista.delete(0, tk.END)
    for i, p in enumerate(obtener_productos()):
        texto = f"{i+1}. {p['nombre']} - ${p['precio']} ({p['cantidad']} u.)"
        lista.insert(tk.END, texto)

def cargar_lista_ventas(lista):
    lista.delete(0, tk.END)
    for v in obtener_ventas():
        texto = f"{v['producto']} x{v['cantidad']} - Total: ${v['total']}"
        lista.insert(tk.END, texto)

def ventana_ventas():
    win = tk.Toplevel()
    win.title("Registro de Ventas")

    lista_prod = tk.Listbox(win, width=50)
    lista_prod.grid(row=0, column=0, columnspan=4, pady=5)
    cargar_lista_productos(lista_prod)

    tk.Label(win, text="Cantidad").grid(row=1, column=0)
    e_cantidad = tk.Entry(win)
    e_cantidad.grid(row=1, column=1)

    def vender():
        sel = lista_prod.curselection()
        if sel:
            try:
                i = sel[0]
                cantidad = int(e_cantidad.get())
                registrar_venta(i, cantidad)
                cargar_lista_productos(lista_prod)
                cargar_lista_ventas(lista_ventas)
            except:
                messagebox.showerror("Error", "Cantidad inválida")

    tk.Button(win, text="Vender", command=vender).grid(row=1, column=2)

    lista_ventas = tk.Listbox(win, width=50)
    lista_ventas.grid(row=2, column=0, columnspan=4, pady=5)
    cargar_lista_ventas(lista_ventas)
