videojuegos = ["fifa", "minecraft", "gta", "zelda", "fortnite"]

buscar = input("Introduce el videojuego que quieres buscar: ")

if buscar.lower() in videojuegos:
    print("El videojuego sí está en la lista.")
else:
    print("El videojuego no está en la lista.")
