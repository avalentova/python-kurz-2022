baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod = input("Zadej kód balíku: ")

status = baliky.get(kod)

if status == True:
    print ("Balík byl předán kurýrovi"),
else:
    print ("Balík zatím nebyl předán kurýrovi")