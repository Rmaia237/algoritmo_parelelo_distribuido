from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from servidor import Servidor


def conectado(conexao):
    resposta = str(conexao.recv(1024))
    print(server.obter_valores())
    print("Tipo: {}\n".format(type(resposta)))
    print("Resposta: {}\n".format(resposta))
    conexao.send("Conexao estabelecida\n".encode())
    conexao.close()


def envia_mensagem():
    socket_id = socket()
    socket_id.connect(("server2", 5000))
    msg = "{}|{}".format(server.id, server.relogio_interno)
    print("msg: '{}'".format(msg))
    socket_id.send(msg.encode())
    socket_id.close()
    return 0


ip = "0.0.0.0"
porta = 5000

server = Servidor()

tcp = socket(AF_INET, SOCK_STREAM)
tcp.bind((ip, porta))
tcp.listen(3)
print("Server ID: {}".format(server.id))
print("Ouvindo em {}:{}\n".format(ip, porta))

enviar = True
while True:
    if enviar and server.id == 1:
        envia_mensagem()
        enviar = False
    con, origem = tcp.accept()
    print("Conexao recebida por: {}:{}\n".format(origem[0], origem[1]))
    thread = Thread(target=conectado, args=(con,))
    thread.start()
