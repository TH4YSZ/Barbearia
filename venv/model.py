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
    def agendamento(self, servico_id, cliente_id):
        return dao.agendar()

class Login:
    def autenticar():
        return(dao.login_autenticar())
    
