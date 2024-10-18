import tkinter as tk

def mostrar_fruta():
    #OBTENER LA FRUTA SELECCIONADA DE LA LISTBOX
    fruta_seleccionada = listbox.get(listbox.curselection())
    #ACTUALIZAR LA ETIQUETA CON EL NOMBRE DE LA FRUTA SELECCIOANDA
    etiqueta.config(text=f"Fruta seleccionada:"+fruta_seleccionada)

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("Ejercicio 6")
root.geometry("300x200")

# CREAR LISTA DE FRUTAS
frutas = ["Manzana", "Banana", "Naranja"]

# CREAR LISTBOX
listbox = tk.Listbox(root)
#RECORRE TODOS LOS ELEMENTOS DE LA LISTA (LOS CUALES TENDRÁN LA VARIABLE DE "fruta"
for fruta in frutas:
    #INSERTA EN LA LISTBOX CADA UNO DE LOS ELEMENTOS DA LISTA, POSICIONÁNDOSE CON EL "tk.END"
    # YA QUE SERÍA EL EQUIVALENTE A "lista.size()"
    listbox.insert(tk.END, fruta)
listbox.pack()

#CREAR BOTÓN QUE MOSTRARÁ LA FRUTA (VA AL MÉTODO "mostrar_fruta")
boton = tk.Button(root, text="Mostrar Fruta", command=mostrar_fruta)
boton.pack()

# CREAR ETIQUETA QUE MUESTRE EL TEXTO "Fruta seleccionada:" MIENTRAS QUE NO SE PULSA EL BOTÓN
#!SOLO SE MOSTRARÁ LA PRIMERA VEZ QUE SE ABRA EL PROGRAMA
etiqueta = tk.Label(root, text="Fruta seleccionada:")
etiqueta.pack()


root.mainloop()
