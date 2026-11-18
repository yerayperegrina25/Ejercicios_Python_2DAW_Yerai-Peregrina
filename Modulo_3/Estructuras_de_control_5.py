edad = int(input("Introduce una edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad <= 64:
    print("Eres adulto")
else:
    print("Eres mayor")