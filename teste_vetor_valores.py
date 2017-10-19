from unittest import TestCase, main

import vetor_valores


class TesteVetorValores(TestCase):
    def teste_obter_vetor_valores(self):
        id_servidor = 2
        num_servidores = 4
        valor_esperado = ["-", 0, "-", "-"]
        valor_obtido = vetor_valores.obter_vetor_valores(num_servidores, id_servidor)
        self.assertEqual(valor_esperado, valor_obtido)


if __name__ == '__main__':
    main()
