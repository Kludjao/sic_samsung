import sympy as sp

# Definindo a variável
x = sp.symbols('x')

# Definindo as constantes
a, b, k = sp.symbols('a b k')

# Funções fornecidas
f1 = x**3 - 1
f2 = sp.log(x**2 - 3*k)
f3 = sp.exp(a*x**b)

# Calculando as derivadas
df1 = sp.diff(f1, x)
df2 = sp.diff(f2, x)
df3 = sp.diff(f3, x)

# Exibindo os resultados
print("Derivada de f(x) = x^3 - 1:")
print(f"f'(x) = {df1}")

print("\nDerivada de f(x) = log(x^2 - 3k):")
print(f"f'(x) = {df2}")

print("\nDerivada de f(x) = exp(ax^b):")
print(f"f'(x) = {df3}")
