import mysql.connector
from flask import jsonify, request
from model import Cliente, Agendamento
from config import MYSQL_CONFIG

class DAO:
    def cadastrar_cliente():
        try:
            conn = mysql.connector.connect(**MYSQL_CONFIG)
            cursor = conn.cursor()

            dados = request.json
            cliente = Cliente(None, dados['nome'], dados['email'], dados['senha'])

            query = "INSERT INTO cliente (nome, email, senha) VALUES (%s, %s, %s)"
            cursor.execute(query, (cliente.nome, cliente.email, cliente.senha))

            conn.commit()
            return jsonify({'mensagem': 'Cliente cadastrado com sucesso'}), 201
        except mysql.connector.Error as err:
            print("Erro ao cadastrar cliente:", err)
            return jsonify({'mensagem': 'Erro ao cadastrar cliente'}), 500
        finally:
            cursor.close()
            conn.close()

    def agendar():
        try:
            conn = mysql.connector.connect(**MYSQL_CONFIG)
            cursor = conn.cursor()

            dados = request.json
            cliente_id = dados['cliente_id']
            data = dados['data']
            agendamento = Agendamento(None, cliente_id, data)

            # Lógica para agendar o cliente

            return jsonify({'mensagem': 'Agendamento realizado com sucesso'}), 201
        except mysql.connector.Error as err:
            print("Erro ao agendar cliente:", err)
            return jsonify({'mensagem': 'Erro ao agendar cliente'}), 500
        finally:
            cursor.close()
            conn.close()
