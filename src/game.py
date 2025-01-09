from board import Spielbrett

class Spiel:
    def __init__(self):
        self.brett = Spielbrett()
        self.aktueller_spieler = 'X'

    def spieler_wechseln(self):
        self.aktueller_spieler = 'O' if self.aktueller_spieler == 'X' else 'X'

    def spielen(self):
        while True:
            self.brett.anzeigen()
            spalte = int(input(f"Spieler {self.aktueller_spieler}, wähle eine Spalte (0-6): "))
            if self.brett.stein_einwerfen(spalte, self.aktueller_spieler):
                if self.brett.gewinner_pruefen(self.aktueller_spieler):
                    self.brett.anzeigen()
                    print(f"Spieler {self.aktueller_spieler} gewinnt!")
                    break
                if self.brett.ist_voll():
                    self.brett.anzeigen()
                    print("Das Spiel endet unentschieden!")
                    break
                self.spieler_wechseln()
            else:
                print("Spalte ist voll. Versuche es erneut.")

if __name__ == '__main__':
    spiel = Spiel()
    spiel.spielen()