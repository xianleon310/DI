import tkinter as tk
#IMPORTES NECESARIOS PARA LAS VENTANAS Y DIALOGOS SECUNDARIOS DE LA INTERFAZ
from tkinter import simpledialog,Toplevel
from controlador import GameController

class GameView:
    def __init__(self,on_card_click_callback,update_move_count_callback,update_time_callback):
        self.window=Toplevel()
        self.labels=[]
        self.on_card_click_callback=on_card_click_callback
        self.update_move_count_callback=update_move_count_callback
        self.update_time_callback=update_time_callback

    def create_board(self,model):
        pass

    def update_board(self,pos,image_id):
        pass

    def reset_cards(self,pos1,pos2):
        pass

    def update_move_count(self,moves):
        pass

    def update_time(self,time):
        pass

    def destroy(self):
        pass


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.root = root
        self.root.title("Juego de Cartas")

        # Crear botones
        self.start_game_button = tk.Button(root, text="Jugar", command=start_game_callback)
        self.show_stats_button = tk.Button(root, text="Estadísticas", command=show_stats_callback)
        self.quit_button = tk.Button(root, text="Salir", command=quit_callback)

        # Empaquetar botones para que se vean
        self.start_game_button.pack(pady=10)
        self.show_stats_button.pack(pady=10)
        self.quit_button.pack(pady=10)