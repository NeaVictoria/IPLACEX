# Solicitar ingreso por parte del usuario del valor del euro y del dolar.
precio_euro = float(input("Ingrese el precio del euro en pesos chileno: "))
precio_dolar = float(input("Ingrese el precio del dolar en pesos chilenos: "))

# Solicitar ingresa del monto en pesos chilenos
monto_pesos = float(input("Ingrese el monto en pesos chilenos que desea convertir: "))

# Calculo de equivalencia en euros y en dolares
equivalencia_dolar = monto_pesos / precio_dolar
equivalencia_euro = monto_pesos / precio_euro

# Imprimir la equivalencia entra las dos divisas
print(f"{monto_pesos} pesos chilenos son {equivalencia_dolar:.2f} dólares")
print(f"{monto_pesos} pesos chilenos son {equivalencia_euro:.2f} euros")

# Determinar la mehjor opción de compra

if equivalencia_dolar > equivalencia_euro:
    print("Le conviene más comprar dólares ya que obtendrá", int(equivalencia_dolar), "y esos es más que", int(equivalencia_euro))
elif equivalencia_dolar < equivalencia_euro:
    print("Le conviene comprar euros ya que obtendrá", int(equivalencia_euro), "y eso es más que", int(equivalencia_dolar))
else:
    print("Da igual la moneda a comprar, obtendrá el mismo valor en ambas.")