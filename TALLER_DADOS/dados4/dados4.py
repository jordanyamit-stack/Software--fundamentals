import os
from random import randint

salir = 0

while salir == 0:

    veces = int(input("¿Cuántas veces desea lanzar los dados? "))

    contador = 0

    while contador < veces:

        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        contador += 1

        print("Lanzamiento", contador, ":  Dado1 =", dado1, " Dado2 =", dado2)

        if dado1 == 6 and dado2 == 6:
            print("¡SALIO PAR DE SEIS! Fin del programa.")
            salir = 1
            contador = veces
