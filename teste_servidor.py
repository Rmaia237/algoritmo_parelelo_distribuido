from os import environ
from unittest import TestCase, main

from servidor import Servidor


class TesteServidor(TestCase):
    def setUp(self):
        environ["ID"] = "2"

    def teste_inicializar_servidor_com_variaveis_ambiente(self):
        environ["NUM_SERVERS"] = "5"
        servidor = Servidor()
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
        servidor = Servidor()
        num_servidores_esperado = 4
        num_servidores_obtido = servidor.num_servidores
        self.assertEqual(num_servidores_esperado, num_servidores_obtido)

    def teste_atualizar_relogio_zerado(self):
        servidor = Servidor()
        relogio = "[1, 1, 1, 1]"
        servidor.atualizar_relogio(relogio)
        valor_esperado = [1, 2, 1, 1]
        valor_obtido = servidor.relogio_interno
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_atualizar_relogio_ja_alterado(self):
        servidor = Servidor()
        servidor.relogio_interno = [1, 2, 3, 4]
        relogio = "[4, 3, 2, 1]"
        servidor.atualizar_relogio(relogio)
        valor_esperado = [4, 4, 3, 4]
        valor_obtido = servidor.relogio_interno
        self.assertEqual(valor_esperado, valor_obtido)



if __name__ == '__main__':
    main()
