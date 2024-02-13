import os
import pandas as pd


class AnalisisScrappedData:

    def __init__(self) -> None:
        self.ruta = 'Web_Scrapping/scrapped_csv'
        self.rutas = os.listdir(self.ruta)


    #En esta funcion vamos a analizar los datos de los csv
    def analize_csv(self):
        for csv in self.rutas:
            self.data_path = self.ruta + '/' + csv
            self.analize(self.data_path)

    #En esta funcion vamos a analizar los datos de un dataframe
    def analize(self, path):
        df = pd.read_csv(path)
        df.drop('Notes', inplace=True, axis=1)
        df.drop('Top Team Scorer', inplace=True, axis=1)
        df.drop('Goalkeeper', inplace=True, axis=1)
        df.dropna(inplace=True)
        df.to_csv(path, index=False)




analisis = AnalisisScrappedData()
print(analisis.rutas)
analisis.analize_csv()