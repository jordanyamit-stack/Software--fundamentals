import os
os.system("clear")

# Iniciar contadores
empleados = []     # debe ser lista
contador_empleados = 0
contador_gender_f = 0
contador_gender_m = 0
contador_gender_o = 0
total_salario = 0
suma_edades = 0

agregar_otro = "s"

# Pedimos los datos solicitados
while agregar_otro.lower() == "s":

    name = input("Ingrese su nombre de usuario: ")
    email = input("Ingrese su correo electrónico: ")
    phone = input("Ingrese su número telefónico: ")

    # Validar género
    gender = input("Ingrese su género (M/F/O): ")
    while gender.upper() not in ["M", "F", "O"]:
        print("Género inválido. Por favor ingrese M, F u O.")
        gender = input("Ingrese su género (M/F/O): ")

    salary = int(input("Ingrese su salario mensual: "))
    year = int(input("Ingrese su año de nacimiento: "))

    # Calcular edad actual 
    edad = 2025 - year

    # Crear registro del empleado
    empleado = {
        "Nombre": name,
        "Correo": email,
        "Género": gender.upper(),
        "Salario": salary,
        "Teléfono": phone,
        "Año de nacimiento": year,
        "Edad": edad
    }

    empleados.append(empleado)

    # Actualizar contadores
    contador_empleados += 1
    total_salario += salary
    suma_edades += edad

    if gender.upper() == "M":
        contador_gender_m += 1
    elif gender.upper() == "F":
        contador_gender_f += 1
    else:
        contador_gender_o += 1

    # Validación para agregar otro
    agregar_otro = input("¿Desea registrar otro empleado? (s/n): ").lower()
    while agregar_otro not in ["s", "n"]:
        print("Entrada inválida. Por favor ingrese 's' o 'n'.")
        agregar_otro = input("¿Desea registrar otro empleado? (s/n): ").lower()

    if agregar_otro == "n":
        print("Saliendo del registro de empleados.\n")

# Resultados finales
print("===== RESUMEN DE REGISTROS =====")
print("Total de empleados registrados:", contador_empleados)
print("Total de empleados masculinos:", contador_gender_m)
print("Total de empleados femeninos:", contador_gender_f)
print("Total de empleados de otro género:", contador_gender_o)
print("Salario total de todos los empleados:", total_salario)
print("Promedio de edades:", suma_edades / contador_empleados if contador_empleados > 0 else 0)

print("\n===== LISTA DE EMPLEADOS =====")
for emp in empleados:
    print(emp)
