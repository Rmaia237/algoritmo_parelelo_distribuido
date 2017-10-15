from os import getenv

from requests import post


class Server(object):
    def __init__(self):
        self.id = int(getenv("ID"))
        self.num_servers = getenv("NUM_SERVERS") if getenv("NUM_SERVERS") else 4
        self.vetor_relogios = self.__inicializa_vetor_relogios()
        self.vetor_valores = self.__inicializa_vetor_valores()
        self.url = "http://server{}:5000?"
        self.msg = "#########\n"

    def __inicializa_vetor_relogios(self):
        vetor = {}
        for i in range(int(self.num_servers)):
            vetor["id{}".format(i + 1)] = 0
        return vetor

    def __inicializa_vetor_valores(self):
        vetor = []
        for i in range(int(self.num_servers)):
            vetor.append("-")
        vetor[self.id - 1] = 0
        return vetor

    def mostrar_valores(self):
        msg = "#########\n"
        msg += "ID: {}\n".format(self.id)
        msg += "Valores: {}\n".format(self.vetor_valores)
        msg += "Relogios: {}\n".format(self.vetor_relogios)
        msg += "Msg: \n{}\n".format(self.msg)
        return msg

    def ordena(self, origem, destino):
        self.msg += "Origem: {}\n".format(origem)
        self.msg += "Destino: {}\n".format(destino)
        retorno = post(self.url.format(origem) + "envia={}".format(destino))
        self.msg += retorno.text

    def recebe_acao(self, query_string):
        for chave, valor in query_string.items():
            self.msg = "{} -> {}".format(chave, valor)
        return self.msg
