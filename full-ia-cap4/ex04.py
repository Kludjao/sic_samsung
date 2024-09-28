import numpy as np
from scipy import stats

media_notas = 80
variancia_notas = 9
n = 30  # tamanho da amostra
desvio_padrao = np.sqrt(variancia_notas)

confiança = 0.95
alpha = 1 - confiança

t_critico = stats.t.ppf(1 - alpha/2, df=n-1)

margem_erro = t_critico * (desvio_padrao / np.sqrt(n))

limite_inferior = media_notas - margem_erro
limite_superior = media_notas + margem_erro

# Output
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")
