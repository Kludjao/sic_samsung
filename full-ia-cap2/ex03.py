from sklearn.datasets import load_digits
import numpy as np

X = load_digits().data

imagem_1 = X[0]  
imagem_10 = X[9]  


semelhança_1_10 = np.dot(imagem_1, imagem_10)
print("Semelhança entre a primeira e a décima imagem:", semelhança_1_10)

semelhanca_matriz = np.dot(X, X.T)

print("Matriz de semelhança (dot product):\n", semelhanca_matriz)
