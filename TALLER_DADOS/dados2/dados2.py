import os
from random import randint

suma = 0

numeroveces = int(input("¿Cuántas veces desea lanzar el dado? "))

for variable in range(1, numeroveces + 1):
    dado = randint(1, 6)
    suma += dado

print("La suma total de los valores generados es:", suma)