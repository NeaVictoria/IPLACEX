miLista = [3,12,5,1,7,8,2,9,0,4,2,13,23,6]
num = int(input("Ingrese un número -->"))

if(num in miLista):
    i = 0
    while(num!=miLista[i]):
        i = i + 1
    print("El elemento",num,"está en el indice",i)
else:
    print("Número no existe en la lista")