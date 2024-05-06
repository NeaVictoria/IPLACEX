# Escriba un programa que solicite al usuario ingresar el nombre y la edad de dos personas y luego imprima un mensaje indicando el nombre del mayor y cuántos años de diferencia tienen.

#Datos
nombre1 = input("Ingresa el nombre de la primera persona")
edad1 = int(input("Ingresa la edad de la primera persona"))
print("===========")
nombre2 = input("Ingresa el nombre de la segunda persona")
edad2 = int(input("Ingresa la edad de la segunda persona"))

if edad1 > edad2:
    diferencia = edad1 - edad2
    mayor = nombre1
    menor = nombre2
elif edad1 < edad2:
    diferencia = edad2 - edad1
    mayor = nombre2
    menor = nombre1
else:
    print(f"{nombre1} y {nombre2} tienen la misma edad.")

print(f"{mayor} es {diferencia} años mayor que {menor}.")
