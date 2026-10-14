videojuegos = ["fortnite", "gears of war", "gta6"]

buscar_juego = input("Busca el juego por su nombre: ").lower()

if buscar_juego in videojuegos:
    print("El juego está en la lista.")
else:
    print("El juego no está en la lista.")
