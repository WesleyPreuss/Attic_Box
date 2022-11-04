import os
import time
import json

product_list = ["Coke","Burger","Fries"]


def fancy_message(msg_txt,msg_length):
    os.system("cls")
    input_string = msg_txt
    output_txt = ""
    for character in input_string:
        os.system("cls")
        output_txt += character
        print(output_txt)
        time.sleep(0.1)
    time.sleep(msg_length)
    



def message(msg_txt,msg_length):
    os.system("cls")
    print(msg_txt)
    time.sleep(msg_length)


def compile_orders():
    order_list = []
    order_compiling = {}
    with open("Attic_Box\orders.txt","r") as order_db:
        order_string = order_db.read()
        full_list = order_string.splitlines()
        for order in full_list:
            if order == "":
                continue
            else:
                order_item = order.split(",")
            for item in order_item:
                split = item.split(":")
                order_compiling.update({split[0]:split[1]})
            order_list.append(order_compiling)
            order_compiling = {}
    return(order_list)


def print_orders():
    os.system("cls")
    print("ORDERS LOG\n``````````")
    orders = compile_orders()
    for order in orders:
        print(orders.index(order) + 1,":")
        for key in order:   
            print(key,":",order.get(key))
    while True:
            user_selection = input("0 To Return:")
            if user_selection == "0":
                order_menu()
            else:
                print("INVALID SELECTION")


def add_new_item():
    while True:
        os.system("cls")
        print("Create New\n``````````")
        print("0:Back")
        new_product_input = input("Enter New Product:")
        if new_product_input == "0":
            product_edit_menu()
        elif new_product_input == "":
            message("INPUT BLANK NO ITEM ADDED",1.5)
            continue
        else:
            product_list.append(new_product_input)
            message(f"New Product Added:{new_product_input}",1.5)
            product_edit_menu() 


def edit_current_item():
    os.system("cls")
    print("Edit Item\n`````````")
    for product in product_list:
        print(product_list.index(product)+1,":",product)
    print("0:Back") 
    try:
        editable = int(input("Select Product To Edit:"))
        if editable == 0:
            product_edit_menu()
        else:
            replacement = input("Replace With:")
            replaced_item = product_list[(editable-1)]
        product_list[(editable-1)] = replacement
        message(f"PRODUCT: {replaced_item}\nREPLACED WITH: {replacement}",2)
        product_edit_menu()
    except Exception as error:
        print(f"INVALID OPTION\n{error}")
        product_edit_menu()


def delete_item():
    while True:
        os.system("cls")
        print("Delete\n``````")
        for product in product_list:
            print(product_list.index(product)+1,":",product)
        print("0:Back")
        try:
            deletable_item = int(input("Select Product To Delete:"))
            if deletable_item == 0:
                product_edit_menu()
            else:
                deleted_item = product_list[(deletable_item)-1]
                product_list.pop(deletable_item - 1)
                message(f"PRODUCT:{deleted_item} DELETED",1.5)
                continue
        except Exception as error:
                message(f"INVALID OPTION\n{error}",2)
                continue


def create_order():
    os.system("cls")
    print(r"CREATE NEW ORDER""\n````````````````")
    try:
        cx_name = input("Customer Name:")
        cx_adress = input("Customer Adress:")
        cx_phone = input("Customer Phone:")
        courier = select_courier()
        status = "Preparing"
        new_order_dict = {"Customer Name":cx_name,"Customer Adress":cx_adress,
        "Customer Phone":cx_phone,"Courier":courier,"Order Status":status}
        new_order_string = ""
        for key in new_order_dict:
            new_order_string += key +":"+ new_order_dict[key] + "," 
        new_order_string = new_order_string.rstrip(",")
        new_order_string += "\n"
        with open("Attic_Box\orders.txt","a+") as orders_db:
           orders_db.write(new_order_string) 
        message("NEW ORDER CREATED",1.5)
        order_menu()
    except Exception as error_message:
        print("ERROR:",error_message)  


