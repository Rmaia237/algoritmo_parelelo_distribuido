from unittest import TestCase, main

import relogio_vetorial


class TesteRelogioVetorial(TestCase):
    def teste_obter_relogio_vetorial(self):
        num_servidores = 4
        valor_esperado = [0, 0, 0, 0]
        valor_obtido = relogio_vetorial.obter_relogio_vetorial(num_servidores)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_incrementar(self):
        relogio_zerado = [0, 0, 0, 0]
        indice = 2
        valor_esperado = [0, 1, 0, 0]
        valor_obtido = relogio_vetorial.incrementar(relogio_zerado, indice)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_atualizar(self):
        relogio_local = [4, 3, 2, 1]
        relogio_recebido = [1, 2, 3, 4]
        valor_esperado = [4, 3, 3, 4]
        valor_obtido = relogio_vetorial.atualizar(relogio_local, relogio_recebido)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_eh_anterior_com_um_relogio_menor(self):
        relogio_a = [1, 2, 3, 4]
        relogio_b = [2, 2, 3, 4]
        valor_esperado = True
        valor_obtido = relogio_vetorial.eh_anterior(relogio_a, relogio_b)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_eh_anterior_com_um_relogio_menor_e_outro_maior(self):
        relogio_a = [3, 2, 1, 4]
        relogio_b = [2, 2, 3, 4]
        valor_esperado = True
        valor_obtido = relogio_vetorial.eh_anterior(relogio_a, relogio_b)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_eh_anterior_com_dois_relogios_menores(self):
        relogio_a = [5, 2, 2, 2]
        relogio_b = [5, 2, 3, 4]
        valor_esperado = True
        valor_obtido = relogio_vetorial.eh_anterior(relogio_a, relogio_b)
        self.assertEqual(valor_esperado, valor_obtido)

    def teste_eh_anterior_com_nenhum_relogio_menor(self):
        relogio_a = [1, 3, 3, 5]
        relogio_b = [1, 2, 3, 4]
        valor_esperado = False
        valor_obtido = relogio_vetorial.eh_anterior(relogio_a, relogio_b)
        self.assertEqual(valor_esperado, valor_obtido)

    # def teste_eh_concorrente_com_relogios_iguais(self):
    #     relogio_a = [1, 2, 3, 4]
    #     relogio_b = [1, 2, 3, 4]
    #     valor_esperado = True
    #     valor_obtido = relogio_vetorial.eh_concorrente(relogio_a, relogio_b)
    #     self.assertEqual(valor_esperado, valor_obtido)
    #
    # def teste_eh_concorrente_com_relogios_diferentes(self):
    #     relogio_a = [1, 2, 3, 4]
    #     relogio_b = [2, 1, 3, 4]
    #     valor_esperado = True
    #     valor_obtido = relogio_vetorial.eh_concorrente(relogio_a, relogio_b)
    #     self.assertEqual(valor_esperado, valor_obtido)


if __name__ == '__main__':
    main()
