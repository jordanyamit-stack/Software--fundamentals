Algoritmo Dados6
	
    Definir dado, totalTiros, suma, pares, impares Como Entero
    Definir respuesta Como Caracter
	
    totalTiros = 0
    suma = 0
    pares = 0
    impares = 0
	
    Escribir "¿Desea lanzar el dado? (S/N)"
    Leer respuesta
    respuesta = Mayusculas(respuesta)
	
    Mientras respuesta = "S" Hacer
		
        dado = Aleatorio(1,6)
        Escribir "Salio ", dado
		
        totalTiros = totalTiros + 1
        suma = suma + dado
		
        Si dado % 2 = 0 Entonces
            pares = pares + 1
        Sino
            impares = impares + 1
        FinSi
		
        Escribir "¿Desea volver a lanzar? S/N"
        Leer respuesta
        respuesta = Mayusculas(respuesta)
		
    FinMientras
	

    Escribir "Total de tiros efectuados ", totalTiros
    Escribir "Suma total de los tiros ", suma
    Escribir "Total de pares generados ", pares
    Escribir "Total de impares generados ", impares

FinAlgoritmo
