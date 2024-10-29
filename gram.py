'''gramname = input("Ievadiet gramatas nosaukumu:")
autor = input("Ievadiet autoru:")
izdotdat = input("Ievadiet izdosanas gadu:")
saraksts = [gramname,autor,izdotdat]
file = open("gramatas.txt", "w", encoding="utf-8")
for el in saraksts:
    file.write(el + "\n")
file.close()'''

with open("gramatas.txt","a",encoding="utf-8") as fail:
    while True:
        jautajums=input('Vai vēlāties ierakstīt vēl vienu grāmatu? (jā / nē) ')
        if jautajums=="jā":
            gramata=input("Ievadi GRAMATU: ") 
            autors=input("Īevadiet AUTORU: ")
            gads_izdosanas=input("Ievadiet IZDOSANAS GADU: ")
            fail.write(f"\nGrāmatas nosaukums: {gramata}\nAutors: {autors}\nIzdošanas gads {gads_izdosanas}")
        else:
            print('Paldies!')
            break 