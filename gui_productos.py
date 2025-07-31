import tkinter as tk
from tkinter import messagebox
from producto import agregar_producto, obtener_productos, actualizar_producto, eliminar_producto

def cargar_lista(lista):
    lista.delete(0, tk.END)
    for i, p in enumerate(obtener_productos()):
        texto = f"{i+1}. {p['nombre']} - ${p['precio']} - {p['cantidad']} u."
        lista.insert(tk.END, texto)

def ventana_productos():
    win = tk.Toplevel()
    win.title("Gestión de Productos")

    lista = tk.Listbox(win, width=50)
    lista.grid(row=0, column=0, columnspan=4, pady=5)
    cargar_lista(lista)

    tk.Label(win, text="Nombre").grid(row=1, column=0)
    tk.Label(win, text="Precio").grid(row=2, column=0)
    tk.Label(win, text="Cantidad").grid(row=3, column=0)

    e_nombre = tk.Entry(win)
    e_precio = tk.Entry(win)
    e_cantidad = tk.Entry(win)
    e_nombre.grid(row=1, column=1)
    e_precio.grid(row=2, column=1)
    e_cantidad.grid(row=3, column=1)

    def agregar():
        try:
            agregar_producto(e_nombre.get(), float(e_precio.get()), int(e_cantidad.get()))
            cargar_lista(lista)
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def actualizar():
        try:
            sel = lista.curselection()
            if sel:
                i = sel[0]
                actualizar_producto(i, e_nombre.get(), float(e_precio.get()), int(e_cantidad.get()))
                cargar_lista(lista)
        except:
            messagebox.showerror("Error", "Error al actualizar")

    def eliminar():
        sel = lista.curselection()
        if sel:
            eliminar_producto(sel[0])
            cargar_lista(lista)

    tk.Button(win, text="Agregar", command=agregar).grid(row=4, column=0)
    tk.Button(win, text="Actualizar", command=actualizar).grid(row=4, column=1)
    tk.Button(win, text="Eliminar", command=eliminar).grid(row=4, column=2)
