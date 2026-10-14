texto_numeros = input("Introduce videojuegos separados por comas: ")

lista_texto = texto_numeros.split(",")

lista_numeros = []
for numero in lista_texto:
    lista_numeros.append(int(numero))

lista_numeros.sort()
print("numeros ordenador: ", lista_numeros)

