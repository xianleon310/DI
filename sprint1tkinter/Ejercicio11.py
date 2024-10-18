import tkinter as tk  # IMPORTA EL MÓDULO TKINTER

def update_label(value):  # DEFINE UNA FUNCIÓN PARA ACTUALIZAR LA ETIQUETA
    label.config(text=f"Valor seleccionado:"+value)  # ACTUALIZA EL TEXTO DE LA ETIQUETA CON EL VALOR SELECCIONADO

# CREAR LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Barra Deslizante")  # ESTABLECE EL TÍTULO DE LA VENTANA

# CREAR UNA ETIQUETA PARA MOSTRAR EL VALOR
label = tk.Label(root, text="Valor seleccionado: 0", font=("Arial", 14))  # INICIALIZA LA ETIQUETA CON UN VALOR INICIAL
label.pack(pady=20)  # AGREGA LA ETIQUETA A LA VENTANA Y AÑADE ESPACIO VERTICAL

# CREAR LA BARRA DESLIZANTE (SCALE)
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_label)  # CONFIGURA LA BARRA DESLIZANTE DE 0 A 100
scale.pack(pady=20)  # AGREGA LA BARRA DESLIZANTE A LA VENTANA Y AÑADE ESPACIO VERTICAL


root.mainloop()
