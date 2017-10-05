import unittest

from mock import patch

import server


class TesteServer(unittest.TestCase):
    def test_atualizar_relogio(self):
        qs = "acao=teste_acao&id2=3&id3=4&id4=5&id5=6"
        retorno = server.atualizar_relogio(qs)
        tipo_esperado = dict
        valor_esperado = {"id3": "4", "id4": "5", "id5": "6", "id2": "3"}
        self.assertEqual(type(retorno), tipo_esperado)
        self.assertEqual(retorno, valor_esperado)

    def teste_obter_relogio(self):
        qs = "acao=teste_msg&id2=3&id3=4&id4=5&id5=6"
        server.atualizar_relogio(qs)
        relogio_esperado = {"id2": "3", "id3": "4", "id4": "5", "id5": "6"}
        valor_esperado = "&id2=3&id3=4&id4=5&id5=6"
        self.assertEqual(server.relogio, relogio_esperado)
        self.assertEqual(server.obter_relogio(), valor_esperado)

    def teste_obter_relogio_vazio(self):
        server.relogio = {}
        valor_esperado = "&id2=0&id3=0&id4=0&id5=0"
        self.assertEqual(server.obter_relogio(), valor_esperado)

    @patch("requests.get")
    def teste_envia_com_sucesso(self, mock_get):
        mock_get.return_value = "teste_retorno"
        server.relogio = {}
        id_no = "1"
        acao = "w3"
        parametro_esperado = "http://172.38.0.1:5000?acao=w3&id2=0&id3=0&id4=0&id5=0"
        retorno_esperado = "this is ok: teste_retorno"
        retorno = server.envia_acao(id_no, acao)
        mock_get.assert_called_with(parametro_esperado, timeout=1)
        self.assertEqual(retorno_esperado, retorno)

    def teste_envia_com_falha(self):
        # TODO melhorar mensagem de retorno
        id_no = "1"
        acao = "w3"
        retorno_esperado = "not ok:"
        retorno = server.envia_acao(id_no, acao)
        self.assertIn(retorno_esperado, retorno)

    def teste_recebe_acao(self):
        # TODO Fazer o teste
        pass


if __name__ == '__main__':
    unittest.main()
