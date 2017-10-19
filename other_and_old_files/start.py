from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from other_and_old_files.server import Server


def retorna_query_string(resposta):
    print(resposta.split(" ")[1])


def conectado(conexao):
    resposta = str(conexao.recv(1024))
    retorna_query_string(resposta)
    print(server.mostrar_valores())
    # print("Resposta: {}\n".format(resposta))
    conexao.send("Conexao estabelecida\n")
    conexao.close()


ip = "0.0.0.0"
porta = 5000

server = Server()

tcp = socket(AF_INET, SOCK_STREAM)
tcp.bind((ip, porta))
tcp.listen(3)
print("Server ID: {}".format(server.id))
print("Ouvindo em {}:{}\n".format(ip, porta))

while True:
    con, origem = tcp.accept()
    print("Conexao recebida por: {}:{}\n".format(origem[0], origem[1]))
    thread = Thread(target=conectado, args=(con,))
    thread.start()
