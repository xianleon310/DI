import tkinter as tk
#from modelo import GameModel
from vista import MainMenu#,GameView
from controlador import GameController

if __name__ == "__main__":
    root = tk.Tk()
    game_controller = GameController(root)
    main_menu = MainMenu(root,
        game_controller.start_game_callback,  # Callback para "Jugar"
        game_controller.show_stats_callback,  # Callback para "Estadísticas"
        game_controller.quit_callback)  # Callback para "Salir"

        #FINAL
    root.mainloop()
def main():
    pass

