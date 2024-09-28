import numpy as np
from sklearn.linear_model import LinearRegression

import pandas as pd

data_url = "http://lib.stat.cmu.edu/datasets/boston"
boston = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
X = np.hstack([boston.values[::2, :], boston.values[1::2, :2]])
y = boston.values[1::2, 2]


A = X[:4, [0, 4, 5, 6]] 
b = y[:4]


model = LinearRegression()
model.fit(A, b)


weights = model.coef_


intercept = model.intercept_

print("Vetor de pesos:", weights)
print("Intercepto:", intercept)
