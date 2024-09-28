import sympy as sp

# Definindo a variável simbólica
x, a, b, k = sp.symbols('x a b k')

# 1) Função: f(x) = x^3 - 1
f1 = x**3 - 1
f1_derivative = sp.diff(f1, x)

# 2) Função: f(x) = log(x^2 - 3k)
f2 = sp.log(x**2 - 3*k)
f2_derivative = sp.diff(f2, x)

# 3) Função: f(x) = exp(ax^b)
f3 = sp.exp(a * x**b)
f3_derivative = sp.diff(f3, x)

# Exibindo os resultados
print(f"1) Derivada de f(x) = x^3 - 1: {f1_derivative}")
print(f"2) Derivada de f(x) = log(x^2 - 3k): {f2_derivative}")
print(f"3) Derivada de f(x) = exp(ax^b): {f3_derivative}")
