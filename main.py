import tkinter as tk
from gui_productos import ventana_productos
from gui_ventas import ventana_ventas

def main():
    root = tk.Tk()
    root.title("Service Manager")

    tk.Button(root, text="Gestión de Productos", width=30, command=ventana_productos).pack(pady=10)
    tk.Button(root, text="Registro de Ventas", width=30, command=ventana_ventas).pack(pady=10)
    tk.Button(root, text="Salir", width=30, command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
