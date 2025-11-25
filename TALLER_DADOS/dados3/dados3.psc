Algoritmo dados3
	
	cara1 = 0;
	cara2 = 0;
	cara3 = 0;
	cara4 = 0;
	cara5 = 0;
	cara6 = 0;
	Escribir "Ingrese el número de veces que desea lanzar el dado:";
	Leer num_tiros;
	Para i = 1 Hasta num_tiros Con Paso 1 Hacer
    resultado = Aleatorio(1, 6);
    
    Si resultado = 1 Entonces
        cara1 = cara1 + 1;
    Sino
        Si resultado = 2 Entonces
            cara2 = cara2 + 1;
        Sino
            Si resultado = 3 Entonces
                cara3 = cara3 + 1;
            Sino
                Si resultado = 4 Entonces
                    cara4 = cara4 + 1;
                Sino
                    Si resultado = 5 Entonces
                        cara5 = cara5 + 1;
                    Sino
                        cara6 = cara6 + 1;
                    FinSi 
                FinSi 
            FinSi 
        FinSi 
    FinSi 
    

FinPara

Escribir "";
Escribir "resultados finales";
Escribir "Total de tiros: ", num_tiros;
Escribir "";

Escribir "El número 1 salió: ", cara1, " veces.";
Escribir "El número 2 salió: ", cara2, " veces.";
Escribir "El número 3 salió: ", cara3, " veces.";
Escribir "El número 4 salió: ", cara4, " veces.";
Escribir "El número 5 salió: ", cara5, " veces.";
Escribir "El número 6 salió: ", cara6, " veces.";
FinAlgoritmo


