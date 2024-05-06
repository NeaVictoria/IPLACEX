# Escribir un programa que permita ingresar la base y la altura para dos triángulos diferentes, Triángulo A y Triángulo B, y en virtud de ello imprima cuál es el que posee la mayor área. Si ambos poseen igual área lo deberá indicar.

# Función calculo área de triángulo
def calcular_area(base, altura):
    return (base * altura) / 2

# Solicitar al usuario ingreso de base y altura del Triángulo A
base_A = float(input("Ingrese la base del Triángulo A: "))
altura_A = float(input("Ingrese la altura del Triángulo A: "))

# Solicitar al usuario ingreso de base y altura del Triángulo B
base_B = float(input("Ingrese la base del Triángulo B: "))
altura_B = float(input("Ingrese la altura del Triángulo B: "))

# Calcular el área de cada triángulo
area_A =calcular_area(base_A, altura_A)
area_B = calcular_area(base_B, altura_B)

# Comparar las áreas y determinar cuál es mayor
if area_A > area_B:
    print("El Triángulo A tiene un área mayor que el Triángulo B.")
elif area_A < area_B:
    print("El Triángulo B tiene un área mayor que el Triángulo A.")
else:
    print("ambos triángulos tienen la misma área.")

# Imprimir las áreas calculadas
print("El área del Triángulo A es:", area_A)
print("El área del Triángulo B es:", area_B)