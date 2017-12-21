contact_data = []

sheryl = []+["Sheryl Beryl"]+["027543771"]
contact_data.append(sheryl)

def addContact():
    while True:
        print("Please enter their information.")
        nam = input("please input their name:")
        phone = input("please input their phone number:")
        contact = []+[nam]+[phone]
        contact_data.append(contact)
        ans = input("would you like to add another contact? ('y' or 'n')")
        if ans == "n":
            ans1 = input("Would you like to do something else? ('y' or 'n')")
            if ans1 == "y":
                start()
                break
            if ans1 == "n":
                break
        if ans == "y":
            continue 

def search():
    nam = input("Enter the name you want to search for")

    for x in contact_data:
        for contact in x:
            if contact == nam:
                print(contact)
                print(x)

def getAll():
    for x in contact_data:
        for y in x:
            print(y)

    while True:
        choice = input("Would you like to do something else? ('y' or 'n'")
        if choice == "y":
            start()
            break
        if choice == "n":
            break
        else: 
            print ("Please enter a valid command")
            continue 

def start():
    print ("If you want to make a new contact type 'New'")
    print ("If you want to see all contacts type 'All'")
    print ("If you want to search for a contact type 'Search'")

    while True:
        choice = input()
        if choice == "New" or "new":
            addContact()
            break
        if choice == "All" or "all":
            getAll()
            break
        if choice == "Search" or "search":
            search()
            break
        else: 
            print ("Please enter a valid command")
            continue 

print ("Welcome to Contact List 1.0")
start()