palabra = input("Introduce una palabra: ")
contador = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        contador += 1

print("Número de vocales:", contador)
