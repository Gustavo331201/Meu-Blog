import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    valores_x = np.loadtxt('X.txt')
    valores_y = np.loadtxt('y.txt')
except:
    valores_x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
    valores_y = np.array([1200, 1400, 1700, 2100, 2500, 2900, 3400, 3800, 4200, 5000])

X_matriz = np.column_stack((np.ones(len(valores_x)), valores_x))
Xt = X_matriz.T

XtX_inv = np.linalg.inv(np.dot(Xt, X_matriz))
beta = np.dot(XtX_inv, np.dot(Xt, valores_y))
a, b = beta[0], beta[1]

plt.figure(figsize=(8, 5))

plt.scatter(valores_x, valores_y, color='yellow', s=50, label='Dados Reais')

plt.plot(valores_x, a + b * valores_x, color='red', linewidth=2, label='Regressão Linear')

plt.title(f"Regressão Linear (Intercepto={a:.2f}, Inclinação={b:.2f})")
plt.xlabel("Anos de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
