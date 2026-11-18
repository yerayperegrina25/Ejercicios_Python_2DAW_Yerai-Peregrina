def suma_numeros(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


print(suma_numeros(2, 4, 6, 7, 9, 10))
print(suma_numeros(2, 4, 6, 7, 9, 1))
print(suma_numeros(2, 4, 6, 7))
print(suma_numeros(2, 4, 6))
print(suma_numeros(2, 4))
