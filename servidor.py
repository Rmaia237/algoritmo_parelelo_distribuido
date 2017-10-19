from os import getenv

import relogio_vetorial
import vetor_valores


class Server(object):
    def __init__(self):
        self.id = int(getenv("ID"))
        self.num_servidores = int(getenv("NUM_SERVERS")) if getenv("NUM_SERVERS") else 4
        self.url = "http://server{}:5000?".format(self.id)
        self.vetor_relogios = relogio_vetorial.obter_relogio_vetorial(self.num_servidores)
        self.vetor_valores = vetor_valores.obter_vetor_valores(self.num_servidores, self.id)

