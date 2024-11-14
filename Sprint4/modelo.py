import os
import threading
import random
from datetime import time, datetime

from recursos import descargar_imagen

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.cards = None
        self.images = {}  # DICCIONARIO PARA ALMACENAR LAS IMÁGENES DESCARGADAS
        self.images_loaded = threading.Event()  # EVENTO PARA INDICAR QUE LAS IMÁGENES ESTÁN CARGADAS
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
        self._generate_board()  # GENERA EL TABLERO SEGÚN LA DIFICULTAD
        self._load_images()  # CARGA LAS IMÁGENES PARA LAS CARTAS
        self.start_time = None  # VARIABLE PARA ALMACENAR EL TIEMPO DE INICIO

    def _generate_board(self):
        # DEFINE NUMPARES EN FUNCIÓN DE LA DIFICULTAD
        if self.difficulty == "facil":
            numpares = 8  # 4 PARES DE CARTAS
            board_size = 4
        elif self.difficulty == "medio":
            numpares = 18  # 8 PARES DE CARTAS
            board_size = 6
        elif self.difficulty == "dificil":
            numpares = 32  # 16 PARES DE CARTAS
            board_size = 8
        else:
            raise ValueError(f"DIFICULTAD '{self.difficulty}' NO VÁLIDA. NO SE PUEDE GENERAR EL TABLERO.")

        # GENERA LA LISTA DE CARTAS CON LOS PARES
        listacartas = list(range(numpares)) * 2
        random.shuffle(listacartas)

        self.cards = [listacartas[i:i + board_size] for i in range(0, len(listacartas), board_size)]

    def _load_images(self):
        def load_images_thread():
            self.hidden_image = descargar_imagen(self.url_base + "/hidden.png", 100)

            # CREA UNA LISTA DE IDS ÚNICOS PARA EVITAR DUPLICADOS
            unique_image_ids = []
            for row in self.cards:
                for image_id in row:
                    if image_id not in unique_image_ids:
                        unique_image_ids.append(image_id)

            # DESCARGA CADA IMAGEN ÚNICA Y LA ALMACENA EN self.images
            for image_id in unique_image_ids:
                image_url = self.url_base + "/" + self.listaimages[image_id]
                self.images[image_id] = descargar_imagen(image_url, 100)

            # INDICA QUE TODAS LAS IMÁGENES SE HAN CARGADO
            self.images_loaded.set()

        # INICIA EL HILO DE DESCARGA DE IMÁGENES
        threading.Thread(target=load_images_thread, daemon=True).start()

    def start_timer(self):
        # INICIA EL TEMPORIZADOR CUANDO SE HACE EL PRIMER CLIC
        self.start_time = time.time()  # REGISTRA EL TIEMPO DE INICIO

    def get_time_elapsed(self):
        # DEVUELVE EL TIEMPO TRANSCURRIDO DESDE QUE COMENZÓ EL JUEGO
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)  # DEVUELVE EL TIEMPO TRANSCURRIDO EN SEGUNDOS

    def save_score(self, nombre, dificultad, movimientos):
        # GUARDA LA PUNTUACIÓN EN EL ARCHIVO RANKING.TXT
        fecha = datetime.now().strftime("%Y-%m-%d")
        new_score = f"{nombre},{dificultad},{movimientos},{fecha}\n"
        if not os.path.exists("ranking.txt"):
            open("ranking.txt", "w").close()

        with open("ranking.txt", "a") as file:
            file.write(new_score)

        # ORDENAR Y CONSERVAR LAS MEJORES TRES PUNTUACIONES
        self._ordenar_scores(dificultad)

    def _ordenar_scores(self, dificultad):
        # ORDENAR Y CONSERVAR LAS TRES MEJORES PUNTUACIONES DE CADA DIFICULTAD EN RANKING.TXT
        with open("ranking.txt", "r") as file:
            scores = file.readlines()

        scores = [line.strip().split(",") for line in scores if line]
        scores = sorted(
            [score for score in scores if score[1] == dificultad],
            key=lambda x: int(x[2])
        )[:3]

        # ESCRIBIR SOLO LAS TRES MEJORES PUNTUACIONES DE CADA DIFICULTAD
        with open("ranking.txt", "w") as file:
            for score in scores:
                file.write(",".join(score) + "\n")

    def load_scores(self):
        # CARGA LAS PUNTUACIONES DESDE RANKING.TXT Y DEVUELVE UN DICCIONARIO POR DIFICULTAD
        scores_by_difficulty = {"facil": [], "medio": [], "dificil": []}
        if os.path.exists("ranking.txt"):
            with open("ranking.txt", "r") as file:
                for line in file:
                    nombre, dificultad, movimientos, fecha = line.strip().split(",")
                    score = {"nombre": nombre, "movimientos": int(movimientos), "fecha": fecha}
                    scores_by_difficulty[dificultad].append(score)
        return scores_by_difficulty
