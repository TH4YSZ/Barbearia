from dao import ConsultarDao, AgendarDao

class Cliente:
    @staticmethod
    def consultar_clientes():
        return ConsultarDao.consultar_clientes()

    @staticmethod
    def adicionar_cliente(nome, telefone, email, senha):
        return AgendarDao.adicionar_cliente(nome, email, senha, telefone)

class Agendamento:
    @staticmethod
    def consultar_agendamentos():
        return ConsultarDao.consultar_agendamentos()

    @staticmethod
    def agendar_horario(data, horario, barbeiro):
        return AgendarDao.agendar_horario(data, horario, barbeiro)
