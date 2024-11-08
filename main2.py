import json


organizations=[]
#print(organisations)

def load_data():
    file = open('organizations.json', 'r')
    data=json.load(file)
    file.close()
    global organizations
    organizations = data['organizations']
    print('Dati load')


def add_organization():
    organization_name=input("Organisation name: ")
    organization_adress=input("Organisation adress ")
    organization_id=input("Organisation id ")

    organization={
        "name": organization_name,
        "adress": organization_adress,
        "id": organization_id,
        "contacts":[]
    }

    while True:
        response=input("Do you want to add a contact(y/n)")
        if response=='y':
            contact_name=input("Contact name: ")
            contact_position=input("Contact position: ")
            contact_id=input("Contact id: ")

            contact={
                'name':contact_name,
                'position':contact_position,
                'id':contact_id,
            }

            organization['contacts'].append(contact)

        elif response=='n':
            break
    organizations.append(organization)

def print_organization():
    for organization in organizations:
        print('---ORGANISATION---')
        print(f"{organization['name']}({organization['id']})")
        print(f"Adrese:{organization['adress']}")
        print(f"Kontaktu skaits: {len(organization['contacts'])}")

def save_data():    
    data = {'organizations':organizations}
    file = open('organizations.json', 'w')
    json.dump(data, file, indent=4)



def find_organization_by_id():
    organization_id = input("Ievadiet organizacijas id: ")
    for organization in organizations:
        if organization['id']==organization_id:
            print('---ORGANISATION---')
            print(f"{organization['name']}({organization['id']})")
            break

def count_organizations():
    print(len(organizations))
def main():
    count_organizations()
    #load_data()
    while (True):
        response=input("(1) Add organisation (2) Print organisations (3) Exit ")
        if response=="1":
            add_organization()
        elif response =="2":
            print_organization()
        elif response =="3":
            save_data()
            print("byeeeeeeeeeeeee!")
            exit() 
        else:
            print('Chose a number betwen 1 and 3')
            continue

main()