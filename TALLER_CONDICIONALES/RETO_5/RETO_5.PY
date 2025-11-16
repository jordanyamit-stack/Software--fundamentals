def reto_condicional_5():

    # Solicitud de datos
    try:
        genero = input("Ingrese su género (M: Mujer, H: Hombre): ").upper()
        salario_actual = float(input("Ingrese su salario actual (en COP): "))
    except ValueError:
        print("Error: Ingrese un valor numérico para el salario.")
        return

    aumento_porcentaje = 0.0

    # calculo del incremento salarial
    
 
    if salario_actual <= 1200000: 
        if genero == 'M':
            aumento_porcentaje = 0.10
        elif genero == 'H':
            aumento_porcentaje = 0.08
        
    elif 1200000 < salario_actual < 2000000: 
        aumento_porcentaje = 0.05

    #
    elif salario_actual >= 2000000:
        if genero == 'M':
            aumento_porcentaje = 0.03 
        elif genero == 'H':
            aumento_porcentaje = 0.025 
    
    # calculo del salario final
    salario_final = salario_actual * (1 + aumento_porcentaje)
# resultado
    print("---")
    print(f"Salario Actual: {salario_actual:,.2f} COP")
    print(f"Porcentaje de Aumento Aplicado: {aumento_porcentaje * 100:.1f} %")
    print(f"Salario Final: {salario_final:,.2f} COP")

if __name__ == "__main__":
    reto_condicional_5()