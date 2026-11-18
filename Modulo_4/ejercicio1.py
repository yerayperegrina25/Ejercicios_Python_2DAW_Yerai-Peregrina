l_nums = [1, 2, 3, 4, 5]

num_quitado = l_nums.pop(1)

l_nums.append(num_quitado)

print("Lista:", l_nums)
print("Elemento eliminado:", num_quitado)

print("Posiciones 3 a 5:", l_nums[2:5])

l_nums.insert(-1, 10)
print("Lista con el 10:", l_nums)

l_nums.clear()
print("Lista vacía:", l_nums)

del l_nums
