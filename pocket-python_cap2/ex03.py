lista = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print(lista)

maior = lista[0]

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        indice_maior = i

lista[indice_maior], lista[-1] = lista[-1], lista[indice_maior]

print(lista)

