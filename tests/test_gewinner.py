import unittest
from vier_gewinnt import Spielbrett

class TestGewinner(unittest.TestCase):
    def setUp(self):
        self.spielbrett = Spielbrett()

    def test_gewinner_horizontal(self):
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 0)] = "O"
        self.spielbrett.spielfeld[(2, 0)] = "O"
        self.spielbrett.spielfeld[(3, 0)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))

    def test_gewinner_vertikal(self):
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(0, 1)] = "O"
        self.spielbrett.spielfeld[(0, 2)] = "O"
        self.spielbrett.spielfeld[(0, 3)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))

    def test_gewinner_diagonal(self):
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 1)] = "O"
        self.spielbrett.spielfeld[(2, 2)] = "O"
        self.spielbrett.spielfeld[(3, 3)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))

    def test_keine_gewinner(self):
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 0)] = "O"
        self.spielbrett.spielfeld[(2, 0)] = "O"
        self.spielbrett.spielfeld[(3, 1)] = "X"
        self.assertFalse(self.spielbrett.gewinner(spieler))

if __name__ == '__main__':
    unittest.main()