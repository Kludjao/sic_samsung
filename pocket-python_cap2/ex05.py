maria = {'coreano': 94, 'ingles': 91, 'matematica': 89, 'ciencia': 83}
soma = 0
for values in maria.values():
    soma += values

media = soma / len(maria)

print(media)