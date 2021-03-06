import socket
from os import getenv

import requests


class Server(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.id = int(getenv("ID"))
        self.num_servers = getenv("NUM_SERVERS") if getenv("NUM_SERVERS") else 4
        self.vetor_relogios = self.__inicializa_vetor_relogios()
        self.vetor_valores = self.__inicializa_vetor_valores()
        self.url = "http://server{}:5000?"

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

    def atualizar_vetor_relogios(self, query_string):
        variaveis = str(query_string).split("&")
        for variavel in variaveis:
            if variavel.startswith("id"):
                id_no = variavel.split("=")[0]
                valor = int(variavel.split("=")[1])
                # no = int(variavel.split("=")[0].replace("id", ""))
                # if no == self.id:
                #     pass
                # else:
                #     self.vetor_relogios[id_no] = max([valor, self.vetor_relogios[id_no]])
                self.vetor_relogios[id_no] = max([valor, self.vetor_relogios[id_no]])

    def obter_query_string_vetor_relogios(self):
        qs = ""
        for relogio, valor in sorted(self.vetor_relogios.items()):
            qs += "&{}={}".format(relogio, valor)
        return qs

    def incrementa_relogio_interno(self):
        for relogio, valor in self.vetor_relogios.items():
            if int(str(relogio).replace("id", "")) == self.id:
                self.vetor_relogios[relogio] += 1

    def envia_acao(self, id_no, acao):
        self.incrementa_relogio_interno()
        qs = self.obter_query_string_vetor_relogios()
        try:
            retorno = requests.get(self.url.format(id_no) + "acao=" + acao + qs, timeout=1)
            msg = str(retorno)
        except requests.RequestException as e:
            msg = str(e)
        return msg

    def recebe_acao(self, acao):
        self.incrementa_relogio_interno()
        if str(acao).startswith("w"):
            valores = str(acao).replace("w", "").split(",")
            self.escreve_valores(valores)
            msg = "ok"
        elif str(acao).startswith("r"):
            msg = str(self.vetor_valores)
        else:
            msg = "nok"
        return msg

    def mostrar_valores(self):
        msg = "#########\n"
        msg += "IP: {}\n".format(self.ip)
        msg += "ID: {}\n".format(self.id)
        msg += "Valores: {}\n".format(self.vetor_valores)
        msg += "Relogios: {}\n".format(self.vetor_relogios)
        return msg

    def escreve_valores(self, valores):
        if len(valores) > 1:
            for i in range(len(valores)):
                if valores[i] != "-":
                    self.vetor_valores[i] = int(valores[i])
                    if i + 1 != self.id:
                        self.envia_acao(i + 1, "w{}".format(valores[i]))
        else:
            self.vetor_valores[self.id - 1] = int(valores[0])
