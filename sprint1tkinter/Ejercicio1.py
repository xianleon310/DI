import tkinter as tk

#Comando el cual utilizaremos más abajo para cambiar el texto de "etiqueta3" al
# que aparece luego de "text="
def cambiar_texto():
    etiqueta3.config(text="Texto Cambiado")


#Creamos un objeto llamado "root" el cual utilizaremos. Lleva el "tk" procedente en el
#importe (luego de "import tkinter as..")".Tk()", necesario y de forma predeterminada
root=tk.Tk()

#Le damos un título a la ventana
root.title("Mi Primera ventana")

#Le daremos un tamaño a la ventana
root.geometry("300x200")

#Creamos widget "etiquetax", las cuales señalan a tk, y se señala root
# entre los paréntesis para indicar que están dentro de la ventana.
#Como segundo parámetro indican que queremos ese texto
etiqueta=tk.Label(root,text="¡Bienvenido!")
etiqueta2=tk.Label(root,text="Xian")
etiqueta3 = tk.Label(root, text="Haz clic en el botón para cambiarme.")


#Estas líneas llaman al método pack() en el objeto etiqueta, que coloca
# la etiqueta en la ventana y la muestra. El método pack() organiza
#  los widgets en la ventana en el orden en que se agregan.
#Sin estas etiquetas el texto no se mostraría
etiqueta.pack()
etiqueta2.pack()
etiqueta3.pack()


# Botón que cambia el texto de la tercera etiqueta
#tk.Button crea un botón el cual tendrá "Cambiar texto" dentro de él y el
#(1)*
#método "cambiar_texto" el cual si hacemos clic se ejecutará dicho
# método que cambia el texto al escrito en el método.
boton = tk.Button(root, text="Cambiar Texto", command=cambiar_texto)
boton.pack()
root.mainloop()