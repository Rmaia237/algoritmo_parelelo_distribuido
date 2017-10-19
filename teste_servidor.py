from os import environ
from unittest import TestCase, main

from servidor import Server


class TesteServidor(TestCase):
    def setUp(self):
        environ["ID"] = "2"
        environ["NUM_SERVERS"] = "5"

    def teste_inicializar_servidor_com_variaveis_ambiente(self):
        servidor = Server()
        id_esperado = 2
        id_obtido = servidor.id
        num_servidores_esperado = 5
        num_servidores_obtido = servidor.num_servidores
        url_esperada = "http://server2:5000?"
        url_obtida = servidor.url
        self.assertEqual(id_esperado, id_obtido)
        self.assertEqual(num_servidores_esperado, num_servidores_obtido)
        self.assertEqual(url_esperada, url_obtida)

    def teste_inicializar_servidor_sem_num_servidores(self):
        del environ["NUM_SERVERS"]
        servidor = Server()
        num_servidores_esperado = 4
        num_servidores_obtido = servidor.num_servidores
        self.assertEqual(num_servidores_esperado, num_servidores_obtido)


if __name__ == '__main__':
    main()
