try:
    numero = float(input("Introduce un número: "))
    print("Has introducido el número:", numero)
except ValueError:
    print("Error: Eso no es un número válido.")
