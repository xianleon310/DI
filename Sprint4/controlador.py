import tkinter as tk
from tkinter import messagebox, simpledialog
from vista import MainMenu,GameView
#from modelo import GameModel

class GameController:
    #LLEGAMOS AL ARCHIVO
    def __init__(self, root):
        #GUARDAMOS EL "root" CREADO EN EL MAIN EN ESTA CLASE
        self.root = root
        #CREAMOS UNA INSTANCIA "main_menu" LLENDO A LA CLASE "MainMenu" LLEVANDO DE ESTA CLASE 3 MÉTODOS
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)

    def start_game_callback(self):
        #CREA UN OBJETO ASKSTRING "difficulty" EL CUAL ALMACENARÁ LO ESCRITO EN "parent",
        self.difficulty=simpledialog.askstring(
            #CON TÍTULO "seleccionar dificulatad",
            "Seleccionar dificultad",
            # CON CUERPO "Elige la dificultad",
            "Elige la dificultad(facil,media,dificil)",
            # Y CON UN CUADRO DE TEXTO PARA ESCRIBIR EN ÉL
            parent=self.root
            )
        #SI LAS PALABRAS "facil","medio" O "dificil" ESTÁN EN EL OBJETO CREADO
        if self.difficulty in ["facil", "medio", "dificil"]:
            #GUARDA EN LA VARIABLE "self.player_name" EL VALOR DEL MÉTODO "ask_player_name" ALMACENADA EN VISTA (ESTÁ DECLARADA COMO "main_menu" PORQUE YA SE HA INSTANCIADO EN EL CONSTRUCTOR)
            self.player_name = self.main_menu.ask_player_name()
            #SI SE HA ESCRITO EL NOMBRE
            if self.player_name:
                # MENSAJE CON EL NOMBRE Y DIFICULTAD QUE HAS ESCOGIDO
                messagebox.showinfo("Inicio del Juego", "Dificultad: "+self.difficulty+"\n"+"Jugador:"+ self.player_name)
            #SI NO SE HA ESCRITO EL NOMBRE SALTA UN MENSAJE DE ERROR
            else:
                messagebox.showwarning("Advertencia", "Debe ingresar un nombre para jugar.")
        #SI LAS PALABRAS "facil","medio" O "dificil" NO ESTÁN EN EL OBJETO CREADO
        else:
            #MENSAJE DE ERROR
            messagebox.showwarning("Advertencia", "Dificultad no válida.")

    def show_stats_callback(self):
        #MENSAJE
        messagebox.showinfo("Acción", "Has seleccionado 'Estadísticas'")

    def quit_callback(self):
        #QUITA LA PÁGINA
        self.root.quit()

    def show_loading_window(self,message):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando")
        tk.Label(self.loading_window, text=message).pack(pady=20)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()


    def check_images_loaded(self):

        if self.game_model.images_loaded.is_set():
            if self.loading_window:
                self.loading_window.destroy()
            self.start_game()
        else:
            self.root.after(100, self.check_images_loaded)