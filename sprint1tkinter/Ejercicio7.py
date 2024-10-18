import tkinter as tk
def dibujar_figuras():
    #LLEGA AL MÉTODO Y:

    #RECOGE EL VALOR QUE SE HA PUESTO EN LOS ENTRY SIN LA COMA EN LA VARIABLE DEL RECTANGULO PARA CREARLO
    coords_rect = entry_coords_rect.get().split(",")
    #SI HAY CUATRO ELEMENTOS (LA LONGITUD DE LA LISTA ES IGUAL A 4):
    if len(coords_rect) == 4:
        #map() ESTÁ APLICANDO LA FUNCIÓN INT A CADA ELEMENTO DE LA LISTA
        x1_rect, y1_rect, x2_rect, y2_rect = map(int, coords_rect)
        #NECESARIO BORRAR EN CADA EJECUCIÓN
        canvas.delete("all")
        #CREAR EL RECTÁNGULO CON LOS VALORES PASADOS A INT QUE SE HAN RECIBIDO EN EL ENTRY
        canvas.create_rectangle(x1_rect, y1_rect, x2_rect, y2_rect, outline="blue", width=2)

    # RECOGE EL VALOR QUE SE HA PUESTO EN LOS ENTRY SIN LA COMA EN LA VARIABLE DEL RECTANGULO PARA CREARLO
    coords_circle = entry_coords_circle.get().split(",")
    if len(coords_circle) == 4:
        # map() ESTÁ APLICANDO LA FUNCIÓN INT A CADA ELEMENTO DE LA LISTA
        x1_circle, y1_circle, x2_circle, y2_circle = map(int, coords_circle)
        # CREAR EL CÍRCULO CON LOS VALORES PASADOS A INT QUE SE HAN RECIBIDO EN EL ENTRY
        canvas.create_oval(x1_circle, y1_circle, x2_circle, y2_circle, outline="red", width=2)


root = tk.Tk()
root.title("Ejercicio 7")
root.geometry("500x500")

#CREA PANTALLA EN BLANCO CON LAS SIGUIENTES MEDIDAS DENTRO DE LA VENTANA
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=20)

#DEBAJO DE LA PANTALLA BLANCA CREA UNA ETIQUETA CON UN TEXTO
tk.Label(root, text="Rectángulo (x1,y1,x2,y2)").pack()
#Y UN ENTRY PARA PODER ESCRIBIR LAS COORDENADAS
entry_coords_rect = tk.Entry(root)
entry_coords_rect.pack()

#DEBAJO DE LA PANTALLA BLANCA CREA UNA ETIQUETA CON UN TEXTO
tk.Label(root, text="Círculo (x1,y1,x2,y2)").pack()
#Y UN ENTRY PARA PODER ESCRIBIR LAS COORDENADAS
entry_coords_circle = tk.Entry(root)
entry_coords_circle.pack()

#CREA UN BOTÓN CON EL TEXTO "DIBUJAR FIGURAS EN EL CUAL SE EJECUTA LO DEL MÉTODO--
boton_dibujar = tk.Button(root, text="Dibujar Figuras", command=dibujar_figuras)
boton_dibujar.pack()

root.mainloop()
