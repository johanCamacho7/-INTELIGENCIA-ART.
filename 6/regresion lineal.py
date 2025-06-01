import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
X = np.linspace(1, 40, 40).reshape(-1, 1)
y = 2.5 * X.flatten() + np.random.normal(0, 8, 40)
y[[5, 12, 20, 30, 35]] -= [15, 10, 20, 12, 8]

modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

plt.scatter(X, y, color='blue', label="Datos reales")
plt.plot(X, y_pred, color='red', linestyle="--", label="Regresión lineal")
plt.xlabel("Inversión ")
plt.ylabel("ganancia)")
plt.title("inversion en el juego contra unidades vendidas")
plt.legend()
plt.grid()
plt.show()

print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")

nueva_inversion = np.array([[25]])  # Inversión
prediccion = modelo.predict(nueva_inversion)
print("ejemplo:")
print(f"gastamos esto en el juego  {nueva_inversion[0][0]} mil dólares, y esperabamos un retorno de  {prediccion[0]:.2f}  de unidades vendidas.")
