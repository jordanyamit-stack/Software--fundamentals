Algoritmo reto_1
	Definir dado1, dado2 Como Entero
	// DATOS
	dado1 <- Aleatorio(1,6)
	dado2 <- Aleatorio(1,6)
	// INTERACCION
	Escribir 'Numero del dado 1 ', dado1
	Escribir 'Numero del dao 2: ', dado2
	// PROSESO
	Escribir '---'
	Si dado1 MOD 2=0 Entonces
		Escribir 'Dado 1 (', dado1, ') es PAR.'
	SiNo
		Escribir 'Dado 1 (', dado1, ') es IMPAR.'
	FinSi
	Si dado2 MOD 2=0 Entonces
		Escribir 'Dado 2 (', dado2, ') es PAR.'
	SiNo
		Escribir 'Dado 2 (', dado2, ') es IMPAR.'
	FinSi
	Si dado1=dado2 Entonces
		Escribir 'YOU WIN'
	SiNo
		Escribir 'GAME OVER'
	FinSi
FinAlgoritmo
