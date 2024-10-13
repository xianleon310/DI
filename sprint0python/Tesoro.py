import random
class Tesoro:
    def __init__(self):
        # <-*La variable "beneficios será un número del 1 al 3 (aleatorio), el cual tendrá diferentes consecuencias según el que se genere
        self.beneficios=random.randint(1,3)

    def encontrar_tesoro(self,heroe):
        print("¡El héroe ha encontrado un tesoro!")
        if (self.beneficios==1):
            heroe.ataque = heroe.ataque + 5
            print ("El ataque del héroe "+heroe.nombre+" aumenta a "+str(heroe.ataque)+".")
        elif (self.beneficios==2):
                heroe.defensa = heroe.defensa + 5
                print("La defensa del héroe " + heroe.nombre + " aumenta a " + str(heroe.defensa)+".")
        elif (self.beneficios==3):
                heroe.salud = heroe.salud_maxima
                print("La salud del héroe " + heroe.nombre + " ha sido restaurada a " + str(heroe.salud_maxima)+".")

