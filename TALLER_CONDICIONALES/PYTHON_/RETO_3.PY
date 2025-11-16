'''DIGITAR NUMERO Y LEERLO'''
numero = int(input("DIGITE EL NUMERO "))
'''PROSESO'''
if numero % 2 == 0:
#POSITIVO
    if numero > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:
#NEGATIVO
    if numero > 0:
        print("Impar positivo")
    else:
        print("Impar negativo")
