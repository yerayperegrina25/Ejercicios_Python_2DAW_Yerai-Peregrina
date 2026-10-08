nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
lugar_nacimiento = input("Introduce donde vives: ")

if edad < 20:
    print("¡Que joven!")
    
elif edad >= 21 and edad <=35:
    print("No eres tan joven...")
    
elif edad >35:
    print("¡Hay que empezar a cuidarse!")
