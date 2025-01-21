class Spielbrett:
    def __init__(self, zeilen=6, spalten=7):
        #Leeres Spielfeld initialisieren
        self.zeilen = zeilen
        self.spalten = spalten
        self.brett = [[0 for _ in range(spalten)] for _ in range(zeilen)]

