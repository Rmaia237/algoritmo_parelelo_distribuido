from unittest import TestCase, main

import vetor_valores


class TesteVetorValores(TestCase):
    def teste_obter_vetor_valores(self):
        id_servidor = 2
        num_servidores = 4
        valor_esperado = ["-", 0, "-", "-"]
        valor_obtido = vetor_valores.obter_vetor_valores(num_servidores, id_servidor)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_atualiza_faltando_valor(self):
        vetor_original = [1, 2, "-", 4]
        novo_vetor = ["-", 3, 4, "-"]
        valor_esperado = [1, 3, 4, 4]
        valor_obtido = vetor_valores.atualiza(vetor_original, novo_vetor)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_atualiza_com_todos_os_valores(self):
        vetor_original = [1, 2, "-", 4]
        novo_vetor = [5, 3, 4, 2]
        valor_esperado = [5, 3, 4, 2]
        valor_obtido = vetor_valores.atualiza(vetor_original, novo_vetor)
        self.assertEqual(valor_esperado, valor_obtido)


if __name__ == '__main__':
    main()
