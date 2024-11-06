import csv

darbiniekuskaits = 0
videjaalga = 0
copalg =0
with open('darbinieki.csv', mode = 'r', newline='', encoding="utf-8") as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(row)
        alga = int(row['Alga'])
        copalg += alga
        algpecnod = alga * 0.77
        darbiniekuskaits += 1

videjaalga = copalg/darbiniekuskaits
print(videjaalga)

#with open('darbinieki.csv', mode = 'w', newline='', encoding="utf-8") as csvfile:
#    csvwriter = csv.writer(csvfile)
