import csv

fields = ['Produkta nosaukums', 'Cena', 'Daudzums']

rows = [['Abols','0.5','10'],['Banans','0.3','15'],['Piens','1.2','7']]

with open('produkti.csv', mode = 'w', newline='', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

