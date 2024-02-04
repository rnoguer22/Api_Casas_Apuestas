import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


class LinearRegression:

    def __init__(self, df):
        self.df = df


    #REGRESION LINEAL MULTIPLE
    #Metodo para obtener la regresión lineal
    def linearRegression(self, target):
        self.x_multiple = self.df.drop([target, 'fecha'], axis='columns')
        self.y_multiple = self.df[target]
        #Dividimos los datos en entrenamiento y test
        x_train, x_test, y_train, self.y_test = train_test_split(self.x_multiple,self.y_multiple, test_size=0.2, random_state=0)

        self.mod_lin_reg = LinearRegression() 
        self.mod_lin_reg.fit(x_train, y_train)
        self.mod_lr_predict = self.mod_lin_reg.predict(x_test)

        
    def get_model_slopes(self):
        return self.mod_lin_reg.coef_, self.mod_lin_reg.intercept_
    
    def plot_model_scopes(self):
        df_coef = pd.DataFrame(self.x_multiple.columns, columns=['variables'])
        df_coef['coeficientes'] = self.mod_lin_reg.coef_
        sns.barplot(x=df_coef['variables'], y=df_coef['coeficientes'])
        plt.show()
    
    def get_model_metrics(self):
        # Métricas para evaluar la calidad del modelo
        print('Mean Absolute Error:', mean_absolute_error(self.y_test, self.mod_lr_predict))
        print('Mean Absolute Percentage Error:', mean_absolute_percentage_error(self.y_test, self.mod_lr_predict)*100)
        print('Mean Squared Error:', mean_squared_error(self.y_test, self.mod_lr_predict))
        print('Root Mean Squared Error:', np.sqrt(mean_squared_error(self.y_test, self.mod_lr_predict)))
        print('R^2 coefficient of determination:', r2_score(self.y_test, self.mod_lr_predict))        


        