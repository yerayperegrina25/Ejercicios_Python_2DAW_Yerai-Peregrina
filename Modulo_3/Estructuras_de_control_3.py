frutas = ["Mango", "Cereza", "Mandarina", "Sandía", "Melocotón"]
print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])
print("Total de frutas:", len(frutas))
frutas.append("Uva")
print(*frutas, sep=", ")
