#Initialisieren des Spielfeldes
spielfeld = {}
Spalten = 7
Zeilen = 6
Zellen = Spalten * Zeilen
#Alle Richtungen(8) für möglichen Gewinn:
#   Im Modell: Zeilen(0-5),Spalten(0-6)
#       (-1,-1) = Eine Spalte nach links und eine Zeile hinauf
Richtungen = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

#Funktion zur Feststellung der tiefsten Zeile einer Spalte
def tiefste_zeile(spalte):
    # Schleife von 5 bis 0 in Zeilen
    for zeile in reversed(range(Zeilen)):
        # Überprüft, ob Feld frei ist
        if (spalte, zeile) not in spielfeld:
            return zeile

#Überprüfen, ob noch Platz in der Spalte ist
def gültigkeit(spalte):
    if spalte == 0 in spielfeld:
        return False
    if 0 <= spalte <= 7:
        return True

def ausgabe_spielfeld():
    for zelle in range(Zellen):
        #Überprüfung ob es sich um ein Zeilenende haltet
        if zelle % Spalten == 0:
            print()
        #Zellen modulo Spalten -> Rest = Zeilen
        position = (zelle % Spalten, zelle // Spalten)
        if position in spielfeld:
            #Ausgabe der Position am Spielfeld mit Leerzeichen danach
            print(spielfeld[position], end = " ")
        else:
            print(".", end = " ")

def gewinner(spieler):
    #Welcher Spieler ist am Zug
    if spieler:
        stein = "O"
    else:
        stein = "X"
    for position in spielfeld:
        for richtung in Richtungen:
            vier_in_einer_reihe = True
            #Überprüfen, ob 4 Steine liegen
            for i in range(4):
                spalte, zeile = position
                delta_spalte, delta_zeile = richtung
                p1 = (spalte + delta_spalte * i, zeile + delta_zeile * i)
                if p1 in spielfeld and spielfeld[p1] == stein:
                    continue    #mach einfach weiter
                vier_in_einer_reihe = False
                break
            if vier_in_einer_reihe:
                return True


spieler = True
while True:
    ausgabe_spielfeld()
    while True:
        spalte = int(input("Spalte(0-6): "))
        if gültigkeit(spalte):
            break   #Ausbrechen
    zeile = tiefste_zeile(spalte)
    if spieler:
        spielfeld[(spalte, zeile)] = "O"
    else:
        spielfeld[(spalte, zeile)] = "X"

    if gewinner(spieler):
        print(spielfeld)
        print("Gewonnen")
        break

    #Wechseln der Spieler bei Schleifendurchlauf
    spieler = not spieler