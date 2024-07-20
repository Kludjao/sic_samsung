# Escreva um programa que recebe dois pontos no plano cartesiano, (x1, y1) e (x2, y2) e imprime a distância entre esses 2 pontos.
import math

ponto1 = input("Insira um ponto do plano cartesiano: ")

ponto2 = input("Insira um ponto do plano cartesiano: ")

a, b = map(float, ponto1.split())

c, d = map(float, ponto2.split())

distancia = math.sqrt((c - a) ** 2 + (d - b) ** 2)
print(f"A distância entre os pontos ({a}, {b}) e ({c}, {d}) é {distancia:.2f}")