def select_courier():
    while True:
        os.system("cls")
        try:
            title = r"SELECT COURIER""\n``````````````"
            couriers = open_courier_db()
            print(title)
            for courier in couriers:
                print(couriers.index(courier) + 1,":",courier)
            user_selection = int(input("Select Courier:"))
            if user_selection in range(1,len(couriers)+1):
                return couriers[user_selection-1]
            else:
                message("INVALID SELECTION",1.5)
                continue
        except Exception as error:
            message(f"ERROR:\n{error}",4)
            order_menu()


def save_orders(input_list):
    output_string = ""
    for order in input_list:
        for key, value in order.items():
            output_string += key + ":" + value + ","
        output_string = output_string.rstrip(",")
        output_string += "\n"
    with open("Attic_Box\orders.txt","w") as orders_db:
        orders_db.write(output_string)


def update_order_status():
    update_order_status_title = r"UPDATE ORDER STATUS""\n```````````````````"
    os.system("cls")
    while True:
        print(update_order_status_title)
        orders = compile_orders()
        for order in orders:
            print(orders.index(order) + 1,":",order)
        print("0:Back")
        try:
            user_selection = int(input("Select Order:"))
            if user_selection == 0:
                order_menu()
            else:
                order = orders[user_selection - 1]              
                print(order)
                new_status = input("Enter New Status:")
                order.update({"Order Status":new_status})
                save_orders(orders)
                message("STATUS UPDATED",1.5)
                order_menu()
        except Exception as error:
            print("INVALID SELECTION):",error)
            continue
    

def edit_orders():
    while True:
        os.system("cls")
        orders = compile_orders()
        for order in orders:
                print(orders.index(order)+1,":",order)
        print("0:Back")
        try:
            user_selection = int(input("Select Order:"))
            index = 1
            if user_selection == 0:
                order_menu()
            else:
                os.system("cls")
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
                elif item_selection == 5:
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
                print(f"INVALID SELECTION:{error}")
                time.sleep(1)
                continue


def delete_orders():
    while True:
        os.system("cls")
        orders = compile_orders()
        for order in orders:
                print(orders.index(order)+1,":",order)
        print("0:Back")
        try:
            user_selection = int(input("Select Order To Delete:"))
            if user_selection == 0:
               order_menu()       
            else:
                confirmation = input("Are You Sure? y/n:")
                if confirmation.lower() == "n":
                    continue
                elif confirmation.lower() == "y":
                    orders.pop(user_selection - 1)
                    save_orders(orders)
                    message("ORDER DELETED",1.5)
                    order_menu()
                else:
                    print("Select Yes Or No")
        except Exception as error:
                print("INVALID SELECTION:",error)
                time.sleep(1)
                continue


def main_menu():
    main_menu_title ="MAIN MENU\n`````````"
    main_menu_list = ["Products","Orders","Couriers"]
    while True:
        os.system("cls")
        print(main_menu_title)
        for option in main_menu_list:
            print(main_menu_list.index(option) + 1,":",option)
        print("0:Exit")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                fancy_message("GOODBYE",1.5)
                os.system("cls")
                exit()
            elif user_selection == 1:
                product_menu() 
            elif user_selection == 2:
                order_menu()
            elif user_selection == 3:
                courier_menu()
            else:
                continue
        except Exception as error:
            message(f"INVALID SELECTION{error}",1.5)
            continue


