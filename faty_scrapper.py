import requests
from bs4 import BeautifulSoup

URL = 'http://www.puertos.es/es-es/oceanografia/Paginas/portus.aspx'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
