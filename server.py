import socket

import requests


class Server(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.relogio = {}
        self.url = "http://server{}:5000?"

    def atualizar_relogio(self, query_string):
        variaveis = str(query_string).split("&")
        for variavel in variaveis:
            if variavel.startswith("id"):
                self.relogio[variavel.split("=")[0]] = variavel.split("=")[1]

    def obter_relogio(self):
        qs = ""
        if not self.relogio:
            self.relogio = {"id1": "0", "id2": "0", "id3": "0", "id4": "0"}
        for chave, valor in sorted(self.relogio.items()):
            qs += "&{}={}".format(chave, valor)
        return qs

    def envia_acao(self, id_no, acao):
        # TODO melhorar mensagem de retorno
        qs = self.obter_relogio()
        try:
            retorno = requests.get(self.url.format(id_no) + "acao=" + acao + qs, timeout=1)
            msg = "this is ok: {}".format(retorno)
        except requests.RequestException as e:
            msg = "not ok: {}".format(e)
        return msg

    # TODO def incrementa_relogio_interno():
    def incrementa_relogio_interno(self):

        pass

    # TODO def recebe_acao():
    def recebe_acao(self):
        pass
