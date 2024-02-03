import sqlite3
import pandas as pd

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('Api_Casas_Apuestas-main/bookmaker.db')

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecutar una consulta para obtener los nombres de las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Obtener los resultados de la consulta
tables = cursor.fetchall()
tables_list = []

# Obtenemos los nombres de las tablas
for table in tables:
    tables_list.append(table[0])


# Ejecutar una consulta SQL y cargar los resultados en un DataFrame de Pandas
df = pd.read_sql_query("SELECT * FROM bookmaker.db", conn)

# Cerrar la conexión a la base de datos
conn.close()

# Ahora puedes trabajar con el DataFrame 'df'
print(df.head())