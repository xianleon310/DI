from Monstruo import Monstruo
from Tesoro import Tesoro


class Mazmorra:
    def __init__(self,heroe):
        #<-*Llega a esta clase y trae el nombre del teclado procedente del main y crea un objeto con el nombre y dos objetos
        #(monstruos,tesoro)
        self.heroe=heroe


        #Guarda en la variable "monstruos" una lista de 3 objetos, por lo que irá a la clase "Monstruo()" a definir los valores
        #CLASE MONSTRUO->*
        self.monstruos=[Monstruo(),Monstruo(), Monstruo()]


        #Guarda en la variable "tesoro" los valores de la clase "Tesoro()"
        #CLASE TESORO->*
        self.tesoro=Tesoro()

    #<-*Se ejecuta el método, hay que recordar que en esta clase se han guardado los valores de las siguientes clases:
    #   -El objeto "Heroe()"
    #   -3 objetos "Monstruo()"
    #   -1 objeto "Tesoro()"
    def jugar(self):
        i = 0
        print("Héroe " + self.heroe.nombre + " entra en la mazmorra.")
        print("Te has encontrado con un " + self.monstruos[i].nombre + ".")
        while i < len(self.monstruos) and self.heroe.esta_vivo():
            self.enfrentar_enemigo(self.monstruos[i])
            if not self.monstruos[i].esta_vivo():
                i += 1
                self.tesoro.encontrar_tesoro(self.heroe)
                if i != len(self.monstruos):
                    print("Te has encontrado con un " + self.monstruos[i].nombre + ".")
        if self.heroe.esta_vivo():
            print("¡" + self.heroe.nombre + " ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print("Héroe ha sido derrotado en la mazmorra.")

    def enfrentar_enemigo(self, enemigo):
        sw = 0
        while sw == 0 and self.heroe.esta_vivo() and enemigo.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defenderse")
            print("3. Curarse")
            opcion = int(input())
            if opcion != 1 and opcion != 2 and opcion != 3:
                print("Opción no válida.")
            else:
                sw = 1
                if opcion == 1:
                    self.heroe.atacar(enemigo)  # Llama al ataque del héroe
                    if enemigo.esta_vivo():  # Verifica si el enemigo sigue vivo
                        enemigo.atacar(self.heroe)  # Llama al ataque del enemigo
                elif opcion == 2:
                    self.heroe.defenderse()
                    enemigo.atacar(self.heroe)  # El enemigo ataca
                    self.heroe.reset_defensa()  # Restaura la defensa del héroe
                elif opcion == 3:
                    self.heroe.curarse()
                    enemigo.atacar(self.heroe)  # El enemigo ataca
