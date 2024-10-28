import tkinter as tk

class VistaNotas:
    def __init__(self,root):
        self.root=root
        #TITULO
        self.root.title("Repaso")
        #ETIQUETA
        self.etiqueta = tk.Label(root, text="Aplicación de gestión de notas")
        self.etiqueta.pack()

        #ETIQUETA
        self.etiqueta_coords = tk.Label(root, text="Coordenadas click: ")
        self.etiqueta_coords.pack(pady=5)

        #FRAME PARA GUARDAR EN ÉL LA LISTBOX
        listbox_frame = tk.Frame(root)
        listbox_frame.pack(pady=10)

        #LISTBOX
        self.listbox = tk.Listbox(listbox_frame, width=50)
        self.listbox.pack(pady=10, side=tk.LEFT)

        #ENTRY
        self.entrada=tk.Entry(root,width=10)
        self.entrada.pack()

        #FRAME PARA LOS BOTONES
        button_frame=tk.Frame(root)
        button_frame.pack(pady=10)

        #BOTONES PARA ACCIONES
        self.agregarnota=tk.Button(button_frame,text="Agregar")
        self.eliminarnota = tk.Button(button_frame, text="Eliminar")
        self.guardarnota = tk.Button(button_frame, text="Guardar")
        self.cargarnota = tk.Button(button_frame, text="Cargar")
        self.descargararchivo=tk.Button(root,text="Descargar archivo")
        
        #ETIQUETA PARA MOSTRAR IMAGEN
        self.etiquetaimagen=tk.Label(root)

        self.agregarnota.grid(row=0,column=0)
        self.eliminarnota.grid(row=0,column=1)
        self.guardarnota.grid(row=0,column=2)
        self.cargarnota.grid(row=0,column=3)
        self.descargararchivo.pack(pady=10)
        self.etiquetaimagen.pack()


