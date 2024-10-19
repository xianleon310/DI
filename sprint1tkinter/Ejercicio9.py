import tkinter as tk
from tkinter import messagebox


def acercade():
    #EL EL COMANDO DE "Acerca de" NOS ABRIRÁ UNA VENTANA EMERGENTE CON EL TEXTO "Has seleccionado la opción 'A cerca de' en el menú!"
    messagebox.showinfo("Información", "¡Has seleccionado la opción 'A cerca de' en el menú!")

def abrir():
    #EL EL COMANDO DE "Abrir" NOS ABRIRÁ UNA VENTANA EMERGENTE CON EL TEXTO "¡Has seleccionado la opción 'Abrir' en el menú!"
    messagebox.showinfo("Información", "¡Has seleccionado la opción 'Abrir' en el menú!")


root=tk.Tk()
root.title("Ejercicio9")
root.geometry("300x200")

#LA VARIABLE MENÚ REPRESENTA A TODAS LAS VARIABLES QUE TENGAMOS DE TIPO MENÚ
menu = tk.Menu(root)

#CREAMOS LA VARIABLE "menu_archivo" LA CUAL ESTARÁ DENTRO DE LA VARIABLE "menu" CREADA ANTERIORMENTE, COMO "menu_ayuda" YA QUE ESTAS SON SUBMENÚS DEL MENÚ PRINCIPAL "menu"
menu_archivo = tk.Menu(menu, tearoff=0)
#OPCION 1 DEL MENÚ, EN LA QUE EL COMANDO SERÁ EL MÉTODO AL QUE REDIRIGIRÁ PARA HACER LAS INSTRUCCIONES
menu_archivo.add_command(label="Abrir", command=abrir)
#OPCION 2 DEL MENÚ, EN LA QUE EL COMANDO SERÁ EL MÉTODO AL QUE REDIRIGIRÁ PARA HACER LAS INSTRUCCIONES
menu_archivo.add_command(label="Salir", command=root.quit)
#INDICAMOS QUE EL TITULO ANTES DE DESGLOSAR LAS OPCIONES SERÁ "Archivo" (label="Archivo") Y ENCADENAMOS LAS OPCIONES AL TÍTULO (menu="menu_archivo")
menu.add_cascade(label="Archivo", menu=menu_archivo)

#CREAMOS LA VARIABLE "menu_ayuda" LA CUAL ESTARÁ DENTRO DE LA VARIABLE "menu" CREADA ANTERIORMENTE, COMO "menu_archivo" YA QUE ESTAS SON SUBMENÚS DEL MENÚ PRINCIPAL "menu"
menu_ayuda=tk.Menu(menu,tearoff=0)
#OPCION 1 DEL MENÚ, EN LA QUE EL COMANDO SERÁ EL MÉTODO AL QUE REDIRIGIRÁ PARA HACER LAS INSTRUCCIONES
menu_ayuda.add_command(label="A cerca de", command=acercade)
#INDICAMOS QUE EL TITULO ANTES DE DESGLOSAR LAS OPCIONES SERÁ "Ayuda" (label="Ayuda") Y ENCADENAMOS LAS OPCIONES AL TÍTULO (menu="menu_ayuda")
menu.add_cascade(label="Ayuda", menu=menu_ayuda)


root.config(menu=menu)

root.mainloop()