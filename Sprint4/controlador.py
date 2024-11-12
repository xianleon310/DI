from tkinter import messagebox


class GameController:
    def __init__(self, root):
        self.root = root

    def start_game_callback(self):
        # Lo que hace cuando se presiona "Jugar"
        messagebox.showinfo("Acción", "Has seleccionado 'Jugar'")

    def show_stats_callback(self):
        # Lo que hace cuando se presiona "Estadísticas"
        messagebox.showinfo("Acción", "Has seleccionado 'Estadísticas'")

    def quit_callback(self):
        # Lo que hace cuando se presiona "Salir"
        self.root.quit()  # Esto cierra la aplicación