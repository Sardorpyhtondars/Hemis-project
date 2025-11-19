import re
n=r"^[A-Za-zА-Яа-яЎўҚқҒғҲҳЁё\s]+$"
p=r"^\+998\d{9}$"
class Contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

Contact1=Contact("Alisher","+998888888888")
Contact2=Contact("Bobur","+998777777777")
Contact3=Contact("Savlat", "+998200000000")

base_c=[Contact1,Contact2,Contact3]

def view_contacts(s:list):
    count=0
    for item in s:
        count+=1
        print(f"{count}. {item.name} {item.phone}")
# view_contacts(base_c)
def add_contact(s:list):
    contact_name=input("Enter contact name:\n")
    if not re.match(n,contact_name):
        print("Invalid name format")
        return
    contact_phone=input("Enter contact phone:\n")
    if not re.match(p,contact_phone):
        print("Invalid phone format")
        return
    contact=Contact(contact_name, contact_phone)
    s.append(contact)
    view_contacts(s)
# add_contact(base_c)
def update_contact(s:list):
    view_contacts(s)
    number=input("Enter contact number of the person to update:\n")
    contact_=None
    for i in s:
        if i.phone==number:
            contact_=i
            break
    if contact_ is None:
        print("Contact not found")
        return
    change=input("What do you want to change?\n1.name\n2.phone number\n").strip()
    if change=="1":
        new_name=input("Enter new contact name:\n")
        if new_name in [c.name for c in s]:
            print("Contact name already exists")
            return
        if not re.match(n,new_name):
            print("Contact name must not contain symbols and numbers")
            return
        contact_.name=new_name
        print("Contact name updated")
        return
    elif change=="2":
        new_phone=input("Enter new contact phone:\n")
        if new_phone in [c.phone for c in s]:
            print("Contact phone number already exists")
            return
        if not re.match(p,new_phone):
            print("Contact phone number is incorrect")
            return
        contact_.phone=new_phone
        print("Contact phone updated")
        return
    else:
        print("Invalid input")
        return
# update_contact(base_c)
def delete_contact(s:list):
    view_contacts(s)
    number=input("Enter contact number of the person to delete:\n")
    if not re.match(p,number):
        print("Invalid phone number")
        return
    contact=None
    for i in s:
        if i.phone==number:
            contact=i
            break
    if contact is None:
        print("Contact not found")
        return
    s.remove(contact)
    print("Contact deleted")
    view_contacts(s)
# delete_contact(base_c)
def contact_manager():
    while True:
        kod=input(" 1. View all contacts\n 2. Add contact\n 3. Update contact\n 4. Delete contact\n 5. Exit\n").strip()
        if kod=="1":
            view_contacts(base_c)
        elif kod=="2":
            add_contact(base_c)
        elif kod=="3":
            update_contact(base_c)
        elif kod=="4":
            delete_contact(base_c)
        elif kod=="5":
            break
        else:
            print("Invalid input")
            continue
# contact_manager()

class Massage:
    def __init__(self,name,phone,massage):
        self.name=name
        self.phone=phone
        self.massage=massage

Massage1=Massage("Alisher","+998888888888", "Hi")
Massage2=Massage("Bobur","+99877777777", "How r u doing?")

base_m=[Massage1,Massage2]

def view_massages(s:list):
    count=0
    for item in s:
        count+=1
        print(f"{count}. {item.name}, {item.phone}, {item.massage}")
# view_massages(base_m)
def send_massage(contacts:list,massages:list):
    view_contacts(contacts)
    number=input("Enter contact number of the person to send:\n")
    if not re.match(p,number):
        print("Invalid phone number")
        return
    contact=None
    for i in contacts:
        if i.phone==number:
            contact=i
            break
    if contact is None:
        print("Contact not found")
        return
    text=input("Enter massage to send:\n")
    massage=Massage(contact.name,contact.phone,text)
    massages.append(massage)
    print("Massage sent successfully")
    view_massages(massages)
# send_massage(base_c, base_m)
def delete_massage(contacts:list,massages:list):
    view_massages(massages)
    number=input("Enter contact number of the person to delete:\n")
    if not re.match(p,number):
        print("Invalid phone number")
        return
    delete_massage=None
    for i in delete_massage:
        if i.phone==number:
            delete_massage =i
            break
    if delete_massage is None:
        print("You don't have any massage")
        return
    massages.remove(delete_massage)
    print("Massage deleted")
    view_massages(massages)
# delete_massage(base_c, base_m)
def massage_manager():
    while True:
        kod=input(" 1. View massages\n 2. Send massage\n 3. Delete massage\n 4. Exit\n").strip()
        if kod=="1":
            view_massages(base_m)
        elif kod=="2":
            send_massage(base_c,base_m)
        elif kod=="3":
            delete_massage(base_c, base_m)
        elif kod=="4":
            break
        else:
            print("Invalid input")
            return
# massage_manager()
def main():
    while True:
        kod=input(" 1. Contacts\n 2. Massages\n 3. Exit\n").strip()
        if kod=="1":
            contact_manager()
        elif kod=="2":
            massage_manager()
        elif kod=="3":
            break
        else:
            print("Invalid input")
            return
main()