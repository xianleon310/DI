import tkinter as tk
from controlador import GameController

if __name__ == "__main__":
    root = tk.Tk()
    #CREAMOS UNA INSTANCIA GAMECONTROLLER, POR LO QUE VAMOS A DICHO ARCHIVO
    game_controller = GameController(root)
    #FINAL
    root.mainloop()
