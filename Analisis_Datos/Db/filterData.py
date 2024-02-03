import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



class filterData:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
    
    
    # Obtenemos los IDs de los registros con datos perdidos
    def get_nulls(self, eliminate=False): 
        nulls = self.df[self.df.isnull().any(axis=1)].index.tolist()
        if eliminate:
            self.df = self.df.dropna()
    

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
        lim_sup = Q3 + 1.5 *IQR

        # Crear la máscara
        filtro_oulier = (self.df[column] < lim_inf) | (self.df[column] > lim_sup)

        # Filtramos el dataset aplicando la máscara
        self.df_pop_out = self.df[filtro_oulier] 

        return self.df_pop_out
    

    #Metodo para obtener el porcentaje de valores atipicos
    def atipic_values_percentaje(self):
        # Calculamos el porcentaje que componen estos valores respecto a la totalidad de los datos
        return self.df_pop_out.shape[0]/self.df.shape[0] * 100




filter = filterData('Analisis_Datos/Db/csv/apuestas.csv')
print(filter.get_nulls(True))
print(filter.df) 
print(filter.get_stats())
filter.get_boxplot(filter.df)
#filter.get_histplot(filter.df)
for column in filter.df.columns:
    filter.atipic_values(column)
    print(column, ': ', filter.atipic_values_percentaje())
filter.get_boxplot(filter.df_pop_out)
