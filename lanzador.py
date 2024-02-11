import matplotlib.pyplot as plt

from Analisis_Datos.Db.getDataFromDb import GetDataFromDb
from Analisis_Datos.filterData import FilterData
from Analisis_Datos.linear_Regression import Linear_regression

from Web_Scrapping.scrapper import Scrapping



class Lanzador:

    def obtener_datos(self):
        analisis = GetDataFromDb('Api_Casas_Apuestas-main/bookmaker.db')
        analisis.complete_bd()
        for table in analisis.bd:
            df = analisis.get_data(table)
            analisis.csv_storage(df, f'Analisis_Datos/Db/csv/{table}.csv')

    def lanzar_apuestas(self, tabla):
        filter = FilterData('Analisis_Datos/Db/csv/{}.csv'.format(tabla)) #Instanciamos la clase FilterData
        filter.df.fillna(0, inplace=True) #Rellenamos los valores nulos con 0
        filter.df.drop('Unnamed: 0', inplace=True, axis=1) #Eliminamos la columna fecha, ya que no es numérica
        filter.get_boxplot(filter.df, tabla) #Obtenemos el diagrama de cajas
        filter.get_histplot(filter.df, tabla) #Obtenemos el histograma
        for column in filter.df.columns:
            filter.atipic_values(column)
            print(column, ': ', filter.atipic_values_percentaje()) #Obtenemos el porcentaje de valores atipicos
        filter.get_pairplot(filter.df, tabla) #Obtenemos el pairplot
        filter.df.drop('fecha', inplace=True, axis=1) #Eliminamos la columna fecha, ya que no es numérica
        print(filter.numeric_transform()) 
        filter.get_heatmap(filter.df, tabla) #Obtenemos el heatmap

        linear_regression = Linear_regression(filter.df)
        linear_regression.readyRegression('ganacia')
        print(linear_regression.get_model_slopes())
        linear_regression.plot_model_scopes()
        linear_regression.plot_regression_model(filter.df['monto'])  

        #Guardamos el dataset filtrado
        filter.df.to_csv('Analisis_Datos/Db/csv_filtrado/{}_filtradas.csv'.format(tabla), index=False)


    def lanzar_clientes(self):
        clientes = FilterData('Analisis_Datos/Db/csv/clientes.csv') #Instanciamos la clase FilterData
        #Eliminamos la columna de email, ya que los nombres no se corresponden con el email
        clientes.df.drop('email', inplace=True, axis=1)
        clientes.df.drop('Unnamed: 0', inplace=True, axis=1)

        clientes.df.to_csv('Analisis_Datos/Db/csv_filtrado/clientes_filtrados.csv', index=False) #Guardamos el dataset filtrado


    def lanzar_cuotas(self):
        cuotas = FilterData('Analisis_Datos/Db/csv/cuotas.csv') #Instanciamos la clase FilterData
        cuotas.df.drop('Unnamed: 0', inplace=True, axis=1)
        cuotas.df.drop_duplicates(subset=['partido_id'], inplace=True) #Eliminamos los registros duplicados
        cuotas.df.drop('partido_id', inplace=True, axis=1)

        cuotas.df.to_csv('Analisis_Datos/Db/csv_filtrado/cuotas_filtradas.csv', index=False) #Guardamos el dataset filtrado
    

    def lanzar_equipos(self):
        equipos = FilterData('Analisis_Datos/Db/csv/equipos.csv')
        equipos.df.drop('Unnamed: 0', inplace=True, axis=1)
        #Eliminamos la columna escudo ya que no proporciona informacion relevante
        equipos.df.drop('escudo', inplace=True, axis=1) 

        #Lo unico que tiene sentido en esta tabla hacer un grafico con la puntacion de cada equipo
        equipos.df[['nombre', 'puntaje']].plot(kind='bar', figsize=(10, 10)) #Diagrama de barras de los puntajes de cad equipo

        equipos.df.to_csv('Analisis_Datos/Db/csv_filtrado/equipos_filtrados.csv', index=False) #Guardamos el dataset filtrado
        plt.savefig('Analisis_Datos/Db/img/barplot/puntaje-equipos.png')


    def lanzar_partidos(self):
        partidos = FilterData('Analisis_Datos/Db/csv/partidos.csv')
        partidos.df.drop('Unnamed: 0', inplace=True, axis=1)
        partidos.df.drop('ganador', inplace=True, axis=1) #Eliminamos la columna ganador que esta vacia (los partidos estan en progreso)
        partidos.df.drop('fecha', inplace=True, axis=1) #Eliminamos la fecha que es siempre la misma salvo en el ultimo registro

        partidos.df.to_csv('Analisis_Datos/Db/csv_filtrado/partidos_filtrados.csv', index=False)

    

    
    def lanzar_scrapper_2023_2024(self):
        url = 'https://fbref.com/en/comps/8/Champions-League-Stats'
        year = '2023-2024'
        scrap = Scrapping(url, year)
        scrap.get_html(write=True)
        df = scrap.get_table()
        scrap.save_csv(df)

    def lanzar_scrapper_2022_2023(self):
        url = 'https://fbref.com/en/comps/8/2022-2023/2022-2023-Champions-League-Stats'