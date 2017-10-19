from os import getenv

import relogio_vetorial
import vetor_valores


class Servidor(object):
    def __init__(self):
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
