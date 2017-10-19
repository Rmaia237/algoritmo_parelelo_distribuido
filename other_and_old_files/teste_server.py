import unittest
from os import environ

from other_and_old_files.server import Server


class TesteServer(unittest.TestCase):
    def setUp(self):
        self.id_no = 1
        environ["ID"] = str(self.id_no)
        environ["NUM_SERVERS"] = "4"
        self.server = Server()
        self.server.id = self.id_no

    def teste_ordena(self):
        origem = 1
        destino = 2
        self.server.ordena(origem, destino)


if __name__ == '__main__':
    unittest.main()
