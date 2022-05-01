# import modulu
from datetime import datetime

# základní parametry
vyssi_vstupne = 250
nizsi_vstupne = 180

prvni_den = datetime(2021, 7, 1)
posledni_drazsi_den = datetime(2021, 8, 10)
posledni_den = datetime(2021, 8, 31)

datum = input("Na které datum si přeješ zakoupit vstupenky? ")
zadane_datum = datetime.strptime(datum, "%d. %m. %Y")

if zadane_datum < prvni_den:
    print("Je nám líto, letní kino je v uvedený den uzavřeno.")
elif zadane_datum > posledni_den:
    print("Je nám líto, letní kino je v uvedený den uzavřeno.")
else:
    osoby = int(input("Kolik vstupenek chceš koupit? "))
    if zadane_datum <= posledni_drazsi_den:
        celkova_cena = osoby * vyssi_vstupne
    else:
        celkova_cena = osoby * nizsi_vstupne
    print (f"Celková cena vstupného je {celkova_cena}Kč. Děkuji za nákup!")