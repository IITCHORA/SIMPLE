import json

def get_password():
    try:
        with open("data.json") as file:
            return json.load(file)
    except:
        return {}
def write_password(data):
    web = input("ENTER THE WEBSITE NAME: ")
    if web in data:
        print("THE FOLLOWING WEB IS NOT AVAILABLE")
        return
    password = input("CREATE THE STRONG PASSWORD: ")
    data[web]= password
    with open("data.json", "w")as file:
        json.dump(data , file)
    print("SUCCESSFULLY ADDED ! ")

def save_password(data):
    with open("data.json", "w")as file:
        json.dump(data , file)
while True:
    data = get_password()
    print("\n\n(1) ADD PASSWORD")
    print("(2) VIEW PASSWORD")
    print("(3) UPDATE PASSWORD")
    print("(4) REMOVE SITE")
    print("(5) LIST ALL WEBSITE")
    print("(6) EXIT")
    try:
        choice = int(input("\n ENTER THE INDEX NUMBER FROM FOLLOWING POINTS: "))
    except :
        print("PLEASE SELECT FROM FOLLOWING POINTS")
        input("\npress for continue")
        continue
    match choice:
        case 6:
            print("THANKS FOR VISITING US!")
            break
        case 1:
            write_password(data)
            input("\npress for continue")
        case 2:
            web = input("ENTER THE WEB NAME: ")
            if web in data:
                print("THE PASSOWRD OF ", web, " IS " ,data[web] )
                input("\npress for continue")
            else:
                print("THE FOLLOWING SITE NOT EXIST")
            input("\npress for continue")
        case 3:
            web = input("ENTER THE WEBSITE NAME TO CHANGE PASSWORD: ")
            if web in data:
                password = input("CREATE A NEW PASSWORD: ")
                data[web] = password
                save_password(data)
                print("PASSWORD CHANGED SUCCESSFULLY")
                
            else:
                print("THE WEBSITE NAME " , web, "DOES NOT EXIST")
            input("\npress for continue")
        case 4:
            web = input("ENTER THE WEBSITE NAME TO REMOVE: ")
            if web in data:
                data.pop(web)
                save_password(data)
                print("REMOVED SUCCESSFULLY!")
            else:
                print("THE WEB NAMED", web, "IS NOT EXIST") 
            input("\npress for continue")
        case 5:
            print("THE WEBSITES CURRENTLY AVAILABLE IS: ")
            for x  in data:
                print(x)
            input("\npress for continue")
        