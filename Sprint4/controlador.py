import tkinter as tk
from tkinter import messagebox, simpledialog
from vista import MainMenu,GameView
from modelo import GameModel

class GameController:
    #LLEGAMOS AL ARCHIVO
    def __init__(self, root):
        #GUARDAMOS EL "root" CREADO EN EL MAIN EN ESTA CLASE
        self.root = root
        #CREAMOS UNA INSTANCIA "main_menu" LLENDO A LA CLASE "MainMenu" LLEVANDO DE ESTA CLASE 3 MÉTODOS
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)
        self.move_count = 0  # Contador de movimientos inicializado en 0
        self.time_elapsed = 0  # Temporizador en segundos inicializado en 0

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

                # Crea el modelo del juego con dificultad y nombre
                self.game_model = GameModel(self.difficulty, self.player_name)

                # Muestra ventana de carga mientras se descargan las imágenes
                self.show_loading_window("Cargando imágenes, por favor espera...")

                # Inicia la verificación periódica de descarga de imágenes
                self.check_images_loaded()


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

    def show_loading_window(self, message):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando")
        tk.Label(self.loading_window, text=message).pack(pady=20)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()  # Hace la ventana de carga modal

    def check_images_loaded(self):
        if self.game_model.images_loaded.is_set():
            if self.loading_window:
                self.loading_window.destroy()
            self.start_game()
        else:
            self.root.after(100, self.check_images_loaded)

    def on_card_click(self, position):
        """Este método maneja la acción de clic en una carta."""
        # Obtén la ID de la imagen de la posición seleccionada del modelo.
        image_id = self.game_model.cards[position[0]][position[1]]

        # Revela la carta seleccionada
        self.game_view.update_board(position, image_id)
    def update_move_count(self):
        self.move_count += 1
        self.game_view.update_move_count(self.move_count)  # Llama a la vista para actualizar el display

    # Método para actualizar el tiempo transcurrido
    def update_time(self):
        self.time_elapsed += 1  # Esto dependerá de cómo estés midiendo el tiempo
        self.game_view.update_time(self.time_elapsed)  # Actualiza el tiempo en la interfaz

    # Implementación del inicio del juego con callbacks
    def start_game(self):
        self.game_view = GameView(
            on_card_click_callback=self.on_card_click,
            update_move_count_callback=self.update_move_count,
            update_time_callback=self.update_time,
        )
        self.game_view.create_board(self.game_model)