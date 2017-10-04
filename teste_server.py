import unittest

from server import *


class TesteServer(unittest.TestCase):
    def test_atualizar_relogio(self):
        qs = "msg=teste_msg&id2=3&id3=4&id4=5&id5=6"
        retorno = atualizar_relogio(qs)
        tipo_esperado = dict
        valor_esperado = {"id3": "4", "id4": "5", "id5": "6", "id2": "3"}
        self.assertEqual(type(retorno), tipo_esperado)
        self.assertEqual(retorno, valor_esperado)

        qs = "msg=teste_msg&id3=3&id4=4&id5=5&id6=6"
        retorno = atualizar_relogio(qs)
        valor_esperado = {"id2": "3", "id3": "3", "id4": "4", "id5": "5", "id6": "6"}
        self.assertEqual(retorno, valor_esperado)

    def teste_obter_relogio(self):
        global relogio
        qs = "msg=teste_msg&id2=3&id3=4&id4=5&id5=6"
        atualizar_relogio(qs)
        relogio_esperado = {"id3": "4", "id4": "5", "id5": "6", "id2": "3"}
        valor_esperado = "&id2=3&id3=4&id4=5&id5=6"
        self.assertEqual(relogio, relogio_esperado)
        self.assertEqual(obter_relogio(), valor_esperado)

    def teste_obter_relogio_vazio(self):
        global relogio
        del relogio
        valor_esperado = "&id2=0&id3=0&id4=0&id5=0&id6=0"
        self.assertEqual(obter_relogio(), valor_esperado)


if __name__ == '__main__':
    unittest.main()
