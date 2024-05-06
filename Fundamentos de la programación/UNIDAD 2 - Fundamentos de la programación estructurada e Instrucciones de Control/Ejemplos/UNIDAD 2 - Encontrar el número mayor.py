# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número "))

# Comparar los números e imprimir el número mayor
if  num1 == num2:
    print("Los números son iguales.")
elif num1 > num2:
    print("El número mayor es", num1)
else:
    print("El número mayor es", num2)
