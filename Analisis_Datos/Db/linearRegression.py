import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns



class LinearRegression:

    def __init__(self, df):
        self.df = df


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

        