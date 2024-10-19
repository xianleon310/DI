import tkinter as tk
#Método que modifica el texto de la etiqueta presionando el boton1
def etiqueta_texto():
    etiqueta.config(text="Nueva etiqueta")
    etiqueta.pack()
#Método que cerrará al presionar el botón2
def cerrar_ventana():
    root.destroy()

root=tk.Tk()
root.title("Ejercicio2")
root.geometry("300x200")

#Crear etiqueta vacía para modificarla en el método en el tk.button(1)*
#Si se crea una nueva etiqueta en el método se verían muchas líneas de texto
etiqueta = tk.Label(root, text="")
#(1)*
boton1 = tk.Button(root, text="Botón1", command=etiqueta_texto)
boton2 = tk.Button(root, text="Botón2", command=cerrar_ventana)
boton1.pack()
boton2.pack()
root.mainloop()