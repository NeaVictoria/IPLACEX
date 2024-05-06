import funcionSumar as FS, funcionRestar as FR, funcionMultiplicar as FM, funcionDividir as FD
continuar = True
while(continuar):
    opcion = input("Ingrese 0 para salir, 1 para sumar, 2 para restar, 3 para multiplicar o 4 para dividir --> ")
    if(opcion=="0"):
        print("Gracias por usar la calculadora")
        continuar = False
    else:
        num1 = int(input("Ingrese un número --> "))
        num2 = int(input("Ingrese otro número --> "))
        if(opcion=="1"):
            resultado = FS.sumar(num1, num2)
            print("La suma de ambos números es:",resultado)
        elif(opcion=="2"):
            resultado = FR.restar(num1, num2)
            print("La resta de ambos números en el orden ingresado es:",resultado)
        elif (opcion == "3"):
            resultado = FM.multiplicar(num1, num2)
            print("La multiplicación de ambos números es",resultado)
        elif (opcion == "4"):
            resultado = FD.dividir(num1, num2)
            print("La división de ambos números en el orden ingresado es:",resultado)