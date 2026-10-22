numeros = input("Introduce números separados por comas: ")
lista = [int(n) for n in numeros.split(",")]
lista.sort()
print(lista)
