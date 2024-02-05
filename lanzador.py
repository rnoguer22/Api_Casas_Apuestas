from Analisis_Datos.filterData import FilterData
from Analisis_Datos.linearRegression import Linear_Regression
from Analisis_Datos.Db.getDataFromDb import GetDataFromDb

class Lanzador:

    def lanzar(self):
        filter = FilterData('Analisis_Datos/Db/csv/apuestas.csv')
        print(filter.get_nulls(True))
        print(filter.df) 
        print(filter.get_stats())
        ##filter.get_boxplot(filter.df)
        ##filter.get_histplot(filter.df)
        for column in filter.df.columns:
            filter.atipic_values(column)
            print(column, ': ', filter.atipic_values_percentaje())
        ##filter.get_pairplot(filter.df)
        #print(filter.remove_atipic_values()) no tiene sentido quitar valores atipicos con tan pocos datos
        filter.numeric_transform()
        filter.get_heatmap(filter.df)
        filter.df = filter.df.drop(['fecha'], axis='columns')
        print(filter.df)

        linear_regression = Linear_Regression(filter.df)
        linear_regression.readyRegression('ganacia')
        print('\n', linear_regression.get_model_slopes())
        linear_regression.plot_model_scopes()
        linear_regression.get_model_metrics()
        linear_regression.plot_regression_model()