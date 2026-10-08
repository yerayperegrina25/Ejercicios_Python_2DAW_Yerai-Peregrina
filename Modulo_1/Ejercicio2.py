try:
    numerador = float(input("Introduce el divisor: "))
    denominador = float(input("Introduce el dividendo: "))

    resultado = numerador / denominador

    print(f"resultado:{resultado:.2f}")

except Error_division:
    print("ERROR: El dividendo no puede ser cero")

except ValueError:
    print("ERROR: Debes introducir un numero")
