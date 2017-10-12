import unittest

from mock import patch

from server import Server


class TesteServer(unittest.TestCase):
    def setUp(self):
        self.id_no = 1
        self.server = Server()
        self.server.id = self.id_no

    def test_atualizar_relogio(self):
        qs = "acao=teste_acao&id1=2&id2=3&id3=4&id4=5"
        self.server.atualizar_vetor_relogios(qs)
        tipo_esperado = dict
        tipo_obtido = type(self.server.vetor_relogios)
        valor_esperado = {"id1": 2, "id2": 3, "id3": 4, "id4": 5}
        valor_obtido = self.server.vetor_relogios
        self.assertEqual(tipo_obtido, tipo_esperado)
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_obter_qs_relogio(self):
        qs = "acao=teste_msg&id1=2&id2=3&id3=4&id4=5"
        self.server.atualizar_vetor_relogios(qs)
        relogio_esperado = {"id1": 2, "id2": 3, "id3": 4, "id4": 5}
        relogio_obtido = self.server.vetor_relogios
        valor_esperado = "&id1=2&id2=3&id3=4&id4=5"
        valor_obtido = self.server.obter_querystring_vetor_relogios()
        self.assertEqual(relogio_obtido, relogio_esperado)
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_obter_qs_relogio_vazio(self):
        relogio_esperado = {"id1": 0, "id2": 0, "id3": 0, "id4": 0}
        relogio_obtido = self.server.vetor_relogios
        valor_esperado = "&id1=0&id2=0&id3=0&id4=0"
        valor_obtido = self.server.obter_querystring_vetor_relogios()
        self.assertEqual(relogio_obtido, relogio_esperado)
        self.assertEqual(valor_obtido, valor_esperado)

    @patch("requests.get")
    def teste_envia_com_sucesso(self, mock_get):
        mock_get.return_value = "teste_retorno"
        acao = "w3"
        parametro_esperado = "http://server1:5000?acao=w3&id1=1&id2=0&id3=0&id4=0"
        retorno_esperado = "this is ok: teste_retorno"
        retorno_obtido = self.server.envia_acao(self.id_no, acao)
        mock_get.assert_called_with(parametro_esperado, timeout=1)
        self.assertEqual(retorno_obtido, retorno_esperado)

    def teste_envia_com_falha(self):
        # TODO melhorar mensagem de retorno
        id_no = "1"
        acao = "w3"
        retorno_esperado = "not ok:"
        retorno_obtido = self.server.envia_acao(id_no, acao)
        self.assertIn(retorno_esperado, retorno_obtido)

    def teste_incrementa_relogio_interno(self):
        self.server.incrementa_relogio_interno()
        valor_esperado = {"id1": 1, "id2": 0, "id3": 0, "id4": 0}
        valor_obtido = self.server.vetor_relogios
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_recebe_acao(self):
        # TODO Fazer o teste
        pass


if __name__ == '__main__':
    unittest.main()
