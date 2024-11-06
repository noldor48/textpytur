import json

data ={"name":"Anna",
       "age":25,
       "city":"Riga"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r", encoding="utf-8") as afile:
    fdata = json.load(afile)
print(fdata)

