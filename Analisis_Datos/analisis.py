import sqlite3
import pandas as pd

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('Api_Casas_Apuestas-main/bookmaker.db')

# Ejecutar una consulta SQL y cargar los resultados en un DataFrame de Pandas
df = pd.read_sql_query("SELECT * FROM bookmaker.db", conn)

# Cerrar la conexión a la base de datos
conn.close()

# Ahora puedes trabajar con el DataFrame 'df'
print(df.head())
