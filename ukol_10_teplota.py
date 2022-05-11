import pandas

# načtení souboru
teploty = pandas.read_csv("temperature.txt")

# prvních 5 řádků
print(teploty.head())

# měření provedená v Praze
Praha = teploty.loc[teploty["City"] == "Prague"]
print(Praha)

# měření, kde je teplota vyšší než 80 stupňů
teplota_80 = teploty[teploty["AvgTemperature"] > 80.0]
print(teplota_80)

# měření, kde je teplota vyšší než 60 stupňů a v Evropě
teplota_60 = teploty["AvgTemperature"] > 60.0
teplota_EU = teploty["Region"] == "Europe"
teplota_60_EU = teploty[teplota_60 & teplota_EU]
print(teplota_60_EU)

# extrémní hodnoty
max = teploty["AvgTemperature"] > 80.0
min = teploty["AvgTemperature"] < 20.0
extremni = teploty[max | min]
print(extremni)
