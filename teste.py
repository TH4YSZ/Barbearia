import mysql.connector

def conectar():
    conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='Barbearia')
    if conexao.is_connected():
        print('Conectado com sucesso')
        cursor = conexao.cursor()
    return conexao, cursor

def consultar_clientes():
    conexao, cursor = conectar()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes

def adicionar_cliente(nome, telefone, email, password):
    conexao, cursor = conectar()
    sql = "INSERT INTO clientes (nome, telefone, email, password) VALUES (%s, %s, %s, %s)"
    valores = (nome, telefone, email, password)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente adicionado com sucesso.")
    cursor.close()
    conexao.close()


def consultar_agendamentos(conectar):
    conexao, cursor = conectar()
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return agendamentos
    
def agendar_horario(data, horario, barbeiro):
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM Agendamentos WHERE Data = %s AND Horario = %s AND Barbeiro = %s", (data, horario, barbeiro))
    agendamento_existente = cursor.fetchone()
    if agendamento_existente:
        print("Já existe um agendamento para o mesmo dia, horário e barbeiro.")
        cursor.close()
        conexao.close()
        return

    sql = "INSERT INTO Agendamentos (Data, Horario, Barbeiro) VALUES (%s, %s, %s)"
    valores = (data, horario, barbeiro)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Agendamento realizado com sucesso.")
    cursor.close()
    conexao.close()