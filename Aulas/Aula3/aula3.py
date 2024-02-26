import re 

filename = "../../data/dicionario_medico.txt"
file = open(filename)
texto = file.read()

#data cleaning
texto = re.sub(r"\f","",texto)

#marcar designações

texto = re.sub(r'\n\n(.+)',r'\n\n@\1',texto)
texto = re.sub(r'@(.+)\n\n@',r'@\1\n',texto)

#Extrair termos 
#designacoes = []
#designacoes = re.findall(r'@(.+)\n',texto)

termos = []
termos = re.findall(r'@(.+)\n([^@]+)',texto)


# Gerar HTML

titulo = "<h3> Dicionário Médico </h3>"
descricao = "<p> Este é um dicionário médico desenvolvido na disciplina de SPLNEB </p>"

body = "<body>"
for termo in termos:
    body += f"<h5> {termo[0]} </h5>"
    body += f"<p> {termo[1]} </p>"
    body += "<hr/>"


body += "</body>"

html = titulo + descricao + body
#print(html)

file_out = open("aula3.html", "w")
file_out.write(html)
file_out.close()