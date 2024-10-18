import tkinter as tk

# Función para mostrar el contenido del Entry en una etiqueta
def mostrar_contenido():
    contenido = entry.get()  # Obtener el contenido del Entry
    etiqueta_mostrada.config(text=contenido)  # Mostrarlo en la etiqueta

# Función para borrar el contenido del Entry
def borrar_contenido():
    entry.delete(0, tk.END)  # Borrar el contenido del Entry
    etiqueta_mostrada.config(text="")  # Limpiar la etiqueta mostrada

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio8")
root.geometry("300x200")

#CREAR FRAME (CONTENEDOR, PARA MANTENER EL ORDEN DE ETIQUETAS U OTROS ELEMENTOS)
frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

#CREAR ETIQUETA1 DENTRO DEL CONTENEDOR
etiqueta1 = tk.Label(frame_superior, text="Etiqueta 1")
etiqueta1.pack()

#CREAR ETIQUETA2 DENTRO DEL CONTENEDOR
etiqueta2 = tk.Label(frame_superior, text="Etiqueta 2")
etiqueta2.pack()

# CREAR UN CAMPO DE ENTRADA DENTRO DEL CONTENEDOR INFERIOR
entry = tk.Entry(frame_superior)
entry.pack()

# CREAR OTRO CONTENEDOR
frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)


# Crear una etiqueta para mostrar el contenido del Entry
etiqueta_mostrada = tk.Label(root, text="")

# CREAR BOTONES EN CONTENEDOR INFERIOR
boton_mostrar = tk.Button(frame_inferior, text="Mostrar Contenido", command=mostrar_contenido)
boton_mostrar.pack(side=tk.LEFT, padx=5)

boton_borrar = tk.Button(frame_inferior, text="Borrar Contenido", command=borrar_contenido)
boton_borrar.pack(side=tk.LEFT, padx=5)

etiqueta_mostrada.pack(pady=10)

root.mainloop()
