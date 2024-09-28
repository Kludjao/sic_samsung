import numpy as np

# Saída da rede neural
output = np.array([0.4, 2.0, 0.001, 0.32])

# Função softmax
def softmax(x):
    e_x = np.exp(x - np.max(x))  # Subtrai o máximo para estabilidade numérica
    return e_x / e_x.sum(axis=0)

# Aplicando a função softmax
softmax_output = softmax(output)
print(softmax_output)
