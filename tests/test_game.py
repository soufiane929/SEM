import unittest
from src.board import Spielbrett

class TestSpielbrett(unittest.TestCase):
    def setUp(self):
        self.brett = Spielbrett()

    def test_stein_einwerfen(self):
        self.assertTrue(self.brett.stein_einwerfen(0, 'X'))
        self.assertEqual(self.brett.brett[-1][0], 'X')

    def test_gewinner_pruefung_horizontal(self):
        for i in range(4):
            self.brett.stein_einwerfen(i, 'X')
        self.assertTrue(self.brett.gewinner_pruefen('X'))

    def test_brett_voll(self):
        for spalte in range(Spielbrett.SPALTEN):
            for _ in range(Spielbrett.REIHEN):
                self.brett.stein_einwerfen(spalte, 'X' if spalte % 2 == 0 else 'O')
        self.assertTrue(self.brett.ist_voll())

if __name__ == '__main__':
    unittest.main()