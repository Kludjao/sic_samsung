lista = [[1, 2], [3, 4], [5, 6]]

lista2 = []

for dup in lista:
    for num in dup:
        lista2.append(num)

print(lista2)