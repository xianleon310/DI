class Heroe:
    def __init__(self, nombre):
        #<-*Llega a esta clase y trae el nombre del teclado procedente del main y crea un objeto con el nombre y características predeterminadas
        #(ataque,defensa,salud,salud_maxima)
        self.nombre = nombre
        self.ataque = 30
        self.defensa = 7
        self.salud = 100
        self.salud_maxima = 100

    def atacar(self, enemigo):
        daño=self.ataque-enemigo.defensa
        print("Héroe "+self.nombre+" ataca a "+enemigo.nombre+".")
        if (daño>0):
            enemigo.salud = enemigo.salud - daño
            print("El enemigo" + enemigo.nombre + " ha recibido " + str(daño) + " puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        self.salud=self.salud+10
        if (self.salud>self.salud_maxima):
            self.salud=self.salud_maxima
        print("Héroe se ha curado. Salud actual: "+str(self.salud))

    def defenderse(self):
        self.defensa=self.defensa+5
        print("Héroe se defiende. Defensa aumentada temporalmente a "+str(self.defensa)+".")

    def reset_defensa(self):
        self.defensa=self.defensa-5
        print("La defensa de "+self.nombre+" vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0
