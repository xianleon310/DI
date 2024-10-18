import tkinter as tk
from tkinter import scrolledtext

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 10")
root.geometry("300x200")

# Crear un widget Text con Scrollbar
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
text_area.pack(expand=True, fill='both')

    # Texto largo para mostrar
long_text = (
    "Este es un ejemplo de un widget Text en Tkinter.\n\n"
    "Tkinter es la biblioteca estándar para crear interfaces gráficas en Python.\n"
    "Puedes añadir varios párrafos de texto y usar una barra de desplazamiento para navegar.\n\n"
    "Este texto es solo un ejemplo. Puedes reemplazarlo con cualquier otro texto largo que desees.\n"
    "Recuerda que el uso de Scrollbars es esencial para mejorar la usabilidad de tu aplicación.\n\n"
    "Si tienes un texto muy largo, una barra de desplazamiento será muy útil.\n"
    "Aquí tienes otro párrafo para que veas cómo se comporta:\n\n"
    "Este es el último párrafo. Asegúrate de probar el desplazamiento hacia abajo y hacia arriba.\n"
    "¡Espero que esto te ayude en tu proyecto con Tkinter!"
)

# Insertar el texto en el widget Text
text_area.insert(tk.END, long_text)

root.mainloop()

