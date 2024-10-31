import csv

'''with open('fcvbsv.csv', mode = 'r', encoding="utf-8") as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)'''

fields = ['Nr', 'Name', 'Year']

rows = [['1','Tic','32'],['2','Sandy','20'],['3','Ash','23']]

with open('student.csv', mode = 'w', newline='', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)