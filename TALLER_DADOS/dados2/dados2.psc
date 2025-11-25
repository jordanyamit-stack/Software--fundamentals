Algoritmo dados2		
		Definir numeroveces, variable, dado, suma Como Entero
		suma = 0
		
		Escribir "¿Cuántas veces desea lanzar el dado?"
		Leer numeroveces
		
		Para variable = 1 Hasta numeroveces Con Paso 1 Hacer
			dado = Aleatorio(1,6)
			suma = suma + dado
		FinPara
		Escribir "La suma total de los valores generados es: ", suma
		

FinAlgoritmo