def product_menu():
    product_menu_title = "PRODUCT MENU\n````````````"
    product_menu_list = ["Show Products","Edit Products"]
    while True:
        os.system("cls")
        print(product_menu_title)
        for option in product_menu_list:
            print(product_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                    main_menu()
            elif user_selection == 1:
                    products_list() 
            elif user_selection == 2:
                    product_edit_menu()
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",1.5)
            continue


def products_list():
    product_list_title = "PRODUCT LIST\n````````````"
    while True:
        os.system("cls")
        print(product_list_title)
        for product in product_list:
            print(product_list.index(product) + 1,":",product)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                product_menu()
            else:
                continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",1.5)
            continue


def product_edit_menu():
    edit_menu_greeting = "EDIT MENU\n`````````"
    edit_menu_list = ["Create New","Edit","Delete"]
    while True:
        os.system("cls")
        print(edit_menu_greeting)
        for option in edit_menu_list:
            print(edit_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                product_menu()
            elif user_selection == 1:
                add_new_item()
            elif user_selection == 2:
                edit_current_item()
            elif user_selection == 3:
                delete_item()
            else:
                continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",1.5)
            continue


def order_menu():
    order_menu_list = ["Show Orders","Create Order","Edit Order Status","Edit Order","Delete Order"]
    order_menu_title = "ORDERS MENU\n```````````"
    while True:
        os.system("cls")
        print(order_menu_title)
        for option in order_menu_list:
            print(order_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                main_menu()
            elif user_selection == 1:
                print_orders()                
            elif user_selection == 2:
                create_order()
            elif user_selection == 3:
                update_order_status()
            elif user_selection == 4:
                edit_orders()
            elif user_selection == 5:
                delete_orders()
        except Exception as error:
            message(f"INVALID SELECTION{error}",1.5)
            continue


def courier_menu():
    courier_menu_list = ["Show Couriers","Create New Courier","Edit Couriers","Delete Couriers"]
    courier_menu_title = "COURIER MENU\n````````````"
    while True:
        os.system("cls")
        print(courier_menu_title)
        for option in courier_menu_list:
            print(courier_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                main_menu()
            elif user_selection == 1:
                print_couriers()               
            elif user_selection == 2:
                create_courier()
            elif user_selection == 3:
                update_courier()
            elif user_selection == 4:
                delete_courier()
        except Exception as error:
            message(f"INVALID SELECTION{error}",3)
            continue


def open_courier_db():
    with open("Attic_Box\couriers.json","r") as couriers_db:
        input_data = couriers_db.read()
        output_data = json.loads(input_data)
        return(output_data)


def save_courier_db(input):
    with open("Attic_Box\couriers.json","w") as courier_db:
        input_data = json.dumps(input)
        courier_db.write(input_data)


def print_couriers():
    try:
        title = "COURIERS\n````````"
        couriers = open_courier_db()
        while True:
            os.system("cls")
            print(title)
            for courier in couriers:
                print(couriers.index(courier) + 1,":",courier)
            print("0:Back")
            user_selection = input("Select Option:")
            if user_selection == "0":
                courier_menu()
            else:
                message("INVALID SELECTION",1.5)
    except Exception as error:
        message("ERROR:\n"+error,4)


def create_courier():
    title = r"CREATE NEW COURIER""\n""``````````````````"
    os.system("cls")
    print(title)
    new_courier = input("New Courier Name:")
    if new_courier == "":
        message("NO CHANGES MADE",1.5)
        courier_menu()
    else:
        couriers = open_courier_db()
        couriers.append(new_courier)
        save_courier_db(couriers)


def update_courier():
    title = r"EDIT COURIER""\n""````````````"
    while True:
        couriers = open_courier_db()
        os.system("cls")
        print(title)
        for courier in couriers:
            print(couriers.index(courier) + 1,":",courier)
        print("0:Back")
        try:
            user_selection = int(input("Select Courier:"))
            if user_selection == 0:
                courier_menu()
            else:
                print(couriers[user_selection-1]," << Selected")
                new_info = input("Change To: ")
                if new_info == "":
                    message("NO CHANGES MADE",1)
                    continue
                else:
                    couriers[user_selection-1] = new_info
                    save_courier_db(couriers)
                    message(r"UPDATED TO: "+new_info,2)
                    continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",3) 

        
def delete_courier():
    title = r"DELETE COURIER""\n""``````````````"
    while True:
        couriers = open_courier_db()
        os.system("cls")
        print(title)
        for courier in couriers:
            print(couriers.index(courier) + 1,":",courier)
        print("0:Back")
        try:
            user_selection = int(input("Select Courier:"))
            if user_selection == 0:
                courier_menu()
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


fancy_message("Welcome To The Shop Programme",2)


main_menu()