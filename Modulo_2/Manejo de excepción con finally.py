try:
    archivo = open("archivo_no_existente.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    print("Bloque finally ejecutado.")
