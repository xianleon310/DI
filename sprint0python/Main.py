from Heroe import Heroe
from Mazmorra import Mazmorra


def main():
    #Guardamos en la variable "nombre_heroe" lo que escribamos vía teclado
    nombre_heroe=input("Introduce el nombre de tu héroe: ")


    #Creamos un objeto "heroe", en el cual se guardarán los datos de la clase "Heroe" que llevará el nombre que escribamos vía teclado
    #-CLASE HÉROE->*
    heroe= Heroe(nombre_heroe)


    #Creamos una variable "mazmorra", en la cual se guardará los datos de la clase "Mazmorra" que llevará el objeto del héroa, llamado "heroe"
    #-CLASE MAZMORRA->*
    mazmorra=Mazmorra(heroe)


    #Viajamos al método "jugar" de la clase mazmorra
    #-CLASE MAZMORRA ->*
    mazmorra.jugar()

if __name__ == "__main__":
    main()
