import tkinter as tk
from tkinter import simpledialog, Toplevel

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback, game_model):
        # CREAR UNA VENTANA SECUNDARIA EN LA INTERFAZ PRINCIPAL
        self.window = Toplevel()
        self.labels = []  # LISTA PARA ALMACENAR ETIQUETAS ADICIONALES, SI ES NECESARIO
        # CALLBACKS (FUNCIONES QUE SE EJECUTARÁN EN EVENTOS ESPECÍFICOS)
        self.on_card_click_callback = on_card_click_callback  # CALLBACK CUANDO SE HACE CLIC EN UNA CARTA
        self.update_move_count_callback = update_move_count_callback  # CALLBACK PARA ACTUALIZAR MOVIMIENTOS
        self.update_time_callback = update_time_callback  # CALLBACK PARA ACTUALIZAR TIEMPO
        # MODELO DEL JUEGO, QUE ALMACENA EL ESTADO DE LAS CARTAS, IMÁGENES, ETC.
        self.game_model = game_model
        self.buttons = []  # LISTA PARA ALMACENAR LOS BOTONES DEL TABLERO
        self.is_active = True  # BANDERA PARA INDICAR SI LA VENTANA ESTÁ ACTIVA

    def create_board(self, model):
        # CREAR EL MARCO PRINCIPAL DEL TABLERO EN LA VENTANA DE JUEGO
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        # ITERAR SOBRE CADA FILA EN EL MODELO (SUPONE QUE 'MODEL.CARDS' TIENE LAS CARTAS A MOSTRAR)
        for i, row in enumerate(model.cards):
            row_frame = tk.Frame(self.board_frame)  # CREAR UN MARCO PARA CADA FILA
            row_frame.pack()
            row_buttons = []  # LISTA TEMPORAL PARA ALMACENAR LOS BOTONES DE ESTA FILA
            for j, image_id in enumerate(row):
                # CREAR CADA BOTÓN CON LA IMAGEN OCULTA
                button = tk.Button(row_frame, image=model.hidden_image)
                button.grid(row=i, column=j)
                # CONFIGURAR EL COMANDO PARA MANEJAR CLICS EN EL BOTÓN DE LA CARTA
                button.config(command=lambda pos=(i, j): self.on_card_click_callback(pos))
                row_buttons.append(button)  # AÑADIR EL BOTÓN A LA LISTA DE BOTONES DE LA FILA
            self.buttons.append(row_buttons)  # AÑADIR LA FILA DE BOTONES A LA LISTA COMPLETA

    def update_board(self, pos, image_id, model):
        # ACTUALIZAR LA IMAGEN DEL BOTÓN EN LA POSICIÓN DADA
        i, j = pos  # OBTENER LAS COORDENADAS DE LA CARTA
        button = self.buttons[i][j]  # ACCEDER AL BOTÓN CORRESPONDIENTE EN LA LISTA
        button.config(image=model.images[image_id])  # ACTUALIZAR LA IMAGEN DEL BOTÓN

    def reset_cards(self, pos1, pos2):
        """OCULTAR LAS CARTAS DESPUÉS DE UN RETRASO SI NO COINCIDEN"""
        i1, j1 = pos1  # POSICIÓN DE LA PRIMERA CARTA
        i2, j2 = pos2  # POSICIÓN DE LA SEGUNDA CARTA
        # CONFIGURAR AMBAS CARTAS DE NUEVO CON LA IMAGEN OCULTA DEL MODELO
        self.buttons[i1][j1].config(image=self.game_model.hidden_image)
        self.buttons[i2][j2].config(image=self.game_model.hidden_image)

    def update_move_count(self, moves):
        # ACTUALIZAR EL CONTADOR DE MOVIMIENTOS EN LA VENTANA
        if hasattr(self, 'move_label'):
            self.move_label.config(text=f"Movimientos: {moves}")
        else:
            self.move_label = tk.Label(self.window, text=f"Movimientos: {moves}")
            self.move_label.pack()

    def update_time(self, time):
        # ACTUALIZAR EL CONTADOR DE TIEMPO SI LA VENTANA SIGUE ACTIVA
        if self.is_active:
            if hasattr(self, 'time_label') and self.time_label.winfo_exists():
                self.time_label.config(text=f"Tiempo: {time}s")
            else:
                # VERIFICAR SI LA VENTANA SIGUE ACTIVA ANTES DE INTENTAR AÑADIR EL LABEL
                if self.window.winfo_exists():
                    self.time_label = tk.Label(self.window, text=f"Tiempo: {time}s")
                    self.time_label.pack()

    def destroy(self):
        # MARCA LA VISTA COMO INACTIVA ANTES DE DESTRUIRLA PARA EVITAR ACTUALIZACIONES FUTURAS
        self.is_active = False
        self.window.destroy()


class MainMenu:
    # RECIBE EL ROOT, Y LAS FUNCIONES DE CALLBACK PARA INICIAR, MOSTRAR ESTADÍSTICAS, Y SALIR
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.root = root  # ALMACENA EL ROOT (VENTANA PRINCIPAL)
        self.root.title("Juego de Cartas")  # CONFIGURA EL TÍTULO DE LA VENTANA

        # CREAR BOTONES CON LAS FUNCIONES DE CALLBACK CORRESPONDIENTES
        self.start_game_button = tk.Button(root, text="Jugar", command=start_game_callback)
        self.show_stats_button = tk.Button(root, text="Estadísticas", command=show_stats_callback)
        self.quit_button = tk.Button(root, text="Salir", command=quit_callback)

        # EMPAQUETAR (MOSTRAR) LOS BOTONES CON UN ESPACIADO VERTICAL DE 10 PÍXELES
        self.start_game_button.pack(pady=10)
        self.show_stats_button.pack(pady=10)
        self.quit_button.pack(pady=10)

    def ask_player_name(self):
        # RETORNA UN CUADRO DE DIÁLOGO PARA SOLICITAR EL NOMBRE DEL JUGADOR
        return simpledialog.askstring(
            "Nombre del Jugador",  # TÍTULO DEL CUADRO DE DIÁLOGO
            "Ingresa tu nombre:",  # TEXTO DENTRO DEL CUADRO DE DIÁLOGO
            parent=self.root  # ESPECIFICA QUE EL CUADRO DE DIÁLOGO ES PARTE DEL ROOT
        )
