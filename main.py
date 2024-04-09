from flask import Flask, request
from dao import DAO
from view import mostrar_formulario_cadastro, mostrar_formulario_agendamento

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'GET':
        return mostrar_formulario_cadastro()
    elif request.method == 'POST':
        return DAO.cadastrar_cliente()

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'GET':
        return mostrar_formulario_agendamento()
    elif request.method == 'POST':
        return DAO.agendar()

if __name__ == '__main__':
    app.run(debug=True)
