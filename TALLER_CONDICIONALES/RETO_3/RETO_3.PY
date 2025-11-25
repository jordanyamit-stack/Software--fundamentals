'''DIGITAR NUMERO Y LEERLO'''
numero = int(input("DIGITE EL NUMERO "))
'''PROSESO'''
if numero % 2 == 0:

    if numero > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:

    if numero > 0:
        print("Impar positivo")
    else:
        print("Impar negativo")
