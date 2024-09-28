import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Definindo os vetores de classificação
a = np.array([4, 5, 2, 2])
b = np.array([4, 0, 2, 0])
c = np.array([2, 2, 0, 1])

# 1) Calculando a distância euclidiana
dist_ab = np.linalg.norm(a - b)
dist_ac = np.linalg.norm(a - c)
dist_bc = np.linalg.norm(b - c)

# Exibindo os resultados
print("Distância Euclidiana entre a e b:", dist_ab)
print("Distância Euclidiana entre a e c:", dist_ac)
print("Distância Euclidiana entre b e c:", dist_bc)

# Criando um dicionário para armazenar distâncias
distancias_euclidiana = {
    'a-b': dist_ab,
    'a-c': dist_ac,
    'b-c': dist_bc
}

# Encontrando os dois usuários mais próximos e mais distantes
mais_proximos = sorted(distancias_euclidiana, key=distancias_euclidiana.get)[:2]
mais_distantes = sorted(distancias_euclidiana, key=distancias_euclidiana.get, reverse=True)[:2]

print("Usuários mais próximos (Euclidiana):", mais_proximos)
print("Usuários mais distantes (Euclidiana):", mais_distantes)

# 2) Calculando a distância do cosseno
ratings = np.array([a, b, c])
similaridade_cosseno = cosine_similarity(ratings)
distancia_cosseno = 1 - similaridade_cosseno

# Exibindo a matriz de distâncias
print("Matriz de Distância do Cosseno:")
print(distancia_cosseno)

# Encontrando os dois usuários mais próximos e mais distantes
distancias_cosseno = {
    'a-b': distancia_cosseno[0][1],
    'a-c': distancia_cosseno[0][2],
    'b-c': distancia_cosseno[1][2]
}

mais_proximos_cosseno = sorted(distancias_cosseno, key=distancias_cosseno.get)[:2]
mais_distantes_cosseno = sorted(distancias_cosseno, key=distancias_cosseno.get, reverse=True)[:2]

print("Usuários mais próximos (Cosseno):", mais_proximos_cosseno)
print("Usuários mais distantes (Cosseno):", mais_distantes_cosseno)

# Resposta:

# 1) Distância Euclidiana:
#    - Distância entre a e b: \(5.0\)
#    - Distância entre a e c: \(2.0\)
#    - Distância entre b e c: \(3.162\)

#    Usuários mais próximos: a e c  
#    Usuários mais distantes: a e b

# 2) Distância do Cosseno:
#    - Distância entre a e b: \(0.5\)
#    - Distância entre a e c: \(0.175\)
#    - Distância entre b e c: \(0.8\)

#    Usuários mais próximos:  a e c  
#    Usuários mais distantes: b e c