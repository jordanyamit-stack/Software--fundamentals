import os
from random import randint

dado = 0
totalTiros = 0
suma = 0
pares = 0
impares = 0

respuesta = input("¿Desea lanzar el dado? (S/N): ").upper()

while respuesta == "S" or respuesta=="s":

    dado = randint(1, 6)
    print("Salió:", dado)

    totalTiros += 1
    suma += dado

    if dado % 2 == 0:
        pares += 1
    else:
        impares += 1

    respuesta = input("¿Desea volver a lanzar? (S/N): ")

print("Total de tiros efectuados:", totalTiros)
print("Suma total de los tiros:", suma)
print("Total de pares generados:", pares)
print("Total de impares generados:", impares)