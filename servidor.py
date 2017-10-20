from json import loads
from os import getenv
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import relogio_vetorial
import vetor_valores


class Servidor(object):
    def __init__(self):
        self.ip = "0.0.0.0"
        self.porta = 5000
        self.tcp = socket(AF_INET, SOCK_STREAM)

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
        self.incrementar_relogio()

    def incrementar_relogio(self):
        self.relogio_interno = relogio_vetorial.incrementar(self.relogio_interno, self.id)

    ##############
    # parte da classe sem cobertura de testes
    ##############
    def prepara_conexao(self):
        self.tcp.bind((self.ip, self.porta))
        self.tcp.listen(3)
        print("Ouvindo em {}:{}".format(self.ip, self.porta))

    def conecta(self):
        conexao, origem = self.tcp.accept()
        print("Conexao recebida por: {}:{}".format(origem[0], origem[1]))
        thread = Thread(target=self.recebe_conexao, args=(conexao,))
        thread.start()

    def recebe_conexao(self, conexao):
        resposta = conexao.recv(1024).decode("utf-8")
        id_servidor, relogio = resposta.split("|")
        self.recebe_mensagem(id_servidor, relogio)
        # conexao.send("Conexao estabelecida".encode())
        conexao.close()

    def recebe_mensagem(self, id_servidor, relogio):
        print("Mensagem recebida do server{}".format(id_servidor))
        print("Com o relogio: {}".format(relogio))
        self.atualizar_relogio(relogio)
        print("Entao atualizo meu relogio: {}".format(self.relogio_interno))

    @staticmethod
    def envia_mensagem(id_servidor, msg):
        socket_id = socket()
        socket_id.connect(("server{}".format(id_servidor), 5000))
        print("Enviando mensagem: '{}'".format(msg))
        socket_id.send(msg.encode())
        socket_id.close()
        return 0

    def start(self):
        self.prepara_conexao()
        enviar = True
        while True:
            if enviar and self.id == 1:
                self.incrementar_relogio()
                msg = "{}|{}".format(self.id, self.relogio_interno)
                self.envia_mensagem(2, msg)
                enviar = False
            self.conecta()


if __name__ == '__main__':
    servidor = Servidor()
    servidor.start()
