import json
import datetime

vardnica = {}

def load_data():
    file = open('apmekletai.json', 'r', encoding="utf-8")
    data=json.load(file)
    file.close()
    global vardnica
    vardnica = data["dalibnieki"]
    print('Dati loaded')

def save_data():    
    data = {"dalibnieki":vardnica}
    file = open('apmekletai.json', 'w',  encoding="utf-8")
    json.dump(data, file, indent=4, ensure_ascii=False)

def info_print():
    for dalibnieki in vardnica:
        print("DALĪBNIEKS:")
        print("id: "+dalibnieki["id"])
        print(dalibnieki["vards"]+' tālr.'+dalibnieki["telefons"]+', '+dalibnieki["pilseta"])

def pievienot_dalibnieku():
    id = int(input("Apmeklētāja id:"))
    #if 12 == id:
    #    print("Dalibnieks jau ir registrets")
    #else:
    name = input("Apmeklētāja vārds:")
    telefons = input("Tālrunis:")
    pilseta = input("Pilsēta:")
    vardnicaw = {
        "id": id,
        "vards": name,
        "telefons": telefons,
        "pilseta": pilseta,
        "apmeklejums": []}
    while True:
        choise = input("Vai vēlaties registret apmeklejumu? (y/n)")
        if choise =="y":
            stundas = input("Cik stundas gribat apmeklet sporta zali?: ")
            sporta_veids = input("Ar kadu sporta veidu jus gribat nodarboties?: ")
            print("1 dvieļa noma maksā 0,50 eiro")
            dvieliz = input("Cik dvieļu gribat panemt: ")
            dvielu_id = input("Dvieļu id:")
            datums = str(datetime.datetime.now())
            dvielis = {
                "id":dvielu_id,
                "daudzums":dvieliz,
                "stundas":stundas,
                "datums":datums,
                "sporta_veids":sporta_veids
            }
            vardnicaw['apmeklejums'].append(dvielis)
        else:
            break
    vardnica.append(vardnicaw)

def main():
    load_data()
    while (True):
        response=input("(1) Pievienot dalibnieku (2) Izprente dalibnieku datus (3) Iziet un saglabat datus")
        if response=="1":
            pievienot_dalibnieku()
        elif response =="2":
            info_print()
        elif response =="3":
            save_data()
            print("byeeeeeeeeeeeee!")
            exit()
        else:
            print('Chose a number betwen 1 and 3')
            continue

main()