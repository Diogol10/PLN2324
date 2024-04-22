import json

with open("conceitos.json", encoding="utf-8") as file:
    conceitos = json.load(file)

with open("termos_traduzidos.txt", encoding="utf-8") as file_trad:
    traducoes = file_trad.read()

trad_dict = {}
for line in traducoes.split("\n"):  # Iterating over the lines of the file content
    if "@" in line:
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

with open("conceitos1.json", "w", encoding="utf-8") as file_out:
    json.dump(res, file_out, ensure_ascii=False, indent=4)



