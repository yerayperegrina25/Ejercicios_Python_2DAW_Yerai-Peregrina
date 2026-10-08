while True:
    pedir_usuario = input("Introduce el nombre de usuario: ")
    if pedir_usuario.isalpha() and 5 <= len(pedir_usuario) <= 10:
        print(f"usuario valido: {pedir_datos}")
        break
    else:
        print("error")

while True:
    contraseña = input("Introduce la contraseña: ")
    if contraseña.isalnum()len(contraseña) > 8:
        print("contraseña correcta")
        break
    else:
        print("error")
