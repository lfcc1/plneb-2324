from flask import Flask
import json

app = Flask(__name__)

file = open("../Aula4/conceitos.json")
conceitos = json.load(file)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/conceitos")
def listar_Conceitos():
    return conceitos

@app.route("/conceitos/<designacao>")
def consultar_Conceitos(designacao):
    return conceitos[designacao]


@app.route("/counceitos/<designacao>", methods=["PUT"])
def editar_Conceitos(designacao):


app.run(host="localhost", port=4002, debug=True)
