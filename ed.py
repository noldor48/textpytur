saraksts = ["Silka","Geroj","Tabul"]

file = open("edieni.txt", "w", encoding="utf-8")
for el in saraksts:
    file.write(el + "\n")
file.close()