from misc_functions import clear_screen,message
import json

#prints courier DB and asks for user selection then outputs selection
def select_courier():
    while True:
        clear_screen()
        try:
            title = r"SELECT COURIER""\n``````````````"
            couriers = open_courier_db()
            print(title)
            for courier in couriers:
                print(couriers.index(courier) + 1,":",courier.get("Courier Name"),": ",courier.get("Courier Number"))
            user_selection = int(input("Select Courier:"))
            if user_selection in range(1,len(couriers)+1):
                return couriers[user_selection-1]
            else:
                message("INVALID SELECTION",1.5)
                continue
        except Exception as error:
            message(f"ERROR:\n{error}",4)
            continue


#Loads courier db and outputs contents
def open_courier_db():
    with open("couriers.json","r") as couriers_db:
        input_data = couriers_db.read()
        output_data = json.loads(input_data)
        return(output_data)

#Takes input as an argument and overwrites db with input
def save_courier_db(input):
    with open("couriers.json","w") as courier_db:
        input_data = json.dumps(input)
        courier_db.write(input_data)


#prints courier from db then asks for user selection and confirmation 
#before deleting the courier form the db       
def delete_courier():
    title = r"DELETE COURIER""\n""``````````````"
    while True:
        couriers = open_courier_db()
        clear_screen()
        print(title)
        for courier in couriers:
            print(couriers.index(courier) + 1,":",courier)
        print("0:Back")
        try:
            user_selection = int(input("Select Courier:"))
            if user_selection == 0:
                break
            else:
                print(couriers[user_selection-1]," << Selected")
                confirmation = input(f"Delete {couriers[user_selection-1]}? Y or N: ")
                if confirmation.lower() == "n":
                    message("NO CHANGES MADE",1)
                    continue
                elif confirmation.lower() == "y":
                    deleting = couriers[user_selection-1]
                    couriers.pop(user_selection-1)
                    save_courier_db(couriers)
                    message(f"{deleting} DELETED",2)
                    continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",3) 


#prints courier and takes user selection and input then overwrites the db with new entry
def update_courier():
    title = r"EDIT COURIER""\n""````````````"
    while True:
        couriers = open_courier_db()
        clear_screen()
        print(title)
        for courier in couriers:
            print(couriers.index(courier) + 1,":",courier.get("Courier Name"),"/ ",courier.get("Courier Number"))
        print("0:Back")
        try:
            user_selection = int(input("Select Courier:"))
            if user_selection == 0:
                break
            else:
                print(couriers[user_selection-1].get("Courier Name")," << Selected")
                new_name = input("New Name: ")
                if new_name == "":
                    message("NO CHANGES MADE",1)
                    continue
                else:
                    while True:
                        change_num = input("Would You Like To Change Number Aswell?? y/n:")
                        if change_num.lower() == "n":
                            new_number = couriers[user_selection-1].get("Courier Number")
                            break 
                        elif change_num.lower() == "y":
                            new_number = input("New Number: ")
                            break
                        else:
                            message("INVALID SELECTION",1)
                            continue
                    couriers[user_selection-1]["Courier Name"] = new_name
                    couriers[user_selection-1]["Courier Number"] = new_number
                    save_courier_db(couriers)
                    message(r"UPDATED TO: "+f"{new_name}:{new_number}",2)
                    continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",3) 


#takes user input and saves data to courier db creating a new courier
def create_courier():
    while True:
        title = r"CREATE NEW COURIER""\n""``````````````````"
        clear_screen()
        print(title)
        new_courier = input("New Courier Name:")
        new_courier_number = input("Courier Number:")
        if new_courier == "":
            message("NO CHANGES MADE",1.5)
            break
        else:
            new_entry = {}
            new_entry.update({"Courier Name":new_courier})
            new_entry.update({"Courier Number":new_courier_number})
            couriers = open_courier_db()
            couriers.append(new_entry)
            save_courier_db(couriers)
            break


#Prints couriers and takes user selection to go back
def print_couriers():
    try:
        title = "COURIERS\n````````"
        couriers = open_courier_db()
        while True:
            clear_screen()
            print(title)
            for courier in couriers:
                print(couriers.index(courier) + 1,":",courier.get("Courier Name"),"/ ",courier.get("Courier Number"))
            print("0:Back")
            user_selection = input("Select Option:")
            if user_selection == "0":
                break
            else:
                message("INVALID SELECTION",1.5)
    except Exception as error:
        message("ERROR:\n"+error,4)