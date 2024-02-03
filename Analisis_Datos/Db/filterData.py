import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



class filterData:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
    
    
    # Obtenemos los IDs de los registros con datos perdidos
    def get_nulls(self): 
        return self.df[self.df.isnull().any(axis=1)].index.tolist()



filter = filterData('Analisis_Datos/Db/csv/apuestas.csv')
print(filter.get_nulls()) 