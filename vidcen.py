import json

kop = 0
vid = 0
skaits = 0
with open("produkti.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for sa in data:
        kop += sa["price"]
        skaits += 1
vid = kop/skaits
print(vid)
print(data)