from vier_gewinnt import Spiel
from computer_spieler import ComputerSpieler

class SpielMitComputer(Spiel):
    def __init__(self):
        super().__init__()  # Ruft den normalen Spiel-Constructor auf
        self.computer = ComputerSpieler(self.spielbrett)  # Fügt den Computer hinzu

    def spielen(self):
        while True:
            self.spielbrett.ausgabe_spielfeld()

            if self.spieler:  # Menschlicher Spieler (O)
                while True:
                    try:
                        spalte = int(input("Spalte (0-6): "))
                        if self.spielbrett.gültigkeit(spalte):
                            break
                        else:
                            print("Ungültige Eingabe, bitte erneut versuchen.")
                    except ValueError:
                        print("Bitte eine gültige Zahl eingeben.")
            else:  # Computer (X)
                spalte = self.computer.waehle_spalte()
                print(f"Der Computer wählt Spalte {spalte}")

            # Stein in der tiefsten Zeile platzieren
            zeile = self.spielbrett.tiefste_zeile(spalte)
            self.spielbrett.spielfeld[(spalte, zeile)] = "O" if self.spieler else "X"

            # Prüfen, ob jemand gewonnen hat
            if self.spielbrett.gewinner(self.spieler):
                self.spielbrett.ausgabe_spielfeld()
                print(f"Spieler {'O' if self.spieler else 'X'} hat gewonnen!")
                return

            # Spieler wechseln
            self.spieler = not self.spieler

if __name__ == "__main__":
    spiel = SpielMitComputer()
    spiel.spielen()
