import mysql.connector

class ConsultarDao:
    @staticmethod
    def conectar():
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='Barbearia')
        if conexao.is_connected():
            cursor = conexao.cursor()
        return conexao, cursor

    @staticmethod
    def consultar_clientes():
        conexao, cursor = ConsultarDao.conectar()
        cursor.execute('SELECT email, senha FROM clientes')
        clientes = []
        for cliente in cursor:
            clientes.append(cliente)
        cursor.close()
        conexao.close()
        return clientes
    
    @staticmethod
    def consultar_agendamentos():
        conexao, cursor = ConsultarDao.conectar()
        cursor.execute('SELECT * FROM agendamentos')
        agendamentos = []
        for agendamento in cursor:
            agendamentos.append(agendamento)
        cursor.close()
        conexao.close()
        return agendamentos

class AgendarDao:
    def adicionar_cliente(nome, email, senha, telefone):
        conexao, cursor = AgendarDao.conectar()
        sql = "INSERT INTO clientes (nome, telefone, email, senha) VALUES (%s, %s, %s, %s)"
        valores = (nome, telefone, email, senha)  
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Cliente adicionado com sucesso.")
            cursor.close()
            conexao.close()
            return True
        except Exception as e:
            print("Erro ao adicionar cliente:", e)
            return False

    @staticmethod
    def agendar_horario(data, horario, barbeiro):
        conexao, cursor = AgendarDao.conectar()
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


#clientes = ConsultarDao.consultar_clientes()

#for cliente in clientes:
    #print(cliente)