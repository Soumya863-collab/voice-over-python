Contacts=[]
profiles={}
contact={}

def AddContact(Contacts,contact):
    print("Add Contact details as you want")
    print("-----------")
    print("Enter The Contact")
    name=input("Enter the Contact Name : ")
    phone=input("Enter the Phone number : ")
    email=input("Enter the Email id : ")
    if(len(name)<4 or len(phone)!=10 or "@gmail.com" not in email):
        print("Enter valid credentials")
        return
    contact={"name":name,"phone":phone,"email":email}
    profiles={"profile":contact}
    Contacts.append(profiles)
    print("Task Completed")
    print("--------------")

def ListOfContacts(Contacts):
    print("List of Contacts")
    print("----------------")
    print(Contacts)
    print("--------------")

def UpdateContact(Contacts,profiles):
    print("Update Contact")
    print("--------------")
    print("Do you want to edit the Name or PhoneNumber or email id")
    print("These are the Contacts,Which Contact you want to delete")
    ListOfContacts(Contacts)
    print("Select which profile you want to delete")
    select=int(input("Enter profile index"))
    print("Enter 1 to edit ContactName")
    print("Enter 2 to edit PhoneNumber")
    print("Enter 3 to edit email id")
    ch=int(input("Enter your choice:"))
    match ch:
        case 1:
            name=input("Enter the new name : ")
            Contacts[select]['profile']['name']=name
        case 2:
            phone=input("Enter the new phonenumber : ")
            Contacts[select]['profile']['phone']=phone
        case 3:
            email=input("Enter the new email id")
            Contacts[select]['profile']['email']=email
    print(Contacts)
    print("--------------")

def DeleteContact():
    print("Delete Contact")
    print("--------------")
    index=int(input("Enter index of the profile you want to delete"))
    del Contacts[index]
    print(Contacts)

def ExitFunction():
    print("Exit")
    exit()

def Welcome():
    print("Welcome")
    print("Here's the features you can use")
    print("Enter 1 for Add Contact to the system")
    print("Enter 2 for List of Contacts")
    print("Enter 3 for Update details")
    print("Enter 4 for Delete the Contact")
    print("Enter 5 for Exit")
    while(1):
        ch=int(input("Enter your choice : "))
        match ch:
            case 1:
                AddContact(Contacts,contact)
            case 2:
                ListOfContacts(Contacts)
            case 3:
                UpdateContact(Contacts,profiles)
            case 4:
                DeleteContact()
            case 5:
                ExitFunction()
            case _:
                print("Invalid Choice");exit()
Welcome()
