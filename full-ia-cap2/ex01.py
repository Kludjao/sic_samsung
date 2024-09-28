import numpy as np

# 1. Vetor Zerado
vetor_zerado = np.zeros(5)
print("Vetor Zerado:", vetor_zerado)

# 2. Vetor com Uns
vetor_uns = np.ones(5)
print("Vetor com Uns:", vetor_uns)

# 3. Matriz Quadrada
matriz_quadrada = np.zeros((3, 3))
print("Matriz Quadrada:\n", matriz_quadrada)

# 4. Matriz Diagonal
matriz_diagonal = np.diag([1, 2, 3])
print("Matriz Diagonal:\n", matriz_diagonal)

# 5. Matriz Identidade
matriz_identidade = np.eye(3)
print("Matriz Identidade:\n", matriz_identidade)

# 6. Matriz Simétrica
matriz_simetrica = np.array([[1, 2, 3],
                              [2, 5, 6],
                              [3, 6, 9]])
print("Matriz Simétrica:\n", matriz_simetrica)
