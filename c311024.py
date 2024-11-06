import json

with open("people.json", "r", encoding="utf-8") as afile:
    fdata = json.load(afile)
    for sa in fdata:
        if sa["age"] > 30:
            print(sa["name"])
print(fdata)
