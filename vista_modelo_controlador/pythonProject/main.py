import tkinter as tk
from modelo import NotasModel
from vista import VistaNotas
from controlador import ControladorNotas

def main():
    root = tk.Tk()
    #VA A LA CLASE "NotasModel" Y CREA UNA LISTA VACÍA
    modelo = NotasModel()

    #VA A LA CLASE "VistaNotas" Y CREA WIDGETS Y DEMÁS
    vista = VistaNotas(root)

    #VA A LA CLASE CONTROLADOR Y HACE TODOS LOS COMANDOS, LLEVANDO LAS CLASES CORRESPONDIESTES AL MODELO Y LA VISTA ->
    controlador = ControladorNotas(modelo, vista)



    root.mainloop()

if __name__ == "__main__":
    main()