dati = ["Pirmais ieraksts","Otrais ieraksts","Tresais ieraksts"]

with open("dati1.txt", "w", encoding="utf-8") as filea_objekts:
    for ieraksts in dati:
        filea_objekts.write(ieraksts + "\n")