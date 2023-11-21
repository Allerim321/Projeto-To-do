from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

############### Get
@app.route('/', methods=['GET'])
def index():
    item = pd.read_csv('Text.csv')
    dicionario = item.to_dict('records')
    return jsonify(dicionario)


################ Post
@app.route('/add', methods=['POST'])
def login():
    item = request.json
    ler = pd.read_csv("Text.csv")
    dicionario = ler.to_dict('records')
    id = len(dicionario)+1
    with open ("Text.csv", "a") as arquivo:
        arquivo.write(f"{id}, {item}\n")


############### Update
@app.route("/update/<int:id>", methods=["PUT"])
def atualizarTarefa(id):
    item = request.json
    ler = pd.read_csv('Text.csv')
    dicionario = ler.to_dict('records')

    with open("Text.csv", "w") as arquivo:
        arquivo.write("Id, Tarefa\n")
        for percorrer in dicionario:
            if percorrer["Id"] != id:
                arquivo.write(f"{percorrer['Id']},{percorrer['Tarefa']}\n")
            else:
                arquivo.write(f"{id},{item['Tarefa']}\n")
                
                return (f"Tarefa {id} atualizada com sucesso!\nTarefa antiga: {percorrer['Tarefa']}\nTarefa nova: {item['Tarefa']}\n")

    ler = pd.read_csv('Text.csv')
    dicionario = ler.to_dict('records')
    return jsonify(dicionario)


############### Delete
@app.route("/delete/<int:id>", methods=['DELETE'])
def deleteTarefas(id):
    tarefas = pd.read_csv('Text.csv')
    tarefas = tarefas[tarefas['Id'] != id].reset_index(drop=True)
    tarefas['Id'] = range(1, len(tarefas) + 1)
    tarefas.to_csv('Text.csv', index=False)
    return jsonify(tarefas.to_dict('records'))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
