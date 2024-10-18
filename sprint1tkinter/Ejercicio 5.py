import tkinter as tk


# METODO PARA MOSTRAR COMO FONDO EL COLOR EN EL QUE HEMOS HECHO CLIC
def mostrarcolor():
    #EN CASO DE QUE EN LO QUE HEMOS HECHO CLIC COINCIDA CON EL VALUE DEL RADIOBUTTON "red" ..
    if var_radio.get()=="red":
        #SE MOSTRARÁ COMO FONDO EL COLOR ROJO
        root.config(bg="red")
    # EN CASO DE QUE EN LO QUE HEMOS HECHO CLIC COINCIDA CON EL VALUE DEL RADIOBUTTON "green" ..
    if var_radio.get()=="green":
        #SE MOSTRARÁ COMO FONDO EL COLOR VERDE
        root.config(bg="green")
    # EN CASO DE QUE EN LO QUE HEMOS HECHO CLIC COINCIDA CON EL VALUE DEL RADIOBUTTON "blue" ..
    if var_radio.get()=="blue":
        #SE MOSTRARÁ COMO FONDO EL COLOR AZUL
        root.config(bg="blue")

#CREA VENTANA
root=tk.Tk()
#NOMBRE QUE APARECERÁ EN LA VENTANA
root.title("Ejercicio5")
#MEDIDAS QUE TENDRÁ LA VENTANA
root.geometry("300x200")

#CREAR VARIABLE "var_radio" DE TIPO STRING, LA CUAL ESTARÁ VINCULADA A LOS RADIOBUTTON
var_radio=tk.StringVar()
#INDICA CUAL ESTARÁ MARCADA POR DEFECTO
var_radio.set("red")
#CAMBIAR EL FONDO DE PANTALLA A ROJO, YA QUE POR DEFECTO ESTARÁ MARCADO "Rojo"
root.config(bg="red")

#CREAR INSTANCIAS DE RADIOBUTTON
#TIENEN TODOS LA MISMA VARIABLE, YA QUE EN CASO DE TENER UNA DIFERENTE SE PODRÍAN MARCAR TODAS LAS OPCIONES
#EL VALUE TIENE QUE VER CON EL VALOR, SERÁ LO QUE SE TENGA EN CUENTA AL HACER COMPARACIONES COMO DEFINICIÓN
radiobutton1 = tk.Radiobutton(root, text="Rojo", variable=var_radio, value="red",command=mostrarcolor)
radiobutton2 = tk.Radiobutton(root, text="Verde", variable=var_radio, value="green",command=mostrarcolor)
radiobutton3 = tk.Radiobutton(root, text="Azul", variable=var_radio, value="blue",command=mostrarcolor)

#EMPAQUETAR BOTONES
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

root.mainloop()