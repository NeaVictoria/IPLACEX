# Solicitar ingresar un número al usuario
numero = int(input("Ingrese un número: "))

# Determinar que mnensaje imprimir
if numero == 1:
    print("Es uno")
elif numero == 2:
    print("Es dos")
elif numero in [3,4]:
    print("Es tres o cuatro")
else:
    print("No es, 1, 2, 3 ni 4")