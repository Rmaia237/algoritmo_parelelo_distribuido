import socket
from os import getenv

import requests


class Server(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.id = getenv("ID")
        self.num_servers = getenv("NUM_SERVERS")
        self.vetor_relogios = self.__inicializa_vetor_relogios()
        self.url = "http://server{}:5000?"

    def __inicializa_vetor_relogios(self):
        if self.num_servers:
            vetor = {}
            for i in range(int(self.num_servers)):
                vetor["id{}".format(i + 1)] = 0
            return vetor
        else:
            return {"id1": 0, "id2": 0, "id3": 0, "id4": 0}

    def atualizar_vetor_relogios(self, query_string):
        variaveis = str(query_string).split("&")
        for variavel in variaveis:
            if variavel.startswith("id"):
                id_no = variavel.split("=")[0]
                valor = int(variavel.split("=")[1])
                self.vetor_relogios[id_no] = valor

    def obter_querystring_vetor_relogios(self):
        qs = ""
        for relogio, valor in sorted(self.vetor_relogios.items()):
            qs += "&{}={}".format(relogio, valor)
        return qs

    def envia_acao(self, id_no, acao):
        self.incrementa_relogio_interno()
        # TODO melhorar mensagem de retorno
        qs = self.obter_querystring_vetor_relogios()
        try:
            retorno = requests.get(self.url.format(id_no) + "acao=" + acao + qs, timeout=1)
            msg = "this is ok: {}".format(retorno)
        except requests.RequestException as e:
            msg = "not ok: {}".format(e)
        return msg

    def incrementa_relogio_interno(self):
        for relogio, valor in self.vetor_relogios.items():
            if int(str(relogio).replace("id", "")) == self.id:
                self.vetor_relogios[relogio] += 1

    # TODO def recebe_acao():
    def recebe_acao(self):
        self.incrementa_relogio_interno()
        pass
