try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    
    resultado = numero1 / numero2
    print("Correcto. El resultado es:", resultado)

except ZeroDivisionError:
    print("ERROR: No se puede dividir entre cero.")
except ValueError:
    print("ERROR: Por favor, introduce solo números válidos.")
