import tkinter as tk
def mostrar_saludo():
    #---ALMACENAMOS EN LA VARIABLE "nombre" LO QUE HEMOS ESCRITO EN EL CAMPO DE ENTRADA
    nombre = entry.get()
    #CREAMOS UNA VARIABLE "saludo" QUE TENDRÁ "¡Hola,*lo que hayamos escrito*!"
    saludo = "¡Hola,"+nombre+"!"
    #MODIFICAMOS LA ETIQUETA PARA QUE TENGA DE TEXTO LA VARIABLE CONFIGURADA EN LA LÍNEA
    #ANTERIOR
    label_saludo.config(text=saludo)
    #LO MATERIALIZAMOS
    label_saludo.pack(pady=10)

#CREA VENTANA
root=tk.Tk()
#NOMBRE QUE APARECERÁ EN LA VENTANA
root.title("Ejercicio3")
#MEDIDAS QUE TENDRÁ LA VENTANA
root.geometry("300x200")

#CREA UN CAMPO DE ENTRADA, QUE ESTARÁ DENTRO DE "root" Y TENDRÁ ANCHURA DE 30
entry = tk.Entry(root, width=30)
#MUESTRA EL CAMPO DE ENTRADA
entry.pack(pady=10)

#CREA UNA ETIQUETA VACÍA DE TEXTO (NO APARECERÁ PERO EN EL CÓDIGO A CONTINUACIÓN
#MODIFICAREMOS LO VACÍO POR UN TEXTO)
label_saludo = tk.Label(root, text="")


#CREA UN BOTÓN, QUE ESTARÁ EN "root", TENDRÁ EL TEXTO "Botón" Y SU RESPECTIVO COMANDO
#SERÁ EL MÉTODO "mostrar_saludo"---
boton = tk.Button(root, text="Botón", command=mostrar_saludo)
#MATERIALIZAMOS EL BOTÓN
boton.pack()

root.mainloop()
