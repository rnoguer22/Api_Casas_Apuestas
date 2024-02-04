import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



class FilterData:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
    
    
    # Obtenemos los IDs de los registros con datos perdidos
    def get_nulls(self, eliminate=False): 
        nulls = self.df[self.df.isnull().any(axis=1)].index.tolist()
        if eliminate:
            self.df = self.df.dropna()
        return nulls
    

    #Obtenemos los estadisticos descriptivos de los datos
    def get_stats(self):
        return self.df.describe()
    

    #Obtenemos el diagrama de cajas de los datos
    def get_boxplot(self, df):
        sns.boxplot(data=df, orient='v')
        plt.show()


    #Histograma
    def get_histplot(self, df):
        for column in df.columns:
            sns.histplot(df[column], kde=True)
            plt.show()
    
    
    #Metodo para obtener los valores atipicos
    def atipic_values(self, column):
        if self.df[column].dtype != np.float64 and self.df[column].dtype != np.int64:
            return 'El tipo de dato no es numérico, no se pueden calcular los valores atípicos'
        
        # Filtrar los valores atípicos basado en el rango intercuartil
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)

        # IQR es el rango intercuartil 
        IQR = Q3 - Q1    

        # Limites permitidos para los datos
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR

        # Crear la máscara
        filtro_oulier = (self.df[column] < lim_inf) | (self.df[column] > lim_sup)

        # Filtramos el dataset aplicando la máscara
        self.df_pop_out = self.df[filtro_oulier] 

        return self.df_pop_out
    

    #Metodo para obtener el porcentaje de valores atipicos
    def atipic_values_percentaje(self):
        # Calculamos el porcentaje que componen estos valores respecto a la totalidad de los datos
        return self.df_pop_out.shape[0]/self.df.shape[0] * 100
    

    #Metodo para crear un dataframe sin valores atipicos
    def remove_atipic_values(self):
        self.df_non_atipic = self.df[~self.df.isin(self.df_pop_out)].dropna()
        return self.df_non_atipic

    
    #Metodo para obtener el diagrama de pares
    def get_pairplot(self, df):
        sns.pairplot(df, height=3, aspect=1.5)
        plt.show()


    #Transformamos los datos no numéricos
    def numeric_transform(self):
        for column in self.df.columns:
            if self.df[column].dtype != np.float64 and self.df[column].dtype != np.int64:
                self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
        return self.df
    
    
    #Metodo para obtener el diagrama de calor
    def get_heatmap(self, df):
        sns.heatmap(df.corr(), annot=True)
        plt.show()