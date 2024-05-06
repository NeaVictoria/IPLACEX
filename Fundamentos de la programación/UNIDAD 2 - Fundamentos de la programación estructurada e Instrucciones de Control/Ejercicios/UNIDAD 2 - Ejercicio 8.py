# Solicitar al usuario que ingresa una nota
nota = float(input("Ingrese la nota: "))

if 1.0 <= nota <= 7.0:
    print("Es válida")

    # Determinar si la nota es azul o roja
    if nota >= 4.0:
        print("Es un azul")
    else:
        print("Es un rojo")
else:
    print("No es una nota válida")