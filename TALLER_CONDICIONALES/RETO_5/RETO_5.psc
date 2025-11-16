Algoritmo sin_titulo
	Escribir 'Ingrese el tipo de identificación:'
	Leer tipoId
	Escribir 'Ingrese nombres:'
	Leer nombres
	Escribir 'Ingrese apellidos:'
	Leer apellidos
	Escribir 'Ingrese género (M/F):'
	Leer genero
	Escribir 'Ingrese año de nacimiento:'
	Leer anoNacimiento
	Escribir 'Ingrese dirección:'
	Leer direccion
	Escribir 'Ingrese teléfono:'
	Leer telefono
	Escribir 'Ingrese salario:'
	Leer salario
	Si salario<=1200000 Entonces
		Si genero='F' Entonces
			aumento <- salario*0.10
		SiNo
			aumento <- salario*0.08
		FinSi
	SiNo
		Si salario<2000000 Entonces
			aumento <- salario*0.05
		SiNo
			Si genero='F' Entonces
				aumento <- salario*0.03
			SiNo
				aumento <- salario*0.025
			FinSi
		FinSi
	FinSi
	salarioFinal <- salario+aumento
	Escribir 'Salario final: ', salarioFinal
FinAlgoritmo
