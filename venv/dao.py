import mysql.connector

class DAO:
    def conectar():
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='Barbearia')
        if conexao.is_connected():
            cursor = conexao.cursor()
        return conexao, cursor

    def consultar_clientes(conectar):
        conexao, cursor = conectar()
        cursor.execute('SELECT email, senha FROM clientes')
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes

    def adicionar_cliente(nome, email, senha, telefone, conectar):
        conexao, cursor = conectar()
        sql = "INSERT INTO clientes (nome, telefone, email, password) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, senha, telefone)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente adicionado com sucesso.")
        cursor.close()
        conexao.close()

    
    def agendar_horario(data, horario, servico_id, cliente_id, conectar):
        conexao, cursor = conectar()
        cursor.execute("SELECT * FROM Agendamentos WHERE Data = %s AND Horario = %s (data, horario)")
        agendamento_existente = cursor.fetchone()
        if agendamento_existente:
            print("Já existe um agendamento para o mesmo dia, horário e barbeiro.")
            cursor.close()
            conexao.close()
            return

        sql = "INSERT INTO Agendamentos (Data, Horario, Barbeiro) VALUES (%s, %s, %s)"
        valores = (data, horario)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Agendamento realizado com sucesso.")
        cursor.close()
        conexao.close()



