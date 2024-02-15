import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression




dir_ = 'Web_Scrapping/scrapped_csv'
# Lista de nombres de archivos CSV que contienen datos históricos
csv_files = os.listdir(dir_)[:7]
print(csv_files)

# Cargar y combinar todos los datos históricos en un solo DataFrame
data = pd.concat([pd.read_csv(f'{dir_}/{file}') for file in csv_files])
#print(data)

# Preparación de datos, división en características (X) y la variable objetivo (y)
X = data.drop(columns=["Squad"])

# Convertir las columnas categóricas en columnas One-Hot Encoding
X_encoded = pd.get_dummies(X['Rk'])

# Eliminar la columna original 'Rk' del DataFrame original
X = X.drop(columns=['Rk'])

# Concatenar las columnas codificadas One-Hot Encoding con el DataFrame original
X = pd.concat([X, X_encoded], axis=1)
#print(X)

# Convertir la variable objetivo en columnas One-Hot Encoding
y = pd.get_dummies(data['Squad'])

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



# Obtener las etiquetas de clase para cada muestra en el conjunto de entrenamiento
y_train_labels = np.argmax(y_train.to_numpy(), axis=1)

# Inicializar y entrenar el modelo de regresión logística con las etiquetas de clase
modelo_logistico = LogisticRegression(max_iter=1000, solver='liblinear', C=0.1)
modelo_logistico.fit(X_train, y_train_labels)

# Predecir las probabilidades de los ganadores de la Champions League actual
probabilidades_predichas = modelo_logistico.predict_proba(X_test)

# Obtener las probabilidades predichas para cada equipo
probabilidades_por_equipo = pd.DataFrame(probabilidades_predichas, columns=modelo_logistico.classes_)

# Mostrar las probabilidades para los equipos
print(probabilidades_por_equipo)
