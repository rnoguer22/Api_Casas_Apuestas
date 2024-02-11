import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scrapping:

    def __init__(self, url) -> None:
        self.url = url


    #Metodo para obtener el HTML de la web
    def get_html(self, write:bool=False, path:str=None):
        # Realizar una solicitud GET para obtener el HTML de la página
        response = requests.get(self.url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la respuesta
            html_content = response.content
            # Crear un objeto BeautifulSoup para analizar el HTML
            self.soup = BeautifulSoup(html_content, 'html.parser')
            if write:
                # Convertir el objeto Tag a una cadena usando prettify()
                html_str = self.soup.prettify()
                # Imprimir el contenido del cuerpo de la página
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(html_str)
        else:
            print('Error al obtener el contenido de la página:', response.status_code)


overall_stats = soup.find('div', id='div_results2023-202480_overall')
print(overall_stats.prettify())

soup_overall = BeautifulSoup(str(overall_stats), 'html.parser')
col = soup_overall.find_all('th', scope='col')
columns = []
for th in col:
    content = th.get_text(strip=True)
    columns.append(content)
print(columns)

tbody = soup_overall.find_all('tbody')
soup_overall_rows = BeautifulSoup(str(tbody), 'html.parser')
rows = soup_overall_rows.find_all('tr')


data = []
col_i = []
counter = 0
for tr in rows:
    #Vamos a eliminar el texto de los span en este caso
    for span in tr.find_all('span'):
        span.decompose()
    
    for td in tr:
        content = td.get_text(strip=True)
        print(content)
        col_i.append(content)
        counter += 1
        if counter == len(columns):
            data.append(col_i)
            col_i = []
            counter = 0


print(data)
df = pd.DataFrame(data, columns=columns)
df.to_csv('Web_Scrapping/scrapped_csv/UEFA_2023-2024.csv', index=True, index_label='id', encoding='utf-8-sig')



# URL de la página a analizar
url = 'https://fbref.com/en/comps/8/Champions-League-Stats' 