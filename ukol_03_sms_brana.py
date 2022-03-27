# telefonni_cislo = input("Zadej telefonní číslo příjemce: ")

# def delka(telefonni_cislo):
#     if len(telefonni_cislo) == 9 or len(telefonni_cislo) == 13:
#         return True
#     else:
#         return False

# if delka(telefonni_cislo) == True:
#     text = input ("Zadej text zprávy: ")
#     def cena(text):
#         if len(text)//180 < 1:
#             return 1 * 3
#         else:
#             return (len(text)//180 + 1) * 3
#     print(f"Výsledná cena zprávy je {cena(text)} Kč")
# else:
#     print ("Neplatné telefonní číslo.")

# upravena verze kodu
import math

def delka(telefonni_cislo):
    if len(telefonni_cislo) == 9 or len(telefonni_cislo) == 13:
        return True
    else:
        return False

def cena(text):
    vypocet = math.ceil(len(text)/180) * 3
    return vypocet

telefonni_cislo = input("Zadej telefonní číslo příjemce: ")

if delka(telefonni_cislo) == True:
    text = input ("Zadej text zprávy: ")
    print(f"Výsledná cena zprávy je {cena(text)} Kč")
else:
    print ("Neplatné telefonní číslo.")