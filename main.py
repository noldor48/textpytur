with open("dati.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
print(saturs)

with open("dati.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()
    print(rindas)

for rinda in rindas:
    print(rinda.strip())
