from dao import DAO

dao = DAO()

class Cliente:
    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def cadastrar_cliente(self):
        return(dao.cadastrar_cliente(self.nome, self.email, self.senha, self.telefone))


class Agendamento:
    def agendamento(self, data, horario, servico_id, cliente_id):
        return dao.agendar_horario(data, horario, servico_id, cliente_id)

class Login:
    def autenticar():
        return(dao.consultar_clientes())
    
