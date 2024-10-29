numwords = 0
with open('File.txt','r', encoding="utf-8") as file:
    data = file.read()
    lines = data.split()
print(len(lines))
print(len(set(lines)))

rindas = ["Pirma rinda.","Otra rinda","Tresa rinda"]

for index, rinda in enumerate(rindas, start=1):
    print(f"{index}:{rinda}")

noraditais_burts = "k"

with open("File.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
saturs = saturs.lower()
vardi = saturs.split()
print(vardi)
sarakst = []
for el in vardi:
    if el[0] == noraditais_burts:
        sarakst.append(el)
print(sarakst)
print(len(sarakst))