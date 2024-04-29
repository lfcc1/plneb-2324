import requests
from bs4 import BeautifulSoup
import json
import string


url = "https://www.atlasdasaude.pt/doencasaaz"
result = requests.get(url)
html = result.text

soup = BeautifulSoup(html,"html.parser")
pais = soup.find_all("div", class_="views-row")
dicionario_doencas = {}
for pai in pais:
    print(pai.findChildren(recursive = False))
    print("----------")





