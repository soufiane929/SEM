class Spielbrett:
    def __init__(self):
        # Initialisieren des Spielfeldes
        self.spielfeld = {}
        self.Spalten = 7
        self.Zeilen = 6
        self.Zellen = self.Spalten * self.Zeilen
        # Alle Richtungen (8) für möglichen Gewinn
        # Im Modell: Zeilen (0-5), Spalten (0-6)
        # (-1,-1) = Eine Spalte nach links und eine Zeile hinauf
        self.Richtungen = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    # Funktion zur Feststellung der tiefsten Zeile einer Spalte
    def tiefste_zeile(self, spalte):
        for zeile in reversed(range(self.Zeilen)):
            # Überprüft, ob Feld frei ist
            if (spalte, zeile) not in self.spielfeld:
                return zeile

    # Überprüfen, ob noch Platz in der Spalte ist
    def gültigkeit(self, spalte):
        if spalte == 0 in self.spielfeld:
            return False
        if 0 <= spalte <= 7:
            return True

    # Spielfeld ausgeben
    def ausgabe_spielfeld(self):
        for zelle in range(self.Zellen):
            # Überprüfung, ob es sich um ein Zeilenende handelt
            if zelle % self.Spalten == 0:
                print()
            # Zellen modulo Spalten -> Rest = Zeilen
            position = (zelle % self.Spalten, zelle // self.Spalten)
            if position in self.spielfeld:
                # Ausgabe der Position am Spielfeld mit Leerzeichen danach
                print(self.spielfeld[position], end=" ")
            else:
                print(".", end=" ")

    # Überprüfen, ob ein Spieler gewonnen hat
    def gewinner(self, spieler):
        stein = "O" if spieler else "X"
        for position in self.spielfeld:
            for richtung in self.Richtungen:
                vier_in_einer_reihe = True
                # Überprüfen, ob 4 Steine liegen
                for i in range(4):
                    spalte, zeile = position
                    delta_spalte, delta_zeile = richtung
                    p1 = (spalte + delta_spalte * i, zeile + delta_zeile * i)
                    if p1 in self.spielfeld and self.spielfeld[p1] == stein:
                        continue  # Mach einfach weiter
                    vier_in_einer_reihe = False
                    break
                if vier_in_einer_reihe:
                    return True


class Spiel:
    def __init__(self):
        self.spielbrett = Spielbrett()
        # True = Spieler O, False = Spieler X
        self.spieler = True

    def spielen(self):
        while True:
            self.spielbrett.ausgabe_spielfeld()
            while True:
                try:
                    # Spieler gibt eine Spalte ein
                    spalte = int(input("Spalte(0-6): "))
                    if self.spielbrett.gültigkeit(spalte):
                        break
                    else:
                        print("Ungültige Eingabe, bitte erneut versuchen.")
                except ValueError:
                    print("Bitte eine gültige Zahl eingeben.")

            # Stein in der tiefsten Zeile platzieren
            zeile = self.spielbrett.tiefste_zeile(spalte)
            self.spielbrett.spielfeld[(spalte, zeile)] = "O" if self.spieler else "X"

            # Prüfen, ob ein Spieler gewonnen hat
            if self.spielbrett.gewinner(self.spieler):
                self.spielbrett.ausgabe_spielfeld()
                print(f"Spieler {'O' if self.spieler else 'X'} hat gewonnen!")
                break

            # Wechseln der Spieler bei Schleifendurchlauf
            self.spieler = not self.spieler


if __name__ == "__main__":
    spiel = Spiel()
    spiel.spielen()
