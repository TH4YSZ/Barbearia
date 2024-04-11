from flask import Flask, render_template, request, jsonify
from model import Cliente, Agendamento, Login
import mysql.connector

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para lidar com o processo de login
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    senha = request.form['password']

    login_model = Login()

    dados_banco = login_model.autenticar()
        
    # Lógica para autenticação (Login)
    for dados in dados_banco:
        if dados['email'] == email and dados['senha'] == senha:
            return True
        else:
            return jsonify({'mensagem': 'Email ou senha inválidos'})
    
    mensagem = "Usuário ou senha incorretos. Tente novamente."
    return render_template('login.html', mensagem=mensagem)


@app.route('/agendar', methods=['PUT'])
def agendar():
    data = request.form['data']
    cliente_id = request.form['id']

    agendar_model = Agendamento()
    agendar_model.agendamento(data, cliente_id)
    return render_template('agendamento.html')

@app.route('/cadastro', methods=['PUT'])
def cadastrar():
    nome = request.form['email']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']

    cad_model = Cliente()

    if cad_model.cadastrar_cliente(nome, email, senha, telefone) == True:
        return render_template('agendamento.html')
    else:
        return('Erro no cadastro.')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)