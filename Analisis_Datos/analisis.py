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
    
    #Metodo para completar el diccionario bd con las tablas y columnas de la base de datos
    def complete_bd(self):
        for table in self.get_tables():
            self.bd[table] = self.get_columns(table)
    
    #Metodo para obtener los datos de una tabla
    def get_data(self, table):
        conn = sqlite3.connect(self.bd_path)
        df = pd.read_sql_query("SELECT * FROM {}".format(table), conn)
        conn.close()
        return df
    



analisis = BdAnalisis('Api_Casas_Apuestas-main/bookmaker.db')
analisis.complete_bd()
for key, value in analisis.bd.items():
    print(key, value)