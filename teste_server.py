import unittest

import server


class TesteServer(unittest.TestCase):
    def test_atualizar_relogio(self):
        qs = "msg=teste_msg&id2=3&id3=4&id4=5&id5=6"
        retorno = server.atualizar_relogio(qs)
        tipo_esperado = dict
        valor_esperado = {"id3": "4", "id4": "5", "id5": "6", "id2": "3"}
        self.assertEqual(type(retorno), tipo_esperado)
        self.assertEqual(retorno, valor_esperado)

    def teste_obter_relogio(self):
        qs = "msg=teste_msg&id2=3&id3=4&id4=5&id5=6"
        server.atualizar_relogio(qs)
        relogio_esperado = {"id2": "3", "id3": "4", "id4": "5", "id5": "6"}
        valor_esperado = "&id2=3&id3=4&id4=5&id5=6"
        self.assertEqual(server.relogio, relogio_esperado)
        self.assertEqual(server.obter_relogio(), valor_esperado)

    def teste_obter_relogio_vazio(self):
        server.relogio = {}
        valor_esperado = "&id2=0&id3=0&id4=0&id5=0"
        self.assertEqual(server.obter_relogio(), valor_esperado)


if __name__ == '__main__':
    unittest.main()
