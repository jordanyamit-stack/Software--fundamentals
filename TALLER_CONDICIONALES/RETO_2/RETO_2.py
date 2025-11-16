def RETO_CONDICIONAL():
    try:
        numero = int(input("Ingrese un número entero (positivo o negativo): "))

        if numero % 2 == 0:
            print(f"El numero {numero} es PAR.")
        else:
            print(f"El numero {numero} es IMPAR.")

    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    RETO_CONDICIONAL()