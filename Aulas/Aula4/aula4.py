import re
import json

file = open("../../data/dicionario_medico.xml", encoding="utf8")
texto = file.read()


#Limpar documento
texto = re.sub(r'<text.+?>',r'',texto)
texto = re.sub(r'</text>', r'', texto)

#texto = re.sub(r'</?text.*?>', r'', texto)

texto = re.sub(r'</?page.*?>', r'', texto)
texto = re.sub(r'</?pdf2xml.*?>', r'', texto)

#Extrair conceitos

#conceitos = re.findall(r'<?b>(.+)</b>\n([\s\S]+?)\n+<',texto)

conceitos = re.findall(r'<b>(.+)</b>\n([^<]+)',texto)

#conceitos = re.findall(r'<\b>(.+)<b>',texto)

novos_conceitos = []
for designacao, descricao in conceitos:
    nova_designacao = designacao.strip()
    nova_descricao = descricao.strip()
    novos_conceitos.append((nova_designacao,nova_descricao))


conceitos_dicti = dict(novos_conceitos)

#conceitos_dicti = { designacao.strip(): descricao.strip() for designacao, descricao in conceitos}

file_out = open("conceitos.json","w", encoding="utf8")
json.dump(conceitos_dicti,file_out, indent=4, ensure_ascii=False)
file_out.close()