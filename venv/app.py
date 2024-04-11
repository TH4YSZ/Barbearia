from flask import Flask, render_template, request, jsonify
from model import Agendamento


app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para lidar com o processo de login
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    senha = request.form['senha']

    cliente = (email, senha)
        
    # Lógica para autenticação (Login)
    for dados in cliente:
        if dados['1'] == email and dados['2'] == senha:
            return True
        else:
            return jsonify({'mensagem': 'Email ou senha inválidos'})
    
    mensagem = "Usuário ou senha incorretos. Tente novamente."
    return render_template('login.html', mensagem=mensagem)


@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.form['data']
    horario = request.form['hora']
    servico_id = request.form['servico_id']
    cliente_id = request.form['id']

    agendar_model = Agendamento()
    agendar_model.agendamento(data, horario, servico_id, cliente_id)
    return render_template('agendamento.html')

@app.route('/cadastro', methods=['PUT'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']

    cad_model = cadastrar()

    if cad_model.cadastrar_cliente(nome, email, senha, telefone):
        return render_template('cadastro.html')
    else:
        return jsonify({'mensagem': 'Erro ao cadastrar cliente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)