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
from statsmodels.api import add_constant
from statsmodels.regression.linear_model import OLS



class Linear_regression:

    def __init__(self, df):
        self.df = df


    #Preparamos la regresion lineal
    def readyRegression(self, target):
        self.target = target
        self.x_multiple = self.df.drop([target], axis='columns')
        self.y_multiple = self.df[target]

        #Dividimos los datos en entrenamiento y test
        x_train, x_test, y_train, self.y_test = train_test_split(self.x_multiple,self.y_multiple, test_size=0.2, random_state=0)
        self.mod_lin_reg = LinearRegression() 
        self.mod_lin_reg.fit(x_train, y_train)
        self.mod_lr_predict = self.mod_lin_reg.predict(x_test)


    #Obtenemos los coeficientes y la intersección        
    def get_model_slopes(self):
        return self.mod_lin_reg.coef_, self.mod_lin_reg.intercept_
    

    #Graficamos los coeficientes
    def plot_model_scopes(self):
        df_coef = pd.DataFrame(self.x_multiple.columns, columns=['variables'])
        df_coef['coeficientes'] = self.mod_lin_reg.coef_
        sns.barplot(x=df_coef['variables'], y=df_coef['coeficientes'])
        plt.show()
    

    #Métricas para evaluar la calidad del modelo
    def get_model_metrics(self):
        print('\nMean Absolute Error:', mean_absolute_error(self.y_test, self.mod_lr_predict))
        print('Mean Absolute Percentage Error:', mean_absolute_percentage_error(self.y_test, self.mod_lr_predict)*100)
        print('Mean Squared Error:', mean_squared_error(self.y_test, self.mod_lr_predict))
        print('Root Mean Squared Error:', np.sqrt(mean_squared_error(self.y_test, self.mod_lr_predict)))
        print('R^2 coefficient of determination:', r2_score(self.y_test, self.mod_lr_predict))    
    

    #Graficamos la regresión
    def plot_regression_model(self, x):
        x_const = add_constant(x) # add a constant to the model
        modelo = OLS(self.y_multiple, x_const).fit() # fit the model
        pred = modelo.predict(x_const) # make predictions
        print(modelo.summary())
        try:
            const = modelo.params[0] # create a variable with the value of the constant given by the summary
            coef = modelo.params[1] # create a variable with the value of the coef given by the summary
            x_l=np.linspace(x.min(), x.max(), 50) 
            y_l= coef*x_l + const # function of the line
            plt.figure(figsize=(10, 10))

            # plot the line
            plt.plot(x_l, y_l, label=f'{x.name} vs {self.y_multiple.name}={coef}*{x.name}+{const}', color='blue')

            # data
            plt.scatter(x, self.y_multiple, color='red', label=f'{x.name} vs {self.y_multiple.name}')

            plt.title('Regresion lineal')
            plt.xlabel(f'{x.name}')
            plt.ylabel(f'{self.y_multiple.name}')
            plt.legend()
            plt.show()
            return modelo
        except:
            print('No se puede imprimir la recta de regresión para modelos multivariable')
            plt.show()
            return modelo