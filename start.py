from flask import Flask, request

from server import Server

app = Flask(__name__)
server = Server()


@app.route('/', methods=['GET'])
def ler_valores():
    return server.mostrar_valores()


@app.route('/', methods=['POST'])
def executar_acao():
    var = request.args
    msg = "{}\n".format(var)
    for arg in request.args:
        msg += "arg -> {}\n".format(arg)
    return msg


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
