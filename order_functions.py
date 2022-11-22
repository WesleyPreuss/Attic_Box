from misc_functions import clear_screen,message
import json
from courier_functions import select_courier
from product_functions import select_items


#This function loads the orders JSON and returns the contents
def compile_orders():
    with open("orders.json","r") as orders_db:
        input_data = orders_db.read()
        output_data = json.loads(input_data)
        return(output_data)


#Iterates through the data and prints it in a more appealing format 
def print_orders():
    clear_screen()
    print("ORDERS LOG\n``````````")
    orders = compile_orders()
    if orders == []:
        print("[NO ORDERS]")
    else:
        pass
    for order in orders:
        print(orders.index(order) + 1,":")
        for key in order:
            if isinstance(order.get(key),dict):
                for subkey in order.get(key):
                    print(subkey,": ",orders[orders.index(order)][key][subkey])
                    continue
            elif isinstance(order.get(key),list):
                print(key,":")
                for item in order.get(key):
                    print(item.get("Product"),"£","{:.2f}".format(item.get("Price")))
                    continue
            else:
                print(key,":",order.get(key))
                continue
        print("\n")
    while True:
        user_selection = input("0 To Return:")
        if user_selection == "0":
            break
        else:
            print("INVALID SELECTION")
            continue



#takes user input and creates a new order then saves to DB
def create_order():
    while True:
        clear_screen()
        print(r"CREATE NEW ORDER""\n````````````````")
        try:
            cx_name = input("Customer Name:")
            cx_adress = input("Customer Adress:")
            cx_phone = input("Customer Phone:")
            courier = select_courier()
            new_order = select_items()
            status = "Preparing"
            new_order_dict = {"Customer Name":cx_name,"Customer Adress":cx_adress,
            "Customer Phone":cx_phone,"Courier":courier,"Order":new_order[0],"Order Total":new_order[1],"Order Status":status}
            order_db = compile_orders()
            order_db.append(new_order_dict)
            save_orders(order_db)
            message("NEW ORDER CREATED",1.5)
            break
        except ValueError:
            new_db = []
            new_db.append(new_order_dict)
            save_orders(new_db)
            message("No Orders Found New File Created",2)
        except Exception as error_message:
            message(f"ERROR:{error_message}",5)
            continue  


#takes input as an argument then overwrites DB with input
def save_orders(input):
        with open("orders.json","w") as orders_db:
            input_data = json.dumps(input)
            orders_db.write(input_data)


#prints orders takes user selection then asks for confirmation before deleting and saving to db
def delete_orders():
    while True:
        clear_screen()
        orders = compile_orders()
        for order in orders:
            print(orders.index(order) + 1,":")
            for key in order:
                if isinstance(order.get(key),dict):
                    for subkey in order.get(key):
                        print(subkey,": ",orders[orders.index(order)][key][subkey])
                        continue
                elif isinstance(order.get(key),list):
                    print(key,":")
                    for item in order.get(key):
                        print(item.get("Product"),item.get("Price"))
                        continue
                else:
                    print(key,":",order.get(key))
                    continue
            print("\n")
        print("0:Back")
        try:
            user_selection = int(input("Select Order To Delete:"))
            if user_selection == 0:
               break       
            else:
                confirmation = input("Are You Sure? y/n:")
                if confirmation.lower() == "n":
                    continue
                elif confirmation.lower() == "y":
                    orders.pop(user_selection - 1)
                    save_orders(orders)
                    message("ORDER DELETED",1.5)
                    break
                else:
                    print("Select Yes Or No")
        except Exception:
                message("INVALID SELECTION",3)
                continue


#prints orders and takes user selection for orders then takes selection for item to edit
#then updates the order and saves to db
def edit_orders():
    while True:
        clear_screen()
        orders = compile_orders()
        for order in orders:
            print(orders.index(order) + 1,":")
            for key in order:
                if isinstance(order.get(key),dict):
                    for subkey in order.get(key):
                        print(subkey,": ",orders[orders.index(order)][key][subkey])
                        continue
                elif isinstance(order.get(key),list):
                    print(key,":")
                    for item in order.get(key):
                        print(item.get("Product"),"£","{:.2f}".format(item.get("Price")))
                        continue
                else:
                    print(key,":",order.get(key))
                    continue
            print("\n")
        print("0:Back")
        try:
            user_selection = int(input("Select Order:"))
            index = 1
            if user_selection == 0:
                break
            else:
                clear_screen()
                order = orders[user_selection-1]
                for item in order :
                    print(index,":",item,":",order.get(item))
                    index += 1
                print("0:Back")
                item_selection = int(input("Select Item To Edit:"))
                if item_selection == 0:
                    continue
                elif item_selection == 1:
                    category = "Customer Name"
                    new_info = input("Replace Name With:")
                elif item_selection == 2:
                    category = "Customer Adress"
                    new_info = input("Replace Adress With:")
                elif item_selection == 3:
                    category = "Customer Phone"
                    new_info = input("Replace Phone Number With:")
                elif item_selection == 4:
                    category = "Courier"
                    new_info = select_courier()
                elif item_selection == 5 or item_selection == 6:
                    category = "Order"
                    order_tup = select_items()
                    new_info = order_tup[0]
                    order["Order Total"] = order_tup[1]
                elif item_selection == 7:
                    category = "Order Status"
                    new_info = input("Replace Status With:")
            if new_info == "":
                message("NOTHING ENTERED NO CHANGES MADE",1.5)
                continue
            else:
                order[category] = new_info
                save_orders(orders)
                message("CUSTOMER INFORMATION UPDATED",1.5)
                continue
        except Exception as error:
                message("INVALID SELECTION",3)
                continue



#prints orders and asks for user selection to select order and user input for new status
#then overwrites db with new status
def update_order_status():
    update_order_status_title = r"UPDATE ORDER STATUS""\n```````````````````"
    clear_screen()
    while True:
        print(update_order_status_title)
        orders = compile_orders()
        for order in orders:
            print(orders.index(order) + 1,":")
            for key in order:
                if isinstance(order.get(key),dict):
                    for subkey in order.get(key):
                        print(subkey,": ",orders[orders.index(order)][key][subkey])
                        continue
                elif isinstance(order.get(key),list):
                    print(key,":")
                    for item in order.get(key):
                        print(item.get("Product"),item.get("Price"))
                        continue
                else:
                    print(key,":",order.get(key))
                    continue
            print("\n")
        print("0:Back")
        try:
            user_selection = int(input("Select Order:"))
            if user_selection == 0:
                break
            else:
                order = orders[user_selection - 1]              
                new_status = input("Enter New Status:")
                order.update({"Order Status":new_status})
                save_orders(orders)
                message("STATUS UPDATED",1.5)
                break
        except Exception as error:
            print("INVALID SELECTION):",error)
            continue
