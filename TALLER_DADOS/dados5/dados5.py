import os
from random import randint

pares = 0
impares = 0

numeroLanzamientos = int(input("¿Cuántos lanzamientos va a efectuar? "))

for i in range(1, numeroLanzamientos + 1):
    dado = randint(1, 6)
    print("Lanzamiento", i, ":", dado)

    if dado % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Total de tiros pares:", pares)
print("Total de tiros impares:", impares)