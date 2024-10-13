from operaciones import suma, resta, multiplicacion, division
sw=0
while (sw==0):
    numero1 = int(input('Teclea el primer número:'))
    numero2 = int(input('Teclea el segundo número: '))
    respuesta = input('¿Qué operación quieres realizar?(suma/resta/multiplicacion/division')
    if (respuesta == 'suma'):
        print(suma(numero1, numero2))
    if (respuesta == 'resta'):
        print(resta(numero1, numero2))
    if (respuesta == 'multiplicacion'):
        print(multiplicacion(numero1, numero2))
    if (respuesta == 'division'):
        print(division(numero1, numero2))
    otra=input('¿Quieres hacer otra operación?(s/n)')
    if (otra=='n'):
        sw=1