import requests
from bs4 import BeautifulSoup
import json
import string


def extrai_doencas(url):
    result = requests.get(url)
    html = result.text

    soup = BeautifulSoup(html,"html.parser")
    pais = soup.find_all("div", class_="views-row")
    dicionario_doencas = {}
    for pai in pais:
        div_designacao = pai.find("div", class_="views-field-title")
        designacao = div_designacao.h3.a.text
        div_descricao = pai.find("div", class_="views-field-body")
        descricao = div_descricao.div.get_text()
        dicionario_doencas[designacao] = descricao
    
    return dicionario_doencas


url_base = "https://www.atlasdasaude.pt/doencasaaz"

urls = [ url_base + "/" + c for c in list(string.ascii_lowercase)]

res = {}
for url in urls:
    dicti = extrai_doencas(url)
    res = res | dicti


f_out = open("doencas_az.json","w")
json.dump(res, f_out, indent= 4, ensure_ascii= False)
f_out.close()