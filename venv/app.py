from flask import Flask, redirect, render_template, request, jsonify
from model import Cliente, Agendamento

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    clientes = Cliente.consultar_clientes()

    for cliente in clientes:
        if email == cliente[0] and senha == cliente[1]:
            return redirect('/agendamento')
    return redirect('/')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']

    if Cliente.adicionar_cliente(nome, email, senha, telefone):
        return render_template('login.html')
    else:
        return 'Erro ao adicionar cliente.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)