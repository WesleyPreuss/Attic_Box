import json
import os
import time
def message(msg_txt,msg_length):
    os.system("cls")
    print(msg_txt)
    time.sleep(msg_length)

def select_courier():
    try:
        title = r"SELECT COURIER""\n``````````````"
        couriers = open_courier_db()
        print(title)
        for courier in couriers:
            print(couriers.index(courier) + 1,":",courier)
        while True:
            user_selection = int(input("Select Courier:"))
            if user_selection in range(1,len(couriers)):
                return couriers[user_selection-1]
            else:
                message("INVALID SELECTION",1.5)
                continue
    except Exception as error:
        message(f"ERROR:\n{error}",4)

def open_courier_db():
    with open("mini_project_folder\couriers.json","r") as couriers_db:
        input_data = couriers_db.read()
        output_data = json.loads(input_data)
        return(output_data)

output = select_courier()
print(output)