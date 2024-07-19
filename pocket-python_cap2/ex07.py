notas = (('Davi', 88, 95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))
nome, ing, mat, cic = zip(*notas)


medmat = sum(mat) / len(mat)

print(medmat)
