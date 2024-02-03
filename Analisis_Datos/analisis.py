import sqlite3
import pandas as pd

class BdAnalisis:

    def __init__(self, bd_path):
        self.bd_path = bd_path
        self.bd = {}

    #Metodo para obtener las tablas de la base de datos
    def get_tables(self):
        conn = sqlite3.connect(self.bd_path)
        cursor = conn.cursor() #Cursor para ejecutar consultas SQL
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tables_list = []
        for table in tables:
            tables_list.append(table[0]) #Obtenemos los nombres de las tablas
        conn.close() #Cerramos la conexión con la base de datos
        return tables_list
    
    #Metodo para obtener las columnas de una tabla
    def get_columns(self, table):
        conn = sqlite3.connect(self.bd_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info({})".format(table))
        columns = cursor.fetchall()
        columns_list = []
        for column in columns:
            columns_list.append(column[1]) #Obtenemos los nombres de las columnas
        conn.close()
        return columns_list
    
    



'''
# Ejecutar una consulta SQL y cargar los resultados en un DataFrame de Pandas
df = pd.read_sql_query("SELECT * FROM bookmaker.db", conn)

# Cerrar la conexión a la base de datos
conn.close()

# Ahora puedes trabajar con el DataFrame 'df'
print(df.head())
'''


analisis = BdAnalisis('Api_Casas_Apuestas-main/bookmaker.db')
print(analisis.get_tables())