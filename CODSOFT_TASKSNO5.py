contacts=[]
while True:
    print("\n1.Add contact 2.View contacts 3.Search contact 4.Delete contact 5.Exit")
    choice=input("choose:")
    if choice=="1":
        name=input("Name:")
        phone=input("Phone:")
        email=input("Email:")
        address=input("Address:")
        contact={"name":name,"phone":phone,"email":email,"address":address}
        contacts.append(contact)
        print("Contact added!")
    elif choice=="2":
        for c in contacts:
            print(c["name"],"-",c["phone"])
    elif choice=="3":
        search_name=input("enter name to search:")
        for c in contacts:
            if c["name"].lower()==search_name.lower():
                print(c)
    elif choice=="4":
        del_name=input("enter name to delete:")
        for c in contacts:
            if c["name"].lower()==del_name.lower():
                contacts.remove(c)
                print("Deleted!")
                break
    elif choice=="5":
        break
