from flask import Flask, request
import socket
import requests

ip = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)


relogio = {}

# querystring = "teste=seraquevai"
# resposta = requests.post("http://172.18.0.3:5000?{}".format(querystring))
# msg += resposta.text


@app.route('/', methods=['GET'])
def ler_valores():
    msg = "#########\n"
    msg += "IP: {}\n".format(ip)
    return msg


@app.route('/', methods=['POST'])
def escrever_valores():
    var = request.args.get('teste')
    msg = "{}\n".format(var)
    for arg in request.args:
        msg += "arg -> {}\n".format(arg)
    return msg


def obter_relogio():
    global relogio
    if not relogio:
        relogio = {"id2": "0", "id3": "0", "id4": "0", "id5": "0", "id6": "0"}
    return relogio


def atualizar_relogio(query_string):
    global relogio

    variaveis = str(query_string).split("&")
    for variavel in variaveis:
        if variavel.startswith("id"):
            relogio[variavel.split("=")[0]] = variavel.split("=")[1]
    return relogio


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#
# import socket
# import os
# import sys
# HOST = ''              # Endereco IP do Servidor
# PORT = 5000            # Porta que o Servidor esta
# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# orig = (HOST, PORT)
# tcp.bind(orig)
# tcp.listen(1)
# while True:
#     con, cliente = tcp.accept()
#     pid = os.fork()
#     if pid == 0:
#         tcp.close()
#         print('Conectado por', cliente)
#         while True:
#             msg = con.recv(1024)
#             if not msg:
#                 break
#             print(cliente, msg)
#         print('Finalizando conexao do cliente', cliente)
#         con.close()
#         sys.exit(0)
#     else:
#         con.close()
