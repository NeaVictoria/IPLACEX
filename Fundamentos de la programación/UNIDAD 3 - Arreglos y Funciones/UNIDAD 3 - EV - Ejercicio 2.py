def ingresar_notas(N):
    """
    Función que recibe el número N como parámetro y retorna un arreglo.
    """
    notas = []
    for i in range(N):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(lista):
    """
    Función que recibe como parámetro una lista que siempre tendrá elementos números y retorna el promedio de los elementos de la lista.
    """
    promedio = sum(lista) / len(lista)
    return promedio

def contar_elementos_por_debajo_del_promedio(lista):
    """
    Función que recibe como parámetro una lista que siempre tendrá elementos numéricos y retorna la cantidad de elementos que están por debajo del promedio de la lista.
    """
    promedio = calcular_promedio(lista)
    elementos_por_debajo_del_promedio = sum(1 for elemento in lista if elemento < promedio)
    return elementos_por_debajo_del_promedio

def main():
    N = int(input("Ingrese la cantidad de notas que desea ingresar: "))
    notas = ingresar_notas(N)
    promedio = calcular_promedio(notas)
    cantidad_por_debajo_del_promedio = contar_elementos_por_debajo_del_promedio(notas)

    print(f"El promedio de las notas es: {promedio}")
    print(f"La cantidad de notas por debajo del promedio es: {cantidad_por_debajo_del_promedio}")

if __name__ == "__main__":
    main()
