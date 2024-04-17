from deep_translator import GoogleTranslator
import json

file = open("../Aula4/conceitos.json")
conceitos = json.load(file)

novo_dici = {}

i = 0
for designcao_pt in conceitos:
    print(i)
    designacao_en = GoogleTranslator(source='pt', target='en').translate(designcao_pt)
    novo_dici[designcao_pt] = {
                                "desc": conceitos[designcao_pt],
                                "en": designacao_en
                               }
    print(designcao_pt,designacao_en)
    i = i + 1

    
file_out = open("conceitos_v2.json","w")
json.dump(novo_dici,file_out, indent=4, ensure_ascii=False)