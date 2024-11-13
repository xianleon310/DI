import requests
from PIL import Image, ImageTk
from io import BytesIO

def descargar_imagen(url,size):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = Image.open(BytesIO(response.content))
        image=image_data.resize(size,Image.LANCZOS)
        return ImageTk.PhotoImage(Image.open(image))
    except:
        return None