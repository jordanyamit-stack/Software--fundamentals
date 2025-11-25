import os
from random import randint


cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0

num_tiros = int(input("Ingrese el número de veces que desea lanzar el dado: "))

for i in range(1, num_tiros + 1):
    resultado = randint(1, 6)
    
    if resultado == 1:
        cara1 += 1
    elif resultado == 2:
        cara2 += 1
    elif resultado == 3:
        cara3 += 1
    elif resultado == 4:
        cara4 += 1
    elif resultado == 5:
        cara5 += 1
    else:
        cara6 += 1


print("Total de lanzamientos:", num_tiros)
print()
print("El número 1 salio:", cara1, "veces.")
print("El número 2 salio:", cara2, "veces.")
print("El número 3 salio:", cara3, "veces.")
print("El número 4 salio:", cara4, "veces.")
print("El número 5 salio:", cara5, "veces.")
print("El número 6 salio:", cara6, "veces.")