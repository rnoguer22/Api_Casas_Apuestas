import os
import pandas as pd


class AnalisisScrappedData:

    def __init__(self) -> None:
        self.ruta = 'Web_Scrapping/scrapped_csv'
        self.rutas = os.listdir(self.ruta)


    #En esta funcion vamos a analizar los datos de los csv
    def analize_csv(self):
        print('Analizando los siguientes datos:')
        for csv in self.rutas:
            print(csv)
            self.data_path = self.ruta + '/' + csv
            self.analize(self.data_path)


    #En esta funcion vamos a analizar los datos de un dataframe
    def analize(self, path):
        df = pd.read_csv(path)
        '''
        df.drop('Notes', inplace=True, axis=1)
        df.drop('Top Team Scorer', inplace=True, axis=1)
        df.drop('Goalkeeper', inplace=True, axis=1)
        df.dropna(inplace=True)
        df['id'] = df.index
        '''
        try: 
            df['Attendance'] = df['Attendance'].str.replace(',', '').astype(float) / 1000
        except:
            pass

        try:
            df.drop('Last 5', inplace=True, axis=1)
        except:
            pass
        #Obtenemos la temporada de cada champions y lo añadimos al nombre del equipo, para diferenciar entre temporadas
        year = path.split('/')[2].split('_')[1].split('.')[0]
        if not df['Squad'].str.contains(year).any():
            df['Squad'] = df['Squad'] + ' ' + year

        df.to_csv(path, index=False)

    
    #Funcion para obtener el dataframe final
    def get_final_data(self):
        dfs = []
        contador = 0
        for csv in self.rutas:
            data_path = self.ruta + '/' + csv
            df = pd.read_csv(data_path)
            df['id'] = range(contador, contador + len(df))
            dfs.append(df)
            contador += len(df)
        final_df = pd.concat(dfs)
        final_df.to_csv('UEFA_Final_Data.csv', index=False)
        return final_df