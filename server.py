from flask import Flask
import socket

ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "Flask Dockerized\n"
    msg += "IP: {}\n".format(ip)
    return msg

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

