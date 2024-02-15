import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dir_ = 'Web_Scrapping/scrapped_csv'
# Lista de nombres de archivos CSV que contienen datos históricos
csv_files = os.listdir(dir_)

# Cargar y combinar todos los datos históricos en un solo DataFrame
data = pd.concat([pd.read_csv(f'{dir_}/{file}') for file in csv_files])

# Preparación de datos, división en características (X) y la variable objetivo (y)
X = data.drop(columns=["Squad"])
y = data["Squad"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir los ganadores de la Champions League actual
ganadores_predichos = modelo.predict(X_test)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, ganadores_predichos)
r2 = r2_score(y_test, ganadores_predichos)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R^2): {r2}")
