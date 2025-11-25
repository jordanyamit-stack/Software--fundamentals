Algoritmo ContarParesImpares
	Definir Veces, i, dado, pares, impares Como Entero
	pares = 0
	impares = 0
	Escribir '¿Cuántos lanzamientos va a efectuar?'
	Leer Veces
	Para i=1 Hasta Veces Con Paso 1 Hacer
		dado = Aleatorio(1,6)
		Escribir 'Lanzamiento ', i, ': ', dado
		Si dado MOD 2=0 Entonces
			pares = pares+1
		SiNo
			impares = impares+1
		FinSi
	FinPara
	Escribir 'Total de tiros pares: ', pares
	Escribir 'Total de tiros impares: ', impares
FinAlgoritmo
