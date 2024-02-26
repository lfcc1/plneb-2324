import re 

filename = "../../data/dicionario_medico.txt"
file = open(filename)
texto = file.read()

#data cleaning
texto = re.sub(r"\f","",texto)

#marcar designações

texto = re.sub(r'\n\n(.+)',r'\n\n@\1',texto)
texto = re.sub(r'@(.+)\n\n@',r'@\1\n',texto)

#extrair termos 


conceitos = re.split(r"\n{2,}",texto)

termos = [ tuple(conceito.split("\n", maxsplit=1)) for conceito in conceitos]

print(termos)