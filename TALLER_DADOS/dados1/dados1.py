import os
from random import randint

input("OPRIMIR TECLADO PARA LANZAR ")

dado1 = randint(1, 6)
print("El número del dado es:", dado1)

if dado1 % 2 == 0:
    print("Es par")
else:
    print("No es par")