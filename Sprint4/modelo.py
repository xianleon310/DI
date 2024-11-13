import threading
import random
from datetime import time

from recursos import descargar_imagen

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.cards = None
        self.images = {}  # Diccionario para almacenar las imágenes descargadas
        self.images_loaded = threading.Event()  # Evento para indicar que las imágenes están cargadas
        self.hidden_image = None
        self.url_base = "https://raw.githubusercontent.com/xianleon310/DI/refs/heads/main/Sprint4/Imagenes"
        self.listaimages = (
            "1200px-Bellibolt.png", "ai-generated-8584912_1280.jpg", "badge-7038441_1280.png",
            "butterfly-4526146_1280.jpg", "diglett-6251282_1280.jpg", "eevee-7334613_1280.jpg",
            "eevee-7792964_1280.png", "gengar-5432819_1280.png", "magikarp-1536179_1280.png",
            "masquerain-7409356_1280.png", "pixel-3316924_1280.png", "pokemon-1536849_1280.png",
            "pokemon-1656997_1280.png", "pokemon-1888657_1280.png", "pokemon-4100742_1280.jpg",
            "pokemon-4784551_1280.png", "pokemon-5101360_1280.jpg", "pokemon-5426712_1920.png",
            "pokemon-5432874_1280.png", "pokemon-6311724_1280.jpg", "pokemon-6895600_1920.png",
            "pop-5475382_1280.jpg", "pop-5475390_1280.jpg", "relaxo-1646949_1280.jpg",
            "scary-1778169_1280.jpg", "sea-7769708_1280.jpg", "snowman-4721285_1280.jpg",
            "squirtle-7400933_1280.jpg", "toy-5051773_1280.jpg", "toys-5353967_1280.jpg",
            "toys-5353969_1280.jpg", "white-male-1778182_1280.jpg"
        )
        self._generate_board()
        self._load_images()
        self.start_time = None  # Variable para almacenar el tiempo de inicio

    def _generate_board(self):
        # Define numpares en función de la dificultad
        if self.difficulty == "facil":
            numpares = 8  # 4 pares de cartas
            board_size = 4
        elif self.difficulty == "medio":
            numpares = 18  # 8 pares de cartas
            board_size = 6
        elif self.difficulty == "dificil":
            numpares = 32  # 16 pares de cartas
            board_size = 8
        else:
            raise ValueError(f"Dificultad '{self.difficulty}' no válida. No se puede generar el tablero.")

        # Genera la lista de cartas con los pares
        listacartas = list(range(numpares)) * 2
        random.shuffle(listacartas)

        self.cards = [listacartas[i:i + board_size] for i in range(0, len(listacartas), board_size)]

    def _load_images(self):
        def load_images_thread():
            self.hidden_image = descargar_imagen(self.url_base + "/hidden.png", 100)

            # Crea una lista de IDs únicos para evitar duplicados
            unique_image_ids = []
            for row in self.cards:
                for image_id in row:
                    if image_id not in unique_image_ids:
                        unique_image_ids.append(image_id)

            # Descarga cada imagen única y la almacena en self.images
            for image_id in unique_image_ids:
                image_url = self.url_base + "/" + self.listaimages[image_id]
                self.images[image_id] = descargar_imagen(image_url, 100)

            # Indica que todas las imágenes se han cargado
            self.images_loaded.set()

        # Inicia el hilo de descarga de imágenes
        threading.Thread(target=load_images_thread, daemon=True).start()

    def start_timer(self):
        """Inicia el temporizador cuando se hace el primer clic."""
        self.start_time = time.time()  # Registra el tiempo de inicio

    def get_time_elapsed(self):
        """Devuelve el tiempo transcurrido desde que comenzó el juego."""
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)  # Devuelve el tiempo transcurrido en segundos