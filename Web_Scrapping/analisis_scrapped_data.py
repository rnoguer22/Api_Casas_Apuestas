import os
import pandas as pd


class AnalisisScrappedData:

    def __init__(self) -> None:
        self.ruta = 'Web_Scrapping/scrapped_csv'
        self.rutas = os.listdir(self.ruta)


    def analize_csv(self):
        for csv in self.rutas:
            data_path = self.ruta + '/' + csv
            self.analize(data_path)
    




analisis = AnalisisScrappedData()
print(analisis.rutas)
analisis.analize_csv()