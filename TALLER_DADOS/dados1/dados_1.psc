Algoritmo dados_1
	Definir dado1 Como Entero
	definir boton Como Caracter
	Escribir "OPRIMIR TECLADO PARA LANZAR"
	Leer boton
		dado1=Aleatorio(1,6)
		Escribir "el numero del dado es : ",dado1
		
		Si dado1 MOD 2=0 Entonces
			Escribir "Es par :"
		SiNo
			Escribir "no es par"
		Fin Si
FinAlgoritmo
