import numpy as np

# 1) Definindo os preços e quantidades como vetores
precos = np.array([1000000, 800000, 500000])  # Preços das ações A, B e C
quantidades = np.array([3, 4, 5])              # Quantidades de ações A, B e C

# 2) Calculando o valor total necessário para comprar as ações
valor_total = precos * quantidades
print("Valor total necessário para comprar as ações:", valor_total)

# Somando o valor total
valor_total_total = np.sum(valor_total)
print("Valor total total necessário:", valor_total_total)
