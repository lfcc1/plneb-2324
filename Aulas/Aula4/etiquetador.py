import json
import re

file_conceitos = open("conceitos.json")
#file_livro = open("../../data/LIVRO-Doenças-do-Aparelho-Digestivo.txt")
file_livro = open("../../data/livrinho.txt")

texto = file_livro.read()
conceitos = json.load(file_conceitos)

blacklist = ["e", "de", "para", "pelo", "os", "são", "este"]

conceitos_min = { chave.lower(): conceitos[chave] for chave in conceitos}

def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        descricao = conceitos_min[palavra]
        etiqueta = f"<a href='' title='{descricao}'>{original}</a>"
        return etiqueta
    else:
        return original


expressao = r'[\wáéçãóõéíêâú]+'
texto = re.sub(expressao,etiquetador ,texto, flags=re.IGNORECASE)
texto = re.sub(r'\n',r'<br>', texto)
texto = re.sub(r'\f', r'<hr>', texto)

file_out = open("livro.html", "w")
print(texto, file=file_out)


