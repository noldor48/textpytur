import csv
import json

skoleni=[]
with open("./gramats.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for line in reader:
        skoleni.append(line)

print(skoleni)

with open("./gramatas.json","w",encoding="utf-8") as json_file:
    json.dump(skoleni, json_file, indent=4)
for vards in skoleni:
    print(vards["vards"])

for vass in skoleni:
    print(vass["vards"],vass["maksa$"],"dolari")

money=0
for vass in skoleni:
    vanda = int(vass["maksa$"])
    money+=vanda

print("Kopeja maksa: ",money)