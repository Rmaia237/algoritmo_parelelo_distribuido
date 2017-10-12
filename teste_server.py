import unittest
from os import environ

from mock import patch

from server import Server


class TesteServer(unittest.TestCase):
    def setUp(self):
        self.id_no = 1
        environ["NUM_SERVERS"] = "4"
        self.server = Server()
        self.server.id = self.id_no

    def test_atualizar_relogio(self):
        query_string = "acao=teste_acao&id1=2&id2=3&id3=4&id4=5"
        self.server.vetor_relogios = {"id1": 2, "id2": 1, "id3": 5, "id4": 0}
        self.server.atualizar_vetor_relogios(query_string)
        tipo_esperado = dict
        tipo_obtido = type(self.server.vetor_relogios)
        valor_esperado = {"id1": 2, "id2": 3, "id3": 5, "id4": 5}
        valor_obtido = self.server.vetor_relogios
        self.assertEqual(tipo_obtido, tipo_esperado)
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_obter_query_string_vetor_relogios(self):
        self.server.vetor_relogios = {"id1": 2, "id2": 3, "id3": 4, "id4": 5}
        valor_esperado = "&id1=2&id2=3&id3=4&id4=5"
        valor_obtido = self.server.obter_query_string_vetor_relogios()
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_obter_qurey_string_vetor_relogios_vazio(self):
        relogio_esperado = {"id1": 0, "id2": 0, "id3": 0, "id4": 0}
        relogio_obtido = self.server.vetor_relogios
        valor_esperado = "&id1=0&id2=0&id3=0&id4=0"
        valor_obtido = self.server.obter_query_string_vetor_relogios()
        self.assertEqual(relogio_obtido, relogio_esperado)
        self.assertEqual(valor_obtido, valor_esperado)

    @patch("requests.get")
    def teste_envia_com_sucesso(self, mock_get):
        mock_get.return_value = "teste_retorno\n"
        acao = "w3"
        parametro_esperado = "http://server1:5000?acao=w3&id1=1&id2=0&id3=0&id4=0"
        retorno_esperado = "teste_retorno\n"
        retorno_obtido = self.server.envia_acao(self.id_no, acao)
        relogio_interno_esperado = 1
        relogio_interno_obtido = self.server.vetor_relogios["id{}".format(self.id_no)]
        mock_get.assert_called_with(parametro_esperado, timeout=1)
        self.assertEqual(retorno_obtido, retorno_esperado)
        self.assertEqual(relogio_interno_obtido, relogio_interno_esperado)

    def teste_envia_com_falha(self):
        id_no = "1"
        acao = "w3"
        retorno_esperado = "Failed to establish a new connection"
        retorno_obtido = self.server.envia_acao(id_no, acao)
        relogio_interno_esperado = 1
        relogio_interno_obtido = self.server.vetor_relogios["id{}".format(self.id_no)]
        self.assertIn(retorno_esperado, retorno_obtido)
        self.assertEqual(relogio_interno_obtido, relogio_interno_esperado)

    def teste_incrementa_relogio_interno(self):
        self.server.incrementa_relogio_interno()
        valor_esperado = {"id1": 1, "id2": 0, "id3": 0, "id4": 0}
        valor_obtido = self.server.vetor_relogios
        self.assertEqual(valor_obtido, valor_esperado)

    def teste_recebe_acao_escrita(self):
        acao = "w3"
        retorno_esperado = "ok"
        retorno_obtido = self.server.recebe_acao(acao)
        valor_esperado = 3
        valor_obtido = self.server.valor_interno
        relogio_interno_esperado = 1
        relogio_interno_obtido = self.server.vetor_relogios["id{}".format(self.id_no)]
        self.assertEqual(retorno_obtido, retorno_esperado)
        self.assertEqual(valor_obtido, valor_esperado)
        self.assertEqual(relogio_interno_obtido, relogio_interno_esperado)

    def teste_recebe_acao_leitura(self):
        acao = "read"
        retorno_esperado = "0"
        retorno_obtido = self.server.recebe_acao(acao)
        valor_esperado = 0
        valor_obtido = self.server.valor_interno
        relogio_interno_esperado = 1
        relogio_interno_obtido = self.server.vetor_relogios["id{}".format(self.id_no)]
        self.assertEqual(retorno_obtido, retorno_esperado)
        self.assertEqual(valor_obtido, valor_esperado)
        self.assertEqual(relogio_interno_obtido, relogio_interno_esperado)

    def teste_recebe_acao_incorreta(self):
        acao = "erro"
        retorno_esperado = "nok"
        retorno_obtido = self.server.recebe_acao(acao)
        valor_esperado = 0
        valor_obtido = self.server.valor_interno
        relogio_interno_esperado = 1
        relogio_interno_obtido = self.server.vetor_relogios["id{}".format(self.id_no)]
        self.assertEqual(retorno_obtido, retorno_esperado)
        self.assertEqual(valor_obtido, valor_esperado)
        self.assertEqual(relogio_interno_obtido, relogio_interno_esperado)


if __name__ == '__main__':
    unittest.main()
