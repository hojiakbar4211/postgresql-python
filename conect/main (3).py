import time

import psycopg2

# connect to db
con = psycopg2.connect(
    host="localhost",
    database="g4",
    user="postgres",
    password="adgjmptw",
    port=5432)
# cursor
cur = con.cursor()


def reg():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    age = input("Enter age: ")
    s_group = input("Which group you wanna join G1, G2, G3, G4 : ")
    cur.execute(f"""insert into school(name, number, age, s_group)
                                    values ('{str(name)}', '{str(phone)}', {age}, '{str(s_group)}');""")
    con.commit()
    time.sleep(2)
    print("\nYou have been registered successfully!!! \n")
    ask()


def group_list():
    choose = int(input("1. G1 \n2. G2 \n3. G3 \n4. G4 : "))
    symb = f'G{choose}'
    if choose == 1 or choose == 2 or choose == 3 or choose == 4:
        cur.execute(f"select * from school where s_group ='{symb}'")
        group_list = cur.fetchall()
        for gr in group_list:
            print("\nName : ", gr[1])
            print("Phone : ", gr[2])
            print("Age : ", gr[3])
            print("Group : ", gr[4])
            print()
    ask()


def settings():
    change = int(input("What you wanna change 1-> name, 2-> phone number, 3->group : "))
    if change == 1:
        namee = input("Enter your current name : ")
        changed_val = input("Enter new name: ")
        cur.execute(f"""UPDATE school SET name = '{changed_val}' WHERE name ='{namee}';""")
        time.sleep(1)
        print("\nName changed successfully!!! \n")

    if change == 2:
        numm = input("Enter your current phone number: ")
        changed_val = input("Enter new name: ")
        cur.execute(f"""UPDATE school SET number = '{changed_val}' WHERE name ='{numm}';""")
        time.sleep(1)
        print("\nPhone number changed successfully!!! \n")
    if change == 3:
        grr = input("Enter your current Group : ")
        changed_val = input("Enter new group: ")
        cur.execute(f"""UPDATE school SET s_group = '{changed_val}' WHERE s_group ='{grr}';""")
        time.sleep(1)
        print("\nGroup changed successfully!!! \n")
    ask()


def delete():
    delete_sm = input("Enter the name which you wanna delete : ")
    cur.execute(f"""delete from school where name='{delete_sm}'""")
    time.sleep(0.5)
    print("Success")


def ask():
    choice = int(input("1.Register\n"
                       "2.Group list\n"
                       "3.Settings\n"
                       "4.Delete\n"
                       "5.Exit : "))
    if choice == 1:
        reg()

    elif choice == 2:
        group_list()

    elif choice == 3:
        settings()

    elif choice == 4:
        delete()


if __name__ == '__main__':
    ask()
    con.close()
