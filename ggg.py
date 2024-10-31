import csv

skaits = 0
with open('studenti.csv', mode = 'r', encoding="utf-8") as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        if int(row['Vecums']) > 20:
            skaits += 1

print(skaits)
