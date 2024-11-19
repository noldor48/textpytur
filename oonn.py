import csv

titles=[]
year=[]
with open("./spotify2.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    for i in reader:
        titles.append(i[0])
        if i[3] not in year:
            year.append(i[3])
    print(titles[1::])
    print(list(set(year[1::])))
