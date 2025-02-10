import random


class ComputerSpieler:
    def __init__(self, spielbrett):
        """
        Erstellt einen Computergegner für Vier Gewinnt.

        Parameter:
        spielbrett : Spielbrett
            Das aktuelle Spielbrett, um gültige Züge zu prüfen.
        """
        self.spielbrett = spielbrett

    def waehle_spalte(self):
        """
        Wählt eine zufällige, gültige Spalte für den nächsten Zug.

        Return:
        int
            Eine gültige Spalte zwischen 0 und 6.
        """
        gueltige_spalten = [spalte for spalte in range(self.spielbrett.Spalten) if self.spielbrett.gültigkeit(spalte)]
        return random.choice(gueltige_spalten) if gueltige_spalten else None