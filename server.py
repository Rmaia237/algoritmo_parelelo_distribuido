import socket

import requests
from flask import Flask, request

app = Flask(__name__)
ip = socket.gethostbyname(socket.gethostname())
relogio = {}
url = "http://172.38.0.{}:5000?"


@app.route('/', methods=['GET'])
def ler_valores():
    # TODO trocar pela implementacao real
    msg = "#########\n"
    msg += "IP: {}\n".format(ip)
    return msg


@app.route('/', methods=['POST'])
def escrever_valores():
    # TODO trocar pela implementacao real
    var = request.args.get('teste')
    msg = "{}\n".format(var)
    for arg in request.args:
        msg += "arg -> {}\n".format(arg)
    return msg


def obter_relogio():
    global relogio
    qs = ""
    if not relogio:
        relogio = {"id2": "0", "id3": "0", "id4": "0", "id5": "0"}
    for chave, valor in sorted(relogio.items()):
        qs += "&{}={}".format(chave, valor)
    return qs


def atualizar_relogio(query_string):
    global relogio

    variaveis = str(query_string).split("&")
    for variavel in variaveis:
        if variavel.startswith("id"):
            relogio[variavel.split("=")[0]] = variavel.split("=")[1]
    return relogio


def envia_acao(id_no, acao):
    # TODO melhorar mensagem de retorno
    qs = obter_relogio()
    try:
        retorno = requests.get(url.format(id_no) + "acao=" + acao + qs, timeout=1)
        msg = "this is ok: {}".format(retorno)
    except requests.RequestException as e:
        msg = "not ok: {}".format(e)
    return msg


# TODO def incrementa_relogio_interno():
def incrementa_relogio_interno():
    pass


# TODO def recebe_acao():
def recebe_acao():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
