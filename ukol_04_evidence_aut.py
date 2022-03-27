class Auto():
    def __init__(self, registracni_znacka, znacka, typ_vozidla, pocet_km, stav=True):
        self.registracni_znacka = registracni_znacka
        self.znacka = znacka
        self.typ_vozidla = typ_vozidla
        self.pocet_km = pocet_km
        self.stav = stav

    def pujc_auto(self):
        if self.stav == True:
            self.stav = False
            print("Potvrzuji zapůjčení vozidla.")
        else:
            print("Vozidlo není k dispozici.")
        
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, značka vozidla: {self.znacka}, typ vozidla: {self.typ_vozidla}"

peugeot = Auto("4A2 3020","Peugeot","403 Cabrio",47534)
skoda = Auto("1P3 4747", "Škoda","Octavia",41253)

dotaz = input("V nabídce máme vozidlo Peugeot a Škoda. Kterou značku si přejete vypůjčit? ")

if dotaz == "Škoda":
     print(skoda.get_info())
     skoda.pujc_auto()
else:
    print(peugeot.get_info())
    peugeot.pujc_auto()

dotaz2 = input("Jaké další vozidlo si přejete vypůjčit? ")
if dotaz2 == "Škoda":
     print(skoda.get_info())
     skoda.pujc_auto()
else:
    print(peugeot.get_info())
    peugeot.pujc_auto()