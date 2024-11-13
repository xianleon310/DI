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
        self.selected=[]

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
        if len(self.selected) == 2:
            return  # Si ya hay dos cartas seleccionadas, no hacemos nada

        # Si es la primera carta seleccionada, guardamos la posición y mostramos la carta.
        self.selected.append(position)
        image_id = self.game_model.cards[position[0]][position[1]]

        # Inicia el temporizador si es el primer clic
        if len(self.selected) == 1 and self.time_elapsed == 0:
            self.root.after(1000, self.update_time)  # Llama a update_time cada segundo

        # Actualizamos el tablero para mostrar la carta seleccionada
        self.game_view.update_board(position, image_id, self.game_model)

        # Si es la segunda carta seleccionada, manejamos la comparación
        if len(self.selected) == 2:
            self.handle_card_selection()  # Verifica si las cartas coinciden o no

            # Incrementamos el contador de movimientos y actualizamos la vista
            self.update_move_count()

    def update_move_count(self):
        self.move_count += 1
        self.game_view.update_move_count(self.move_count)  # Llama a la vista para actualizar el display

    # Método para actualizar el tiempo transcurrido
    def update_time(self):
        """Este método actualiza el temporizador."""
        self.time_elapsed += 1
        self.game_view.update_time(self.time_elapsed)
        # Llama a la función después de un segundo para seguir actualizando el tiempo
        self.root.after(1000, self.update_time)

    # Implementación del inicio del juego con callbacks
    def start_game(self):
        self.game_view = GameView(
            on_card_click_callback=self.on_card_click,
            update_move_count_callback=self.update_move_count,
            update_time_callback=self.update_time,
            game_model=self.game_model  # Pasa el modelo aquí
        )
        self.game_view.create_board(self.game_model)

    def handle_card_selection(self):
        """Este método maneja la lógica de comparación de las cartas seleccionadas."""
        pos1, pos2 = self.selected
        image_id1 = self.game_model.cards[pos1[0]][pos1[1]]
        image_id2 = self.game_model.cards[pos2[0]][pos2[1]]

        # Verificamos si las dos cartas son iguales
        if image_id1 == image_id2:
            # Si son iguales, las dejamos reveladas
            self.selected = []  # Limpiar la selección aquí
        else:
            # Si no son iguales, las ocultamos nuevamente después de un retraso
            self.root.after(1000, self.game_view.reset_cards, pos1, pos2)
            self.selected = []  # Limpiar la selección después de la espera

