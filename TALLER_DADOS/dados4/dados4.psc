Algoritmo dados4
	
    Definir veces, contador, d1, d2, salir Como Entero
    salir = 0    
	
    Mientras salir = 0 Hacer
		
        Escribir "¿Cuántas veces desea lanzar los dados?"
        Leer veces
		
        contador = 0
		
        Mientras contador < veces Hacer
			
            d1 = Aleatorio(1,6)
            d2 = Aleatorio(1,6)
            contador = contador + 1
			
            Escribir "Lanzamiento ", contador, ":  Dado1 = ", d1, "  Dado2 = ", d2
			
            Si d1 = 6 Y d2 = 6 Entonces
                Escribir "¡Salio par de seis! Fin del programa "
                salir = 1
                contador = veces 
            FinSi
			
        FinMientras
		
    FinMientras
	
FinAlgoritmo