class Spielbrett:
    REIHEN = 6
    SPALTEN = 7

    def __init__(self):
        self.brett = [[' ' for _ in range(self.SPALTEN)] for _ in range(self.REIHEN)]

    def anzeigen(self):
        for reihe in self.brett:
            print('|'.join(reihe))
            print('-' * (self.SPALTEN * 2 - 1))

    def stein_einwerfen(self, spalte, stein):
        for reihe in reversed(self.brett):
            if reihe[spalte] == ' ':
                reihe[spalte] = stein
                return True
        return False

    def ist_voll(self):
        return all(all(zelle != ' ' for zelle in reihe) for reihe in self.brett)

    def gewinner_pruefen(self, stein):
        for reihe in range(self.REIHEN):
            for spalte in range(self.SPALTEN - 3):
                if all(self.brett[reihe][spalte + i] == stein for i in range(4)):
                    return True

        for reihe in range(self.REIHEN - 3):
            for spalte in range(self.SPALTEN):
                if all(self.brett[reihe + i][spalte] == stein for i in range(4)):
                    return True

        for reihe in range(self.REIHEN - 3):
            for spalte in range(self.SPALTEN - 3):
                if all(self.brett[reihe + i][spalte + i] == stein for i in range(4)):
                    return True

        for reihe in range(3, self.REIHEN):
            for spalte in range(self.SPALTEN - 3):
                if all(self.brett[reihe - i][spalte + i] == stein for i in range(4)):
                    return True

        return False