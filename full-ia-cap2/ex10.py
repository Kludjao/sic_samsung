import numpy as np

def logistic_inverse(y):
    if y <= 0 or y >= 1:
        raise ValueError("y deve estar entre 0 e 1 (exclusivo).")
    return -np.log((1 - y) / y)

# Exemplo de uso
y_values = [0.1, 0.5, 0.9]
inverse_results = [logistic_inverse(y) for y in y_values]

# Exibindo os resultados
for y, inv in zip(y_values, inverse_results):
    print(f"σ⁻¹({y}) = {inv:.4f}")
