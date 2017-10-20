from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Conexao(object):
    def __init__(self):
        self.ip = "0.0.0.0"
        self.porta = 5000
        self.tcp = socket(AF_INET, SOCK_STREAM)

    def prepara_conexao(self):
        self.tcp.bind((self.ip, self.porta))
        self.tcp.listen(3)
        print("Ouvindo em {}:{}\n".format(self.ip, self.porta))

    def conecta(self):
        conexao, origem = self.tcp.accept()
        print("Conexao recebida por: {}:{}\n".format(origem[0], origem[1]))
        thread = Thread(target=self.recebe_conexao, args=(conexao,))
        thread.start()

    @staticmethod
    def recebe_conexao(conexao):
        resposta = str(conexao.recv(1024))
        print(resposta)
        conexao.send("Conexao estabelecida\n".encode())
        conexao.close()

    @staticmethod
    def envia_mensagem(id_servidor, msg):
        socket_id = socket()
        socket_id.connect(("server{}".format(id_servidor), 5000))
        print("msg: '{}'".format(msg))
        socket_id.send(msg.encode())
        socket_id.close()
        return 0
