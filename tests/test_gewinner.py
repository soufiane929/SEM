import unittest
from vier_gewinnt import Spielbrett

class TestGewinner(unittest.TestCase):
    def setUp(self):
        self.spielbrett = Spielbrett()

    def test_tiefste_zeile(self):
        print("Running test_tiefste_zeile...")
        self.assertEqual(self.spielbrett.tiefste_zeile(0), 5)
        self.spielbrett.spielfeld[(0, 5)] = "O"
        self.assertEqual(self.spielbrett.tiefste_zeile(0), 4)
        self.spielbrett.spielfeld[(0, 4)] = "X"
        self.assertEqual(self.spielbrett.tiefste_zeile(0), 3)
        print("test_tiefste_zeile passed.")

    def test_gültigkeit(self):
        print("Running test_gültigkeit...")
        self.assertTrue(self.spielbrett.gültigkeit(0))
        self.assertTrue(self.spielbrett.gültigkeit(6))
        self.assertIsNone(self.spielbrett.gültigkeit(-1))
        self.assertTrue(self.spielbrett.gültigkeit(7))
        for zeile in range(6):
            self.spielbrett.spielfeld[(0, zeile)] = "O"
        self.assertTrue(self.spielbrett.gültigkeit(0))
        print("test_gültigkeit passed.")

    def test_gewinner_horizontal(self):
        print("Running test_gewinner_horizontal...")
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 0)] = "O"
        self.spielbrett.spielfeld[(2, 0)] = "O"
        self.spielbrett.spielfeld[(3, 0)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))
        print("test_gewinner_horizontal passed.")

    def test_gewinner_vertikal(self):
        print("Running test_gewinner_vertikal...")
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(0, 1)] = "O"
        self.spielbrett.spielfeld[(0, 2)] = "O"
        self.spielbrett.spielfeld[(0, 3)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))
        print("test_gewinner_vertikal passed.")

    def test_gewinner_diagonal(self):
        print("Running test_gewinner_diagonal...")
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 1)] = "O"
        self.spielbrett.spielfeld[(2, 2)] = "O"
        self.spielbrett.spielfeld[(3, 3)] = "O"
        self.assertTrue(self.spielbrett.gewinner(spieler))
        print("test_gewinner_diagonal passed.")

    def test_keine_gewinner(self):
        print("Running test_keine_gewinner...")
        spieler = True
        self.spielbrett.spielfeld[(0, 0)] = "O"
        self.spielbrett.spielfeld[(1, 0)] = "O"
        self.spielbrett.spielfeld[(2, 0)] = "O"
        self.spielbrett.spielfeld[(3, 1)] = "X"
        self.assertFalse(self.spielbrett.gewinner(spieler))
        print("test_keine_gewinner passed.")

if __name__ == "__main__":
    unittest.main()
