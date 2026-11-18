lista = [1, 2, 3, 4, 5]

introducir_numero = (int(input("Introduce un número de la lista: ")))

lista = list(range(1, 6))

if introducir_numero in lista:
    print("El número  fué eliminado")
else:
    print("El número fué eliminado de la lista")

print("lista:", lista)
