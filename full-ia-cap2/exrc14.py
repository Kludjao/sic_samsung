import sympy as sp

# Definindo as variáveis
x, y = sp.symbols('x y')

# Definindo a função
f = sp.exp(x**2 + 2*y**3)

# Primeiras derivadas parciais
fx = sp.diff(f, x)
fy = sp.diff(f, y)

# Segundas derivadas parciais
fxx = sp.diff(fx, x)
fxy = sp.diff(fx, y)
fyx = sp.diff(fy, x)
fyy = sp.diff(fy, y)

# Exibindo os resultados
print("Primeiras derivadas parciais:")
print(f"f_x = {fx}")
print(f"f_y = {fy}")

print("\nSegundas derivadas parciais:")
print(f"f_xx = {fxx}")
print(f"f_xy = {fxy}")
print(f"f_yx = {fyx}")
print(f"f_yy = {fyy}")
