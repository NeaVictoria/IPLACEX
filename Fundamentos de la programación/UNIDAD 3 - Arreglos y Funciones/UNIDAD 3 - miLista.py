miLista = [3,12,5,1,7,8,2,9,0,4,2,13,23,6]
print(miLista)
miLista.append(55) #Agrega el 55
print(miLista)
suma = sum(miLista) #Suma todos los elementos (debería ser 150)
print(suma)
largo = len(miLista) #Guarda la cantidad de elementos en la lista (en este caso 15)
print(largo)
miLista.pop() #Elimina el último elemento (en este caso el 55)
print(miLista)
miLista.pop(1) #Elimina el contenido del índice 1. En este caso el 12
print(miLista)
miLista.remove(2) #Elimina el primero número 2 en la lista (en este caso el que está entre el 8 y el 9)
print(miLista)
minimo = min(miLista)
print(minimo)
maximo = max(miLista)
print(maximo)