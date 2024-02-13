import os

class AnalisisScrappedData:

    def __init__(self) -> None:
        self.rutas = os.listdir('Web_Scrapping/scrapped_csv')

analisis = AnalisisScrappedData()
print(analisis.rutas)