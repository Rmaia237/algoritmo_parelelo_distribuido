from flask import Flask, request

from server import Server

app = Flask(__name__)
server = Server()


@app.route('/', methods=['GET'])
def ler_valores():
    # TODO trocar pela implementacao real
    msg = "#########\n"
    msg += "IP: {}\n".format(server.ip)
    msg += "ID: {}\n".format(server.id)
    return msg


@app.route('/', methods=['POST'])
def escrever_valores():
    # TODO trocar pela implementacao real
    var = request.args.get('teste')
    msg = "{}\n".format(var)
    for arg in request.args:
        msg += "arg -> {}\n".format(arg)
    return msg


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
