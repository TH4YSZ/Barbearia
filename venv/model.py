class Cliente:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

class Agendamento:
    def __init__(self, id, cliente_id, data):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
