import tkinter as tk
def mostrar():
    #CREA VARIABLE "concatenacion"
    concatenacion = ""
    #"check_var.get()=1 SIGNIFICA "SI ESTÁ ACTIVADA LA CASILLA QUE PERTENEZCA A "check_var"..."
    #SE ESTABLECEN LAS CONDICIONES, PARA QUE EN CASO DE ESTAR ACTIVADAS LAS CASILLAS LAS GUARDA EN LA VARIABLE
    #"concatenacion", a la cual--
    if check_var.get()==1:
        concatenacion += "Leer"+"\n"
    if check_var2.get()==1:
        concatenacion+="Deporte"+"\n"
    if check_var3.get()==1:
        concatenacion+="Música"+"\n"
    #COLOCAREMOS EN LA ETIQUETA VACÍA PARA ASÍ MOSTRARLO ABAJO
    # EJEMPLO: SI MARCAS LA CHECKBOX "Leer" PONDRÁ EL TEXTO "Leer" ALMACENADO EN LA ETIQUETA "etiqueta"
    etiqueta.config(text=concatenacion)

#CREA VENTANA
root=tk.Tk()
#NOMBRE QUE APARECERÁ EN LA VENTANA
root.title("Ejercicio4")
#MEDIDAS QUE TENDRÁ LA VENTANA
root.geometry("300x200")

#CREAR ETIQUETAS VACÍA PARA QUE APAREZCAN LUEGO AL HACER CLIC EN LA CHECKBOX
etiqueta=tk.Label(root,text="")

#CREAR INSTANCIAS DE CHECKBOX
check_var = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()

#CREAR CHECKBOX QUE TENDRÁ DE TEXTO "Leer", ESTARÁ EN LA PRIMERA INSTANCIA CHECKBOX Y PROCESARÁ EL MÉTODO "mostrar"
checkboxleer = tk.Checkbutton(root, text="Leer", variable=check_var, command=mostrar)
checkboxleer.pack(pady=10)
checkboxdeporte = tk.Checkbutton(root, text="Deporte", variable=check_var2, command=mostrar)
checkboxdeporte.pack(pady=10)
checkboxmusica = tk.Checkbutton(root, text="Música", variable=check_var3, command=mostrar)
checkboxmusica.pack(pady=10)

etiqueta.pack()

root.mainloop()