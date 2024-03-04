#Analisar DOC
#Extrair Termos (posso fazer data cleaning e pattern matching(por marcas onde quero))
#Guardar Termos
#Gerar HTML

import re
filename = "C:\\Users\\Asus Rog Strix\\Desktop\\Informática Médica\\1ºAno\\2º Semestre\\Processamento de Linguagem Natural\\dicionario_medico.txt"
with open(filename, 'r', encoding= 'utf-8') as f:
    texto=f.read()

#data cleaning
texto = re.sub(r'\f','',texto)  #substituir o texto em que removemos o ff(quebra de pagina) por nada

#designacao= re.compile(r'\n\n(.+?)\n')  # O padrão (.+?) corresponde a qualquer texto entre duas quebras de linha
# Encontra todas as designações
#correspondenciasdesignacao = re.findall(designacao, texto)
#print(correspondenciasdesignacao)

#descricao = re.compile(r'\n(.+?)\n\n')  # O padrão (.+?) corresponde a qualquer texto entre uma quebra de linha e duas quebras de linha consecutivas

# Encontra todas as descrições
#correspondenciasdescricao = re.findall(descricao, texto)
#print(correspondenciasdescricao)



#marcar designações
texto = re.sub(r'\n\n(.+)',r'\n\n@\1',texto)  #mesmo assim ha locais com dois @ seguidos
texto = re.sub(r'@(.+)\n\n@',r'@\1\n',texto)  #apenas poe um arroba

#extrair termos
termos=[]
termos = re.findall(r'@(.+)\n',texto)

#extrair descrições
descricoes=[]
descricoes= re.findall(r'@.+\n([^@]+)',texto)  #encontra as descricoes ate chegar a um @, apanha todos os caracteres menos @

#para excluir os \n finais que estao a ficar podemos fazer
conceitos= re.split(r"\n\n{2,}",texto)  #antes de 2 ou mais \n, 

termo = [conceito.split("\n",maxsplit=1) for conceito in conceitos]



#Gerar HTML

'''titulo = "<h3 style='font-family: Arial, sans-serif; text-align: center;'> Dicionário Médico </h3>"
descricao = "<p style='font-family: Arial, sans-serif; font-size: 18px; text-align: center;'> Este é um dicionário médico desenvolvido na disciplina de SPLEB<br/><br/> </p>"
body= "<body style='text-align: left; background-color: #e6f7ff;'>"

# Supondo que 'termos' e 'descricoes' são listas de termos e descrições correspondentes
for i in range(len(termos)):
    body += f"<p style='font-size: 18px;'> {termos[i]} - {descricoes[i]} </p>"
    body += "<hr/>"  # Adiciona uma barra horizontal após cada termo
    body += "<br/>"  # Adiciona uma quebra de linha entre cada termo

body += "</body>"

html = titulo + descricao + body'''

titulo = "<h3 style='font-family: Arial, sans-serif; text-align: center;'> Dicionário Médico </h3>"
descricao = "<p style='font-family: Arial, sans-serif; font-size: 18px; text-align: center;'> Este é um dicionário médico desenvolvido na disciplina de SPLEB<br/><br/> </p>"
body= "<body style='text-align: left; background-color: white;'>"
body += "<div style='background-color: white; padding: 20px;'>"

for i in range(len(termos)):
    body += "<div style='border: 1px solid #ccc; padding: 10px; margin: 10px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #e6f7ff;'>"
    body += f"<p style='font-size: 18px;'><strong>{termos[i]}</strong></p>"
    body += f"<p>{descricoes[i]}</p>"
    body += "</div>"
    body += "<br/>"

body += "</div>"

body += "</body>"

html = titulo + descricao + body


file_out = open("aula3.html","w")
file_out.write(html)
file_out.close()


#formfeed e brincar com html