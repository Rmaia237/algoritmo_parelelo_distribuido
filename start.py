from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from servidor import Servidor


def retorna_query_string(resposta):
    print(type(resposta))
    print(resposta)
    # print(resposta.split(" ")[1])


def conectado(conexao):
    resposta = str(conexao.recv(1024))
    retorna_query_string(resposta)
    print(server.obter_valores())
    print("Resposta: {}\n".format(resposta))
    conexao.send("Conexao estabelecida\n".encode())
    conexao.close()


def envia_mensagem():
    print("enviando mensagem para o 2")
    socket_id = socket()
    socket_id.connect(("server2", int("5000")))
    msg = "{}.{}".format(server.id, server.relogio_interno)
    print("msg: '{}'".format(msg))
    retorno = socket_id.send(msg.encode())
    print(retorno)
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
    print(enviar)
    print(server.id)
    if enviar and server.id == 1:
        envia_mensagem()
        enviar = False
    con, origem = tcp.accept()
    print("Conexao recebida por: {}:{}\n".format(origem[0], origem[1]))
    thread = Thread(target=conectado, args=(con,))
    thread.start()

