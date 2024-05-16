from bs4 import BeautifulSoup 
import requests
import json

def get_paper(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    paper_info = {}
    
    titulo_h1 = soup.find("h1", class_="page_title")
    resumo_section = soup.find("section",class_="item abstract")
    doi_section = soup.find("section",class_="item doi") 

    if titulo_h1:
        paper_info["titulo"] = titulo_h1.text.strip()
    if resumo_section:
        paper_info["resumo"] = resumo_section.p.text.strip()
    if doi_section:
        paper_info["doi"] = doi_section.span.a.text.strip()
    return paper_info


def get_Volume(url):
    
    response = requests.get(url)
    html = response.text
    papers = []
    soup = BeautifulSoup(html, "html.parser")
    titulos = soup.find_all("h3", class_="title")
    for titulo in titulos:
        url_paper = titulo.a["href"]
        paper_info = get_paper(url_paper)
        papers.append(paper_info)
    return papers


url = "https://www.actamedicaportuguesa.com/revista/index.php/amp/issue/view/462"
lista_papers = get_Volume(url)

f_out = open("papers.json","w")
json.dump(lista_papers,f_out, indent=4, ensure_ascii=False)
f_out.close()

