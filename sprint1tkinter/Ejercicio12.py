import tkinter as tk
from tkinter import scrolledtext, messagebox

lista_usuarios=[]
def update_label(value):  # DEFINE UNA FUNCIÓN PARA ACTUALIZAR LA ETIQUETA
    label.config(text=f"Años:"+value)  # ACTUALIZA EL TEXTO DE LA ETIQUETA CON EL VALOR SELECCIONADO

def registrarusuario():
    #GUARDAR EN LAS VARIABLES "nombre","edad" y "sexo" EL VALOR QUE RECOGE POR EL USUARIO
     nombre=str(entry.get())
     edad=str(scale.get())
     if (var_radio.get()=="otro"):
         sexo="'otro'"
     if (var_radio.get() == "masc"):
        sexo = "masculino"
     if (var_radio.get() =="fem"):
         sexo="femenino"
    #CREAMOS UNA LISTA "usuario" DONDE ALMACENA EL NOMBRE, EDAD Y SEXO DE UNO DE LOS USUARIOS
     usuario=["El usuario "+nombre+" con "+edad+" años y de género "+sexo]
    #CREAMOS UNA LISTA DE USUARIOS, DONDE LOS DATOS DE ESE USUARIO VAN A OTRA LISTA
     lista_usuarios.append(usuario)
    # INSERTA EL USUARIO EN LA "LISTBOX"
     listbox.insert(tk.END, usuario)
def eliminarusuario():
    if listbox.curselection():  # Verifica que hay una selección
        listbox.delete(listbox.curselection())  # Elimina el usuario seleccionado

def guardarlista():
    messagebox.showinfo("Guardar lista", "¡La lista ha sido guardada!")
def cargarlista():
    messagebox.showinfo("Cargar lista", "¡La lista ha sido cargada!")

root=tk.Tk()
root.title("Ejercicio12")
root.geometry("750x750")




#----------------------------------------------------------------------------------------------------------
#(1)CAMPO DE ENTRADA NOMBRE USUARIO:

#CREAR FRAME PARA ALMACENAR LA ETIQUETA Y EL ENTRY EN EL MISMO SITIO
frame = tk.Frame(root)
frame.pack(pady=10)
#CREAR TEXTO "Nombre:" EL CUAL ESTARÁ DENTRO DEL FRAME ANTERIORMENTE CREADO
etiqueta= tk.Label(frame,text="Nombre:")
etiqueta.pack()
#CREA UN CAMPO DE ENTRADA, QUE ESTARÁ DENTRO DE "frame" Y TENDRÁ ANCHURA DE 30
entry = tk.Entry(frame, width=30)
#MUESTRA EL CAMPO DE ENTRADA
entry.pack(pady=10)
#--------------------------------------------------------------------------------------
#(2)BARRA DESLIZANTE (SCALE) PARA LA EDAD DEL USUARIO (0-100)

label = tk.Label(root, text="Introduce la edad (0-100):")  # INICIALIZA LA ETIQUETA CON UN VALOR INICIAL
label.pack()  # AGREGA LA ETIQUETA A LA VENTANA Y AÑADE ESPACIO VERTICAL
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_label)  # CONFIGURA LA BARRA DESLIZANTE DE 0 A 100
scale.pack()  # AGREGA LA BARRA DESLIZANTE A LA VENTANA Y AÑADE ESPACIO VERTICAL
#--------------------------------------------------------------------------------------
#(3)TRES RADIOBUTTON PARA SELECCIONAR EL GÉNERO

#CREAR TEXTO "Sexo:"
etiqueta= tk.Label(root,text="Sexo:")
etiqueta.pack(pady=10)
#CREAR VARIABLE "var_radio" DE TIPO STRING, LA CUAL ESTARÁ VINCULADA A LOS RADIOBUTTON Y QUE MARCARÁ POR DEFECTO "otro"
var_radio=tk.StringVar(value="otro")
#CREAR INSTANCIAS DE RADIOBUTTON
#TIENEN TODOS LA MISMA VARIABLE, YA QUE EN CASO DE TENER UNA DIFERENTE SE PODRÍAN MARCAR TODAS LAS OPCIONES
#EL VALUE TIENE QUE VER CON EL VALOR, SERÁ LO QUE SE TENGA EN CUENTA AL HACER COMPARACIONES COMO DEFINICIÓN
radiobutton1 = tk.Radiobutton(root, text="Masculino", variable=var_radio, value="masc")
radiobutton2 = tk.Radiobutton(root, text="Femenino", variable=var_radio, value="fem")
radiobutton3 = tk.Radiobutton(root, text="Otro", variable=var_radio, value="otro")
#EMPAQUETAR BOTONES
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

#--------------------------------------------------------------------------------------
#(4)BOTÓN PARA AÑADIR EL USUARIO A UNA LISTA

#BOTÓN QUE AL HACER CLIC REDIRIGIRÁ AL MÉTODO "registrarusuario()"
boton=tk.Button(root,text="Registrarse",command=registrarusuario)
boton.pack(pady=10)

#--------------------------------------------------------------------------------------
#(5) LISTBOX QUE MUESTRE NOMBRE, EDAD Y SEXO DE TODOS LOS USUARIOS REGISTRADOS
#CREA UN FRAME PARA LUEGO ASOCIARLO A UNA BARRA LATERAL (SIGUIENTE EJERCICIO)
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)
listbox = tk.Listbox(listbox_frame, width=50)
listbox.pack(pady=10,side=tk.LEFT)

#--------------------------------------------------------------------------------------
#(6) SCROLLBAR PARA LA LISTBOX
#CREA UNA BARRA LATERAL DENTRO DEL FRAME ASOCIADO CON LA LISTBOX
scrollbar = tk.Scrollbar(listbox_frame)
#SCROLLBAR.PACK(SIDE=tk.RIGHT, FILL=tk.Y): ESTO COLOCA LA SCROLLBAR EN EL LADO DERECHO
# DEL LISTBOX_FRAME. EL ARGUMENTO FILL=tk.Y INDICA QUE LA BARRA DE DESPLAZAMIENTO
# DEBE EXTENDERSE PARA LLENAR TODO EL ESPACIO VERTICAL DISPONIBLE.
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#EL LISTBOX ENVIARÁ INFORMACIÓN A LA SCROLLBAR SOBRE SU POSICIÓN DE DESPLAZAMIENTO.
# CUANDO EL CONTENIDO DEL LISTBOX CAMBIE (POR EJEMPLO, CUANDO SE AÑADAN MÁS ELEMENTOS),
# SE LLAMARÁ A SCROLLBAR.SET() PARA ACTUALIZAR LA POSICIÓN DE LA SCROLLBAR DE ACUERDO
# CON LA POSICIÓN ACTUAL DEL LISTBOX.
listbox.config(yscrollcommand=scrollbar.set)
#ESTO CONFIGURA LA SCROLLBAR PARA QUE CONTROLE LA VISTA DEL LISTBOX.
# CUANDO EL USUARIO INTERACTÚE CON LA SCROLLBAR (POR EJEMPLO, DESLIZÁNDOLA HACIA ARRIBA
# O HACIA ABAJO), SE LLAMARÁ A LISTBOX.YVIEW(), LO QUE DESPLAZARÁ LA VISTA DEL LISTBOX
# EN LA DIRECCIÓN CORRESPONDIENTE.
scrollbar.config(command=listbox.yview)

#--------------------------------------------------------------------------------------
#(7) BOTÓN PARA ELIMINAR USUARIO DE LA LISTBOX
botoneliminar=tk.Button(root,text="Eliminar usuario",command=eliminarusuario)
botoneliminar.pack(pady=10)

#--------------------------------------------------------------------------------------
#(8) BOTÓN PARA SALIR DE LA APLICACIÓN
botonsalir=tk.Button(root,text="Salir",command=root.destroy)
botonsalir.pack(pady=10)

#--------------------------------------------------------------------------------------
#(9) DESPLEGABLE CON GUARDAR Y CARGAR LISTA

menu=tk.Menu(root)
menu_desple=tk.Menu(menu,tearoff=0)
menu_desple.add_command(label="Guardar lista",command=guardarlista)
menu_desple.add_command(label="Cargar lista",command=cargarlista)
menu.add_cascade(label="Opciones",menu=menu_desple)

root.config(menu=menu)


root.mainloop()

