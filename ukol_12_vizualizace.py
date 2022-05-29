# 1. Histogram platů
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

import matplotlib.pyplot as plt
import pandas

platy = pandas.read_csv("platy_2021_02.csv")

df = platy["plat"]

df.hist(bins=[30000, 40000, 50000, 60000])
plt.show()

#2. Teplota ve městech

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(r.content)

teploty = pandas.read_csv("temperature.txt")
print(teploty)