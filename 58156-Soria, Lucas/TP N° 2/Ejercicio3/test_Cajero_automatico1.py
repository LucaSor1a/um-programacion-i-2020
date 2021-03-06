import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Billete import Billete_de_1000


class Cajero_automatico_Test1(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()
        self.mil_pesos = Billete_de_1000("pesos", "$")
        self.lista = []
        for x in range(10):
            self.lista.append(self.mil_pesos)
        self.caj.agregar_dinero(self.lista)

    def test_a(self):
        contar = self.caj.contar_dinero()
        self.assertEqual(contar, "10 billetes de $1000, parcial $10000\n" +
                         "Total: $10000")

    @parameterized.expand([
        (5000, "5 billetes de $1000\n"),
        (12000, "Error. Quiero sacar mas dinero de lo que puedo"),
        (5520, "Error. El monto es incorrecto"),
    ])
    def test_b(self, monto, respuesta):
        extraer = self.caj.extraer_dinero(monto)
        self.assertEqual(extraer, respuesta)


if __name__ == '__main__':
    unittest.main()
