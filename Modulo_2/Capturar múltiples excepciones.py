try:
    operacion = 10 / 0
    archivo = open("archivo_no_existente.txt", "r")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except FileNotFoundError:
    print("Error: El archivo no existe.")