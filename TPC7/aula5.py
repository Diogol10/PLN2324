from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

with open("conceitos1.json", encoding="utf-8") as file:
    conceitos = json.load(file)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/conceitos")
def listar_Conceitos():
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/conceitos/<designacao>")
def consultar_Conceitos(designacao):
    if designacao in conceitos:
        conceito = conceitos[designacao]
        return render_template("conceito.html", conceito = conceito, designacao = designacao)
    else:
        return render_template("error.html", error = "Conceito não existe na nossa base de dados.")
        
    


@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    en = request.form.get("en")

    print(designacao,descricao,en)
    
    conceitos[designacao] = {
        "desc": descricao,
        "en": en
    }

    return render_template("conceitos.html", conceitos = conceitos)



@app.route("/conceitos/<designacao>", methods = ["DELETE"])
def delete_conceitos(designacao):
    os.rename("conceitos.json", "conceitos_backup.json")
    file_out = open("conceitos.json","w")
    del conceitos[designacao]
    json.dump(conceitos,file_out,indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/table", methods=["GET", "POST"])
def table():
    return render_template("table.html", conceitos= conceitos)


@app.route("/pesquisar", methods=["GET", "POST"])
def pesquisar():
    results = []

    if request.method == "POST":
        query = request.form.get("query", "")

        if query:
            query = query.lower()
            for designacao, info in conceitos.items():
                desc = info.get("desc", "").lower()
                en = info.get("en", "").lower()
                if query in designacao.lower() or query in desc or query in en:
                    results.append({
                        "designacao": designacao,
                        "desc": info.get("desc", ""),
                        "en": info.get("en", "")
                    })

    if not results:
        error_message = "Nenhum resultado encontrado para a pesquisa."
    else:
        error_message = None

    return render_template("pesquisar.html", results=results, error_message=error_message)



app.run(host="localhost", port=4002, debug=True)
