import json

def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
        print("DATA ENTERED SUCCESSFULLY! ")
def show_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except (json.JSONDecodeError , FileNotFoundError):
        return []
    
def nothing():
    input("PRESS FOR CONTINUE: ")
def not_found_error(name):
    print("THERE NO STUDENT WITH NAME", name)
    print("PLEASE TRY AGAIN!")
while True:
        temp_data = {}
        data = show_data()

        print("\n\n1 . ADD STUDENT")
        print("2 . UPDATE STUDENT")
        print("3 . VIEW STUDENT MARK")
        print("4 . REMOVE STUDENT")
        print("5 . EXIT")

        try:
            choice = int(input("ENTER (1 - 5): "))
        except ValueError:
            print("YOU HAVE ENTER WRONG NUMBER , PLEASE THE CHOOSE THE FIELD BY NUMBER CORRECTLY")
            nothing()
            continue
        
        match choice:
            case 1:
                try:
                    temp_data["name"] = input("ENTER THE NAME OF STUDENT TO ADD: ")
                    temp_data["marks"] = float(input("ENTER THE PERCENTAGE OF  STUDENT: "))
                    if temp_data["marks"] >100 or temp_data["marks"] <0:
                        print("INVALID PERCENTAGE")
                        nothing()
                        continue
                    data.append(temp_data)
                    write_data(data)
                    nothing()
                except (TypeError, ValueError):
                    print("TRY AGAIN!")
                    continue
            case 4:
                name = input("ENTER THE NAME OF STUDENT TO REMOVE IT: ")
                for x in data:
                    get = False
                    if name == x["name"]:
                        data.remove(x)
                        get = True
                        print("DATA HAS REMOVED SUCCESSFULLY")
                        write_data(data)
                        nothing()
                        break
                if not get:
                    not_found_error(name)
                
                
            case 3:
                name = input("ENTER THE NAME OF STUDENT: ")
                for x in data:
                    get = False
                    if name == x["name"]:
                        print("STUDENT NAME: ", name)
                        print("MARKS: ", x["marks"])
                        nothing()
                        break
                if not get:
                    not_found_error(name)
            case 2: 
                name =input("ENTER THE STUDENT NAME TO UPDATE IT MARKS: ")
                for x in data:
                    get = False
                    if name == x["name"]:
                        mark = float(input("THE MARKS WILL GOING TO CHANGE: "))
                        x["marks"] = mark
                        get = True
                        print("STUDENT NAME: ", name)
                        print("MARKS: ", x["marks"])
                        write_data(data)
                        nothing()
                        break
                if not get:
                    not_found_error(name)
            case 5:
                print("THANKS FOR VISITING US!")
                break 