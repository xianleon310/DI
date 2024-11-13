import threading
import random
import requests
#from recursos import descargar_imagen

def __init__(self,difficulty,player_name,cell_size=100):
    self.difficulty=difficulty
    self.player_name=player_name
    self.cell_size=cell_size
    self.cards = None
    self.images = {}  # Diccionario para almacenar las imágenes descargadas
    self.images_loaded = threading.Event()  # Evento para indicar que las imágenes están cargadas
    self.hidden_image = None
    self.url_base = "https://github.com/tu_repo_de_imagenes/"
    self.listaimages=(
        "1200px-Bellibolt.png",
        "ai-generated-8584912_1280.jpg",
        "badge-7038441_1280.png",
        "butterfly-4526146_1280.jpg",
        "diglett-6251282_1280.jpg",
        "eevee-7334613_1280.jpg",
        "eevee-7792964_1280.png",
        "gengar-5432819_1280.png",
        "magikarp-1536179_1280.png",
        "masquerain-7409356_1280.png",
        "pixel-3316924_1280.png",
        "pokemon-1536849_1280.png",
        "pokemon-1656997_1280.png",
        "pokemon-1888657_1280.png",
        "pokemon-4100742_1280.jpg",
        "pokemon-4784551_1280.png",
        "pokemon-5101360_1280.jpg",
        "pokemon-5426712_1920.png",
        "pokemon-5432874_1280.png",
        "pokemon-6311724_1280.jpg",
        "pokemon-6895600_1920.png",
        "pop-5475382_1280.jpg",
        "pop-5475390_1280.jpg",
        "relaxo-1646949_1280.jpg",
        "scary-1778169_1280.jpg",
        "sea-7769708_1280.jpg",
        "snowman-4721285_1280.jpg",
        "squirtle-7400933_1280.jpg",
        "toy-5051773_1280.jpg",
        "toys-5353967_1280.jpg",
        "toys-5353969_1280.jpg",
        "white-male-1778182_1280.jpg",
    )
    self._generate_board()
    self._load_images()

def _generate_board(self):
    if self.difficulty=="8x8":
        numpares=32
    if self.difficulty=="4x4":
        numpares=8
    if self.difficulty=="6x6":
        numpares=16
    listacartas=list(range(numpares))
    random.shuffle(listacartas)
    self.cards = [listacartas[i:i + int(self.difficulty[0])] for i in range(0, len(listacartas), int(self.difficulty[0]))]

def _load_images(self):
    pass

def load_images_thread(self):
    pass

#self.cards=self.img_names[:num_pares]*2