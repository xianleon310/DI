class NotasModel:
    def __init__(self):
        #CREA UNA LISTA LLAMADA "notas"
        self.notas = []

    def agregar_nota(self, nueva_nota):
        #ALMACENA EN LA LISTA LA NOTA PASADA POR PARÁMETRO
        self.notas.append(nueva_nota)

    def eliminar_nota(self, indice):
        #ELIMINA DE LA LISTA LA NOTA PASADA POR PARÁMETRO
        del self.notas[indice]

    def obtener_notas(self):
        #MUESTRA LA LISTA CON TODAS LAS NOTAS
        return self.notas

    def guardar_notas(self):
        #ABRE EL FICHERO COMO LECTURA Y LE DÁ EL VALOR COMO LA VARIABLE "archivo"
        with open('notas.txt', 'w') as archivo:
            #HACE UN BUCLE FOR POR LO QUE CADA LINEA DE LA LISTA ESCRIBIRÁ EN EL ARCHIVO
            #ESPECIFICADO EN LA LÍNEA ANTERIOR (notas.txt)
            for linea in self.notas:
                archivo.write(linea+"\n")

    def cargar_notas(self):
        #MARCAMOS LA LISTA COMO VACÍA PARA QUE NO SALGAN LOS VALORES DUPLICADOS
        self.notas=[]
        #ABRE EL FICHERO COMO ESCRITURA Y LE DÁ EL VALOR COMO LA VARIABLE "archivo"
        with open('notas.txt', 'r') as archivo:
            #HACE UN BUCLE FOR POR LO QUE CADA LINEA DE LA VARIABLE "archivo" (notas.txt)
            #ES AÑADIDA A LA LISTA "notas". (EL ".strip()" ES PARA ELIMINAR CUALQUIER ESPACIO
            #EN BLANCO O CARACTERES DE NUEVA LÍNEA, ES COMPLEMENTARIO.
            for linea in archivo:
                self.notas.append(linea.strip())

