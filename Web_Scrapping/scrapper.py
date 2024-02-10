import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.sofascore.com/tournament/football/europe/uefa-champions-league/7')
soup = BeautifulSoup(r.text, 'xml')
print(soup)