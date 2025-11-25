tipoId = input("Ingrese el tipo de identificación: ")
nombres = input("Ingrese nombres: ")
apellidos = input("Ingrese apellidos: ")
genero = input("Ingrese género (M/F): ")
anoNacimiento = input("Ingrese año de nacimiento: ")
direccion = input("Ingrese dirección: ")
telefono = input("Ingrese teléfono: ")
salario = float(input("Ingrese salario: "))

if salario <= 1200000:
    if genero == 'F':
        aumento = salario * 0.10
    else:
        aumento = salario * 0.08
else:
    if salario < 2000000:
        aumento = salario * 0.05
    else:
        if genero == 'F':
            aumento = salario * 0.03
        else:
            aumento = salario * 0.025

salarioFinal = salario + aumento

print("Tipo de identificación:", tipoId)
print("Nombres:", nombres)
print("Apellidos:", apellidos)
print("Género:", genero)
print("Año de nacimiento:", anoNacimiento)
print("Dirección:", direccion)
print("Teléfono:", telefono)

print("----- SALARIO -----")
print("Salario inicial:", salario)
print("Aumento aplicado:", aumento)
print("Salario final:", salarioFinal)