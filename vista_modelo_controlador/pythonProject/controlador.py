import threading
import tkinter as tk
from tkinter import messagebox
import requests
from io import BytesIO
from PIL import Image,ImageTk


class ControladorNotas:
    def __init__(self, modelo, vista):
        #ASIGNA EL MODELO Y VISTA A ATRIBUTOS DEL CONTROLADOR
        self.modelo = modelo
        self.vista = vista

        #ENLAZA LOS BOTONES DE LA VISTA A MÉTODOS EN EL CONTROLADOR
        self.vista.agregarnota.config(command=self.agregar_nota)
        self.vista.eliminarnota.config(command=self.eliminar_nota)
        self.vista.guardarnota.config(command=self.guardar_notas)
        self.vista.cargarnota.config(command=self.cargar_notas)
        self.vista.descargararchivo.config(command=self.iniciar_descarga)

        #ASIGNA EVENTO PARA ACTUALIZAR COORDENADAS DEL CURSOR
        self.vista.root.bind("<Button-1>", self.actualizar_coordenadas)

    def agregar_nota(self):
        #GUARDA EN LA VARIABLE "nuevanota" LO CORRESPONDIENTE A LO QUE SE HAYA PUESTO EN EL ENTRY ESPECIFICADO EN LA VISTA
        nuevanota = self.vista.entrada.get()
        #LLEVA LA VARIABLE AL MÉTODO "agregar_nota" DE LA CLASE MODELO, LO CUAL LO GUARDARÁ EN LA LISTA "notas" DE ESA CLASE
        self.modelo.agregar_nota(nuevanota)
        #PARA QUE SE VACÍE LA ENTRADA LUEGO DE PULSAR EN EL BOTÓN
        self.vista.entrada.delete(0,tk.END)
        #VA AL MÉTODO "actualizar_listbox" LLEVANDO LA LISTA CON TODAS LAS NOTAS
        self.actualizar_listbox(self.modelo.obtener_notas())

    def eliminar_nota(self):
        # GUARDA EN LA VARIABLE "noteliminada" LO CORRESPONDIENTE A LO SELECCIONADO CON EL RATÓN DE LA LISTBOX (SI HAY ALGO SELECCIONADO GUARDA EL ÍNDICE DE LA POSICIÓN)
        noteliminada=self.vista.listbox.curselection()
        #SI HAY ALGO SELECCIONADO..
        if noteliminada:
            #LE PASA DICHO ÍNDICE AL MÉTODO "eliminar_nota" DE LA CLASE MODELO, EL CUAL ELIMINARÁ LA NOTA DE LA LISTA DE LA CLASE MODELO SEGÚN EL ÍNDICE DE LA LÍNEA SELECCIONADA
            self.modelo.eliminar_nota(noteliminada[0])
            #VA AL MÉTODO "actualizar_listbox" LLEVANDO LA LISTA CON TODAS LAS NOTAS AHORA, CON ESA ELIMINADA EN LA LÍNEA ANTERIOR
            self.actualizar_listbox(self.modelo.obtener_notas())

    def guardar_notas(self):
        #VA AL MÉTODO "guardar_notas" DEL MODELO
        self.modelo.guardar_notas()
        #LANZA UNA VENTANA EMERJENTE CON EL SIGUIENTE TÍTULO Y TEXTO:
        messagebox.showinfo("Atención", "Notas guardadas correctamente")

    def cargar_notas(self):
        # VA AL MÉTODO "CARGAR_notas" DEL MODELO
        self.modelo.cargar_notas()
        #VA AL MÉTODO "actualizar_listbox" LLEVANDO LA LISTA CON TODAS LAS NOTAS. ESTE PASO HAY QUE HACERLO, PORQUE A DIFERENCIA DEL MÉTODO "guardar_notas",
        #ESTE MÉTODO SE CORRESPONDE CON EL APARTADO GRÁFICO E INFLUYE LA LISTBOX
        self.actualizar_listbox(self.modelo.obtener_notas())
        # LANZA UNA VENTANA EMERJENTE CON EL SIGUIENTE TÍTULO Y TEXTO:
        messagebox.showinfo("Atención", "Notas cargadas correctamente.")
#IMAGENES Y COORDENADAS
    def descargar_imagen(self,url,callback):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            imagen = Image.open(BytesIO(respuesta.content))
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.vista.root.after(0, callback, imagen_tk)
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
            self.vista.root.after(0, callback, None)

    def actualizar_etiqueta(self,imagen_tk):
        if imagen_tk:
            self.vista.etiquetaimagen.config(image=imagen_tk)
            self.vista.etiquetaimagen.image = imagen_tk
        else:
            self.vista.etiquetaimagen.config(text="Error al descargar la imagen.")

    def iniciar_descarga(self):
        url = 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/fototkinter.jpg'
        # Imagen de repositorio de Marcos Rama, xa que o meu é repositorio privado
        hilo = threading.Thread(target=self.descargar_imagen, args=(url, self.actualizar_etiqueta))
        hilo.start()

    def actualizar_coordenadas(self,event):
        self.vista.etiqueta_coords.config(text=f"Coordenadas: {event.x}, {event.y}")

#-------------------------------------------------------------------------------------
    #RECIBE COMO PARÁMETRO LA LISTA DE LAS NOTAS
    def actualizar_listbox(self,notas):
        #LIMPIA EL LISTBOX
        self.vista.listbox.delete(0, tk.END)
        #PARA CADA LÍNEA (nota) EN LA LISTA "notas"..
        for nota in notas:
            #INSERTA EN EL LISTBOX (SITUADO EN "vista") LA LISTA AHORA AL COMPLETO, AÑADIENDO LA ÚLTIMA MODIFICACIÓN
            self.vista.listbox.insert(tk.END, nota)