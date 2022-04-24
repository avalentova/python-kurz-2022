nazev_souboru = "auta.txt"

# načtení souboru
with open(nazev_souboru, encoding='utf-8') as vstup:
    ujete_km = vstup.readlines()

# převedení čárky na tečku
ujete_km = [auto.replace(",",".") for auto in ujete_km]

# rozdělení podle mezery na RZ a číslo
ujete_km = [auto.split() for auto in ujete_km]

# úprava ze stringu na desetinné číslo
ujete_km = [[auto[0], float(auto[1])] for auto in ujete_km]

# vytvoření pouze seznamu ujetých km
pocty_km = []
for auto in ujete_km:
    pocty_km.append(auto[1])

# sečtení pouze ujetých km
celkovy_pocet = sum(pocty_km)
print (celkovy_pocet)

# druhý způsob sečtení
soucet_km = sum([radek[1] for radek in ujete_km])
print(soucet_km)