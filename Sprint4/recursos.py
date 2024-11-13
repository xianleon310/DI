import requests
from PIL import Image, ImageTk
from io import BytesIO

def descargar_imagen(url, size):
    print(f"Descargando imagen de {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = Image.open(BytesIO(response.content))
        image = image_data.resize((size, size), Image.LANCZOS)
        return ImageTk.PhotoImage(image)  # Aquí usamos directamente `image`
    except:
        return None
