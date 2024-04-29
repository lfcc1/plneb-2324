import requests
from bs4 import BeautifulSoup

url = "https://www.atlasdasaude.pt/doencasAaZ"
result = requests.get(url)
html = result.text

soup = BeautifulSoup(html,"html.parser")

lista_h3 = soup.find_all("h3", class_="field-content")

designacoes = []
for h3 in lista_h3:
    designacoes.append(h3.a.text)


lista_div = soup.find_all("div", class_="field-content")

descricoes = []
for div in lista_div:
    descricoes.append(div.get_text())


print(len(descricoes), len(designacoes))





