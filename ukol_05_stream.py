class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}."

class Film (Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_info(self):
        return super().get_info() + f" Film má délku {self.delka} minut."

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        return super().get_info() + f" Seriál má {self.pocet_epizod} epizod a délka jedné je {self.delka_epizody} minut."

objekt_film = Film("Smrt na Nilu","Krimi/Drama", 127)
objekt_serial = Serial("Hercule Poirot", "Krimi/Drama", 70, 60)


print(objekt_film.get_info())
print(objekt_serial.get_info())