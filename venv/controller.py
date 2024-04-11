from flask import jsonify, request
from model import Cliente, Agendamento, Login
from dao import ClienteDAO, AgendamentoDAO

cliente_dao = ClienteDAO()
agendamento_dao = AgendamentoDAO()
login_model = Login()

class ClienteController:
    def cadastrar_cliente():
        dados = request.json
        cliente = Cliente(None, dados['nome'], dados['email'], dados['senha'])
        if cliente_dao.cadastrar_cliente(cliente):
            return jsonify({'mensagem': 'Cliente cadastrado com sucesso'}), 201
        else:
            return jsonify({'mensagem': 'Erro ao cadastrar cliente'}), 500

class AgendamentoController:
    def agendar():
        dados = request.json
        cliente_id = dados['cliente_id']
        data = dados['data']
        if agendamento_dao.verificar_disponibilidade(data):
            agendamento = Agendamento(None, cliente_id, data)
            # Lógica para agendar o cliente
            return jsonify({'mensagem': 'Agendamento realizado com sucesso'}), 201
        else:
            return jsonify({'mensagem': 'Data não disponível'}), 400

class Login:
    def autenticar():
        dados = request.json
        email = dados['email']
        senha = dados['senha']

        dados_banco = login_model.autenticar()
        
        # Lógica para autenticação (Login)
        for dados in dados_banco:
            if dados['email'] == email and dados['senha'] == senha:
                return True
            else:
                return jsonify({'mensagem': 'Email ou senha inválidos'})