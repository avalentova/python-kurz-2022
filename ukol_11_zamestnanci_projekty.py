# 1. Zaměstnanci

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

import pandas

praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")

# přidání sloupce s městem
praha['město'] = 'Praha'
plzen['město'] = 'Plzeň'
liberec['město'] = 'Liberec'

# spojení do jedné tabulky
zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)

# načtení platů a propojení
platy = pandas.read_csv("platy_2021_02.csv")
propojeni = pandas.merge(platy, zamestnanci)

# kontrola rozsahu
print(zamestnanci.shape)
print (propojeni.shape)

# výpočet průměrného platu
prumer = propojeni.groupby('město')['plat'].mean()
print(prumer)

# 2. Projekty
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(r.content)

projekty = pandas.read_csv("vykazy.csv")
print(projekty)

hodiny = projekty.groupby('project')['hours'].sum()
print(hodiny)



