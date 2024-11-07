import json

try:
    with open("people_data.json", "r", encoding="utf-8") as file:
        people = json.load(file)
except FileNotFoundError:
    people = []
    
while True:
    name = input("Ievadiet vardu: ")
    age = int(input("Ievadiet vecumu: "))
    city = input("Ievadiet pilsetu: ")

    people.append({"name": name,
                "age": age,
                "city": city})
    another = input("Vai velaties pievienot vel vienu cilveku? (ja/ne)").strip().lower()
    if another !="ja":
        break

with open("people_data.json", "w", encoding="utf-8") as file:
    json.dump(people, file, indent=4)

print("Dati par cilvekiem ir veiksmigi saglabati json faila!")
 
for person in people:
    a = int(person["age"])
    if a >= 18:
        print(f"Vards: {person['name']}, Vecums: {person['age']},Pilseta: {person['city']}")