import mysql.connector
from flask import request
from model import Cliente

class DAO:
    def conectar():
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='Barbearia'
        )
        
        if conexao.is_connected():
            print('Conectado com sucesso')
            cursor = conexao.cursor()
        return conexao, cursor

    def cadastrar_cliente():
        conexao, cursor = DAO.conectar()
        try:
            dados = request.json
            cliente = Cliente(None, dados['nome'], dados['email'], dados['senha'])
            cursor.execute('INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s)', (cliente.nome, cliente.email, cliente.senha))
            conexao.commit()
            return True
        except mysql.connector.Error as err:
            print("Erro ao cadastrar cliente:", err)
            return False
        finally:
            cursor.close()
            conexao.close()

    def agendar():
        conexao, cursor = DAO.conectar()
        try:
            dados = request.json
            cliente_id = dados['cliente_id']
            data = dados['data']
            cursor.execute('INSERT INTO agendamentos (cliente_id, data) VALUES (%s, %s)', (cliente_id, data))
            conexao.commit()
            return True
        except mysql.connector.Error as err:
            print("Erro ao agendar cliente:", err)
            return False
        finally:
            cursor.close()
            conexao.close()

    def listar_preco():
        conexao, cursor = DAO.conectar()
        resultado = cursor.execute('SELECT * FROM PrecosCortes')
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()

    def login_autenticar():
        conexao, cursor = DAO.conectar()
        try:
            resultado = cursor.execute('SELECT email, senha FROM clientes')
            resultado = cursor.fetchall()
            return(resultado)
        except:
            return('Erro ao consultar o banco.')
        finally:
            cursor.close()
            conexao.close()