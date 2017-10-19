from json import loads
from os import getenv

import relogio_vetorial
import vetor_valores
from conexao import Conexao


class Servidor(object):
    def __init__(self):
        self.id = int(getenv("ID"))
        self.num_servidores = int(getenv("NUM_SERVERS")) if getenv("NUM_SERVERS") else 4
        self.url = "http://server{}:5000?".format(self.id)
        self.relogio_interno = relogio_vetorial.obter_relogio_vetorial(self.num_servidores)
        self.vetor_valores = vetor_valores.obter_vetor_valores(self.num_servidores, self.id)

    def obter_valores(self):
        msg = "ID: {}\n".format(self.id)
        msg += "URL: {}\n".format(self.url)
        msg += "Num Servidores: {}\n".format(self.num_servidores)
        msg += "Relogio: {}\n".format(self.relogio_interno)
        msg += "Valores: {}\n".format(self.vetor_valores)
        return msg

    def atualizar_relogio(self, relogio_str):
        self.relogio_interno = relogio_vetorial.atualizar(self.relogio_interno, loads(relogio_str))
        self.relogio_interno = relogio_vetorial.incrementar(self.relogio_interno, self.id)

    def start(self):
        conexao = Conexao()
        conexao.prepara_conexao()

        enviar = True
        while True:
            if enviar and self.id == 1:
                msg = "{}|{}".format(self.id, self.relogio_interno)
                Conexao.envia_mensagem(2, msg)
                enviar = False
            conexao.conecta()


if __name__ == '__main__':
    servidor = Servidor()
    servidor.start()
