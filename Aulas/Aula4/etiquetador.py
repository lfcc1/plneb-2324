import json
import re

file_conceitos = open("conceitos.json")
#file_livro = open("../../data/LIVRO-Doenças-do-Aparelho-Digestivo.txt")
file_livro = open("../../data/livrinho.txt")

texto = file_livro.read()
conceitos = json.load(file_conceitos)

def etiquetador(matched):
    designacao = matched[0]
    descricao = conceitos[designacao]

    etiqueta = f"<a href='' title='{descricao}'>{designacao}</a>"
    return etiqueta

for designacao, descricao in conceitos.items():
    expressao = r'\b'+ re.escape(designacao) + r'\b'
    texto = re.sub(expressao,etiquetador ,texto)

file_out = open("livro.html", "w")
print(texto, file=file_out)


