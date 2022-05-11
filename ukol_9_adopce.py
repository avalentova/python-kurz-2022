import pandas

# načtení souboru
soubor = pandas.read_csv("adopce-zvirat.txt", sep = ";")
print(soubor)

#  informace o tabulce
print(soubor.info())

# záznam index 34
print(soubor.iloc[34, [1,2]])
