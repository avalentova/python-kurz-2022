import re

nazev_souboru = "posta.html"

#načtení souboru, místo read() mám readlines
with open(nazev_souboru, encoding='utf-8') as vstup:
    posta = vstup.readlines()

#odstranění znaků pro řádky
posta = [radek.replace("\n"," ") for radek in posta]
#nahrazení více mezer jen jednou
posta = [re.sub('\s{1,}',' ', radek) for radek in posta]
#vytvořím string pro re.findall
posta = "".join(posta)

#hledám spojení PSČ a města
psc_posta = re.findall("\d{3} \d{2} \s*\w*\s*\w*\s*\w*", posta)
print(psc_posta)

