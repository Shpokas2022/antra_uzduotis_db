
from db_tables import Person, engine, Supply_action, Clothing, Status, Clothing_type
from sqlalchemy.orm import sessionmaker
from pprint import pprint

session =  sessionmaker(engine)()

def create_person(f_name, s_name, personal_id, phone, e_mail):
    person = Person(f_name=f_name, s_name=s_name, personal_id=personal_id, phone=phone, e_mail=e_mail)
    session.add(person)
    session.commit()
    return person

def read_persons():
    persons = session.query(Person).all()
    return persons

def create_clothing(name, size):
    clothing = Clothing(name=name, size=size)
    session.add(clothing)
    session.commit()
    return clothing

def read_clothings():
    clothings = session.query(Clothing).all()
    return clothings

# def create_status(name):
#     status = Status(name=name)
#     session.add(status)
#     session.commit()
#     return status

def read_statuses():
    statuses = session.query(Status).all()
    return statuses

# def create_type(name):
#     clothing_type = Clothing_type(name=name)
#     session.add(clothing_type)
#     session.commit()
#     return clothing_type

# def read_types():
#     clothing_types = session.query(Clothing_type).all()
#     return clothing_types

# def create_action():
#     supply_action = Supply_action()
#     session.add(supply_action)
#     session.commit()
#     return supply_action

# def read_types():
#     supply_actions = session.query(Supply_action).all()
#     return supply_actions

while True:
    pasirinkimas = int(input("1 - įvesti asmenį\n2 - įvesti drabužius\n3 - užsakyti drabužius\n4 - peržiūrėti asmenis\n5 - peržiūrėti drabužius\n6 - peržiūrėti kokie drabužiai paimti\n7 - išeiti iš programos"))
    if pasirinkimas == 1:
        f_name = input("Įveskite vardą: ")
        s_name = input("Įveskite pavardę: ")
        personal_id = int(input("Įveskite asmens kodą: "))
        telefonas = input("Įveskite telefona: ")
        e_mail = input("Įveskite elktroninį paštą: ")
        person = create_person(f_name, s_name, personal_id, telefonas, e_mail)

    if pasirinkimas == 2:
        name = input("Įveskite šalmas, striukė, kelnės arba batai: ")
        size = input("Įveskite dydį: ")
        clothing = create_clothing(name, size)
    #     session.add(bankas)
    #     session.commit()
    # if pasirinkimas == 3:
    #     iban = input("Įveskite sąskaitos numerį")
    #     balansas = 0
    #     vartotojai = session.query(Zmogus).all()
    #     for vartotojas in vartotojai:
    #         print(vartotojas)
    #     zmogus_id = int(input("Pasirinkite vartotojo ID: "))
    #     bankai = session.query(Bankas).all()
    #     for vienas in bankai:
    #         print(vienas)
    #     bank_id = int(input("Pasirinkite banko ID: "))
    #     saskaita = create_account(iban, balansas, zmogus_id)
    #     saskaita = Saskaita(numeris=numeris, balansas=balansas, asmuo_id=vartotojo_id, bankas_id=banko_id)
    #     session.add(saskaita)
    #     session.commit()
    if pasirinkimas == 4:
        vartotojai = read_persons()
        # for vartotojas in vartotojai:
        pprint(vartotojai)
    # if pasirinkimas == 7:
    #     bankai = read_bank()
    #     # for vienas in bankai:
    #     pprint(bankai)
    # if pasirinkimas == 8:
    #     saskaitos = read_account()
    #     # for viena in saskaitos:
    #     pprint(saskaitos)
    if pasirinkimas == 7:
        print("Programa baigta")
        break