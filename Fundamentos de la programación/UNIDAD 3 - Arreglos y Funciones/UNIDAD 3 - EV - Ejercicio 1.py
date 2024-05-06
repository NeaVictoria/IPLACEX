# Se le pide al usuario que ingrese el número N
N = int(input("Ingresar la cantidad de números a ingresar: "))

# Luego, se crea una lista vacía para almacenar los números.
lista = []

# Se llena la lista con N números ingresados por usuario
for i in range(N):
    num = int(input(f"Ingresar el número {i+1}: "))
    lista.append(num)

# Se ordena la lista en orden descendente
lista.sort(reverse=True)

# Imprime el tercer mayor número en la lista
if len(lista) >= 3:
    print(f"El tercer mayor número en la lista es: {lista[2]}")
else:
    print("La lista no tiene suficientes elementos ")

# Contar la cantidad de números impares en la lista
num_impares = sum(1 for num in lista if num % 2 != 0)
print(f"La cantidad de números impares en la lista es {num_impares}")

# Contar la cantidad de números en la lista que están entre dos números
count = 0
for i in range(len(lista)):
    for j in range(i+2, len(lista)):
        if lista[i > lista[j]]:
            count += 1
print(f"La cantidad de números en la lista que cumplen la condición de ser dos números mayores a él es: {count}")

