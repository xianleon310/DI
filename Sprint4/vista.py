import tkinter as tk
#IMPORTES NECESARIOS PARA LAS VENTANAS Y DIALOGOS SECUNDARIOS DE LA INTERFAZ
from tkinter import simpledialog,Toplevel

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback, game_model):
        self.window = Toplevel()
        self.labels = []
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.game_model = game_model  # Agrega el modelo aquí
        self.buttons = []


    def create_board(self, model):
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        for i, row in enumerate(model.cards):
            row_frame = tk.Frame(self.board_frame)
            row_frame.pack()
            row_buttons = []  # Esta lista almacenará los botones de esta fila
            for j, image_id in enumerate(row):
                # Crear cada botón con la imagen oculta
                button = tk.Button(row_frame, image=model.hidden_image)
                button.grid(row=i, column=j)
                # Añadir un comando para manejar los clics en cada carta
                button.config(command=lambda pos=(i, j): self.on_card_click_callback(pos))
                row_buttons.append(button)  # Añadir el botón a la fila

            self.buttons.append(row_buttons)  # Añadir la fila de botones a self.buttons

    def update_board(self, pos, image_id, model):
        i, j = pos
        button = self.buttons[i][j]  # Acceder al botón correspondiente
        button.config(image=model.images[image_id])  # Actualizar la imagen

    def reset_cards(self, pos1, pos2):
        """Ocultar las cartas después de un retraso si no coinciden"""
        i1, j1 = pos1
        i2, j2 = pos2
        self.buttons[i1][j1].config(image=self.game_model.hidden_image)
        self.buttons[i2][j2].config(image=self.game_model.hidden_image)

    def update_move_count(self,moves):
        if hasattr(self, 'move_label'):
            self.move_label.config(text=f"Movimientos: {moves}")
        else:
            self.move_label = tk.Label(self.window, text=f"Movimientos: {moves}")
            self.move_label.pack()

    def update_time(self, time):
        if hasattr(self, 'time_label'):
            self.time_label.config(text=f"Tiempo: {time}s")
        else:
            self.time_label = tk.Label(self.window, text=f"Tiempo: {time}s")
            self.time_label.pack()

    def destroy(self):
        pass


class MainMenu:
    #TRANSPORTA DEL CONTROLADOR EL ROOT, LA LÓGICA DEL COMIENZO DEL JUEGO, LAS STATS Y "QUITAR" JUEGO
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        #CREA UNA VENTANA
        self.root = root
        # CON EL TÍTULO "Juego de Cartas"
        self.root.title("Juego de Cartas")

        #CREA BOTONES PERTENECIENTES A ROOT, CON UN TEXTO DENTRO Y COMO COMANDOS LA LÓGICA QUE VIENE DE "controlador.py"
        self.start_game_button = tk.Button(root, text="Jugar", command=start_game_callback)
        self.show_stats_button = tk.Button(root, text="Estadísticas", command=show_stats_callback)
        self.quit_button = tk.Button(root, text="Salir", command=quit_callback)

        #EMPAQUETAMOS BOTONES
        self.start_game_button.pack(pady=10)
        self.show_stats_button.pack(pady=10)
        self.quit_button.pack(pady=10)

    #LLEGA A ESTE MÉTODO, EL CUAL RETORNA UN DIÁLOGO EMERGENTE, CON UN ASKSTRING, QUE CONTIENE
    def ask_player_name(self):
        return simpledialog.askstring(
            #UN TITULO CON "Nombre del Jugador"
            "Nombre del Jugador",
            #"Ingresa tu nombre:" COMO CUERPO DE TEXTO
            "Ingresa tu nombre:",
            #Y UN CUADRO DE TEXTO QUE ALMACENARÁ LO QUE ESCRIBAMOS
            parent=self.root)