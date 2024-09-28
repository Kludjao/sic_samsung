from scipy.stats import binom

# Número de filhos (n) e a probabilidade de ser menino (p)
n = 3
p = 0.5

# Probabilidade de ter exatamente 2 meninos (k = 2)
k = 2
probabilidade = binom.pmf(k, n, p)

# Valor esperado (média) e variância da distribuição binomial
media = binom.mean(n, p)
variancia = binom.var(n, p)

# Exibindo os resultados
print(f"Probabilidade de ter exatamente 2 meninos: {probabilidade:.4f}")
print(f"Valor esperado (média) do número de meninos: {media:.4f}")
print(f"Variância do número de meninos: {variancia:.4f}")
