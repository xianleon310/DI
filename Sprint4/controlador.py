import tkinter as tk
from tkinter import messagebox, simpledialog
from vista import MainMenu, GameView
from modelo import GameModel

class GameController:
    # LLEGAMOS AL ARCHIVO
    def __init__(self, root):
        # GUARDAMOS EL "ROOT" CREADO EN EL MAIN EN ESTA CLASE
        self.root = root
        # CREAMOS UNA INSTANCIA "MAIN_MENU" LLAMANDO A LA CLASE "MAINMENU" Y PASANDOLE 3 MÉTODOS COMO PARÁMETROS
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)
        self.move_count = 0  # CONTADOR DE MOVIMIENTOS INICIALIZADO EN 0
        self.time_elapsed = 0  # TEMPORIZADOR EN SEGUNDOS INICIALIZADO EN 0
        self.selected = []  # LISTA PARA ALMACENAR LAS CARTAS SELECCIONADAS

    def start_game_callback(self):
        # CREA UN OBJETO ASKSTRING "DIFFICULTY" EL CUAL ALMACENARÁ LO ESCRITO EN "PARENT"
        self.difficulty = simpledialog.askstring(
            # CON TÍTULO "SELECCIONAR DIFICULTAD"
            "Seleccionar dificultad",
            # CON CUERPO "ELIGE LA DIFICULTAD"
            "Elige la dificultad(facil,media,dificil)",
            # Y CON UN CUADRO DE TEXTO PARA ESCRIBIR EN ÉL
            parent=self.root
        )
        # SI LAS PALABRAS "FACIL", "MEDIO" O "DIFICIL" ESTÁN EN EL OBJETO CREADO
        if self.difficulty in ["facil", "medio", "dificil"]:
            # GUARDA EN LA VARIABLE "SELF.PLAYER_NAME" EL VALOR DEL MÉTODO "ASK_PLAYER_NAME" ALMACENADA EN VISTA
            self.player_name = self.main_menu.ask_player_name()
            # SI SE HA ESCRITO EL NOMBRE
            if self.player_name:
                # MENSAJE CON EL NOMBRE Y DIFICULTAD QUE HAS ESCOGIDO
                messagebox.showinfo("Inicio del Juego", "Dificultad: " + self.difficulty + "\n" + "Jugador:" + self.player_name)

                # CREA EL MODELO DEL JUEGO CON DIFICULTAD Y NOMBRE
                self.game_model = GameModel(self.difficulty, self.player_name)

                # MUESTRA VENTANA DE CARGA MIENTRAS SE DESCARGAN LAS IMÁGENES
                self.show_loading_window("Cargando imágenes, por favor espera...")

                # INICIA LA VERIFICACIÓN PERIÓDICA DE DESCARGA DE IMÁGENES
                self.check_images_loaded()
            # SI NO SE HA ESCRITO EL NOMBRE, SALTA UN MENSAJE DE ERROR
            else:
                messagebox.showwarning("Advertencia", "Debe ingresar un nombre para jugar.")
        # SI LAS PALABRAS "FACIL", "MEDIO" O "DIFICIL" NO ESTÁN EN EL OBJETO CREADO
        else:
            # MENSAJE DE ERROR
            messagebox.showwarning("Advertencia", "Dificultad no válida.")

    def show_stats_callback(self):
        #MUESTRA LAS ESTADÍSTICAS DE PUNTUACIÓN.
        scores = self.game_model.load_scores()
        formatted_scores = "\n".join(
            [f"{dificultad}:\n" + "\n".join([f"{score['nombre']} - {score['movimientos']} movimientos - {score['fecha']}"
                                            for score in scores[dificultad]]) for dificultad in scores]
        )
        messagebox.showinfo("Estadísticas", formatted_scores)

    def quit_callback(self):
        # QUITA LA PÁGINA
        self.root.quit()

    def show_loading_window(self, message):
        # MUESTRA UNA VENTANA MODAL DE CARGA
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando")
        tk.Label(self.loading_window, text=message).pack(pady=20)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()  # HACE QUE LA VENTANA DE CARGA SEA MODAL

    def check_images_loaded(self):
        # VERIFICA SI LAS IMÁGENES HAN SIDO CARGADAS
        if self.game_model.images_loaded.is_set():
            if self.loading_window:
                self.loading_window.destroy()
            self.start_game()
        else:
            self.root.after(100, self.check_images_loaded)

    def on_card_click(self, position):
        #ESTE MÉTODO MANEJA LA ACCIÓN DE CLIC EN UNA CARTA.
        if len(self.selected) == 2:
            return  # SI YA HAY DOS CARTAS SELECCIONADAS, NO HACEMOS NADA

        # SI ES LA PRIMERA CARTA SELECCIONADA, GUARDAMOS LA POSICIÓN Y MOSTRAMOS LA CARTA.
        self.selected.append(position)
        image_id = self.game_model.cards[position[0]][position[1]]

        # INICIA EL TEMPORIZADOR SI ES EL PRIMER CLIC
        if len(self.selected) == 1 and self.time_elapsed == 0:
            self.root.after(1000, self.update_time)  # LLAMA A update_time CADA SEGUNDO

        # ACTUALIZAMOS EL TABLERO PARA MOSTRAR LA CARTA SELECCIONADA
        self.game_view.update_board(position, image_id, self.game_model)

        # SI ES LA SEGUNDA CARTA SELECCIONADA, MANEJAMOS LA COMPARACIÓN
        if len(self.selected) == 2:
            self.handle_card_selection()  # VERIFICA SI LAS CARTAS COINCIDEN O NO

            # INCREMENTAMOS EL CONTADOR DE MOVIMIENTOS Y ACTUALIZAMOS LA VISTA
            self.update_move_count()

    def update_move_count(self):
        # INCREMENTA EL CONTADOR DE MOVIMIENTOS Y ACTUALIZA LA VISTA
        self.move_count += 1
        if self.game_view and self.game_view.is_active:
            self.game_view.update_move_count(self.move_count)

    # MÉTODO PARA ACTUALIZAR EL TIEMPO TRANSCURRIDO
    def update_time(self):
        #ESTE MÉTODO ACTUALIZA EL TEMPORIZADOR.
        self.time_elapsed += 1
        if self.game_view and self.game_view.is_active:
            self.game_view.update_time(self.time_elapsed)
            self.root.after(1000, self.update_time)

    # IMPLEMENTACIÓN DEL INICIO DEL JUEGO CON CALLBACKS
    def start_game(self):
        # CREA UNA INSTANCIA DE GameView Y PASA LOS CALLBACKS Y EL MODELO
        self.game_view = GameView(
            on_card_click_callback=self.on_card_click,
            update_move_count_callback=self.update_move_count,
            update_time_callback=self.update_time,
            game_model=self.game_model  # PASA EL MODELO AQUÍ
        )
        self.game_view.create_board(self.game_model)

    def handle_card_selection(self):
        # MANEJA LA SELECCIÓN DE DOS CARTAS
        pos1, pos2 = self.selected
        image_id1 = self.game_model.cards[pos1[0]][pos1[1]]
        image_id2 = self.game_model.cards[pos2[0]][pos2[1]]
        if image_id1 == image_id2:
            self.selected = []
            self.game_model.cards[pos1[0]][pos1[1]] = None  # MARCA LAS CARTAS COMO COMPLETADAS
            self.game_model.cards[pos2[0]][pos2[1]] = None
            self.check_game_complete()  # VERIFICA SI EL JUEGO ESTÁ COMPLETO
        else:
            self.root.after(1000, self.game_view.reset_cards, pos1, pos2)
            self.selected = []

    def check_game_complete(self):
        #VERIFICA SI EL JUGADOR HA ENCONTRADO TODOS LOS PARES Y COMPLETA EL JUEGO.
        if all(card is None for row in self.game_model.cards for card in row):
            # SI TODAS LAS CARTAS ESTÁN REVELADAS (NONE), EL JUEGO HA TERMINADO
            messagebox.showinfo("¡Felicidades!", f"Juego completado en {self.move_count} movimientos")
            self.save_score()
            self.return_to_main_menu()  # REGRESA AL MENÚ PRINCIPAL

    def save_score(self):
        #GUARDA LA PUNTUACIÓN DEL JUGADOR EN RANKING.TXT
        self.game_model.save_score(self.player_name, self.difficulty, self.move_count)

    def return_to_main_menu(self):
        #REGRESA AL MENÚ PRINCIPAL
        if self.game_view:
            self.game_view.destroy()  # DESTRUYE LA VISTA DEL JUEGO ACTUAL

        if not self.main_menu:  # SOLO CREA UN NUEVO MENÚ SI NO EXISTE
            self.main_menu = MainMenu(self.root, self.start_game_callback, self.show_stats_callback, self.quit_callback)
