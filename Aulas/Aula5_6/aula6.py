import json
import re

file = open("../Aula4/conceitos.json")
file_trad = open("../../data/termos_traduzidos.txt")

#traducoes = file_trad.read()
conceitos =  json.load(file)

#re.findall(r'(.+)\s@\s(.+)',"traducoes")

trad_dict = {}
for line in file_trad:
    pt, en = line.split("@")
    pt = pt.strip()
    en = en.strip()
    trad_dict[pt] = en

print(trad_dict)
res = {}
for conceito in conceitos:
    if conceito in trad_dict:
        tmp = {
            "desc": conceitos[conceito],
            "en": trad_dict[conceito]
        }
        res[conceito] = tmp
    else:
        tmp = {
            "desc": conceitos[conceito],
            "en": "sem tradução"
        }
        res[conceito] = tmp

file_out = open("conceitos.json","w")
json.dump(res, file_out, ensure_ascii=False, indent=4)


