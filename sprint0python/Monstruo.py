import random
class Monstruo:
    def __init__(self):
        # <-*Llega a esta clase y guarda en una lista unos nombres
        lista=["Jacobo","Diego","Iago","Ricardo","Arturo","Carlos","Rebeca","Marcos","Pablo"]


        #Escoge un nombre random de dicha lista
        self.nombre=random.choice(lista)


        #Y lo elimina, para que así, cuando vuelvan a llamar al método no vuelva a coincidir dicho nombre
        lista.remove(self.nombre)


        self.ataque=10
        self.defensa=4
        self.salud=100

    def atacar(self, heroe):
        daño = self.ataque - heroe.defensa
        print("Monstruo " + self.nombre + " ataca a " + heroe.nombre + ".")
        if daño > 0:
            heroe.salud = heroe.salud- daño
            print("El héroe " + heroe.nombre + " ha recibido " + str(
                daño) + " puntos de daño.")  # Convertir daño a string
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        return self.salud > 0
