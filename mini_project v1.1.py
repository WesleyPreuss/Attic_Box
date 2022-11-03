import os
import time
main_menu_greeting ="MAIN MENU\n`````````"
main_menu = ["Exit","Products","Orders"]
products_menu_greeting = "PRODUCT MENU\n````````````"
products_menu = ["Back To Main Menu","Show Products","Edit Products"]
product_list_greeting = "PRODUCT LIST\n````````````\nPress 0 To Go Back"
product_list = ["Coke","Burger","Fries"]
edit_menu_greeting = "EDIT MENU\n`````````"
edit_menu = ["Back","Create New","Edit","Delete"]
orders_menu = ["Back","Show Orders","Create Order","Edit Order Status","Edit Order","Delete Order"]
orders_greeting = "ORDERS MENU\n```````````"
update_order_status_greeting = r"UPDATE ORDER STATUS""\n```````````````````"


def message(msg_txt,msg_length):
    os.system("cls")
    print(msg_txt)
    time.sleep(msg_length)


def print_menu(menu_name,greeting):
    if greeting != "ORDERS LOG":
        os.system("cls")
    else:
        pass
    print(greeting)
    for option in menu_name:
        print(menu_name.index(option),":",option)
    menu_logic(menu_name)


def compile_orders():
    order_list = []
    order_compiling = {}
    with open("mini_project_folder\orders.txt","r") as order_db:
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
        try:
            user_selection = int(input("0 To Return:"))
            if user_selection == 0:
                print_menu(orders_menu,orders_greeting)
            else:
                print("INVALID SELECTION")
        except:
            print("INVALID SELECTION")
            continue


def add_new_item():
    os.system("cls")
    print("Create New\ntype back to cancel")
    new_product_input = input("Enter New Product:")
    if new_product_input.lower() == "back":
        print_menu(edit_menu,edit_menu_greeting)
    else:
        product_list.append(new_product_input)
        message(f"New Product Added:{new_product_input}",1.5)
        print_menu(edit_menu,edit_menu_greeting) 


def edit_current_item():
    os.system("cls")
    print("Amend\ntype back to cancel")
    for product in product_list:
        print(product_list.index(product),":",product)
    
    editable = input("Select Product To Edit:")
    if editable.lower() == "back":
        print_menu(edit_menu,edit_menu_greeting)
    else:
        replacement = input("Replace With:")
        replaced_item = product_list[(int(editable))]
    try:
        product_list.pop(int(editable))
        product_list.insert(int(editable),replacement)
        message(f"PRODUCT:{replaced_item} REPLACED WITH:{replacement}",1.5)
        print_menu(edit_menu,edit_menu_greeting)
    except:
        print("INVALID OPTION")
        print_menu(edit_menu,edit_menu_greeting)


def delete_item():
    os.system("cls")
    print("Delete\ntype back to cancel")
    for product in product_list:
        print(product_list.index(product),":",product)
    try:
        deletable_item = input("Select Product To Delete:")
        if deletable_item.lower() == "back":
            print_menu(edit_menu,edit_menu_greeting)
        else:
            deleted_item = product_list[(int(deletable_item))]
            product_list.pop(int(deletable_item))
            message(f"PRODUCT:{deleted_item} DELETED",1.5)
            print_menu(edit_menu,edit_menu_greeting)
    except:
            print("INVALID OPTION")
            print_menu(edit_menu,edit_menu_greeting)


def create_order():
    os.system("cls")
    print(r"CREATE NEW ORDER""\n````````````````")
    try:
        cx_name = input("Customer Name:")
        cx_adress = input("Customer Adress:")
        cx_phone = input("Customer Phone:")
        status = "Preparing"
        new_order_dict = {"Customer Name":cx_name,"Customer Adress":cx_adress,
        "Customer Phone":cx_phone,"Order Status":status}
        new_order_string = ""
        for key in new_order_dict:
            new_order_string += key +":"+ new_order_dict[key] + "," 
        new_order_string = new_order_string.rstrip(",")
        new_order_string += "\n"
        with open("mini_project_folder\orders.txt","a+") as orders_db:
           orders_db.write(new_order_string) 
        message("NEW ORDER CREATED",1.5)
        print_menu(orders_menu,orders_greeting)
    except Exception as error_message:
        print("ERROR:",error_message)  


def save_orders(input_list):
    output_string = ""
    for order in input_list:
        for key, value in order.items():
            output_string += key + ":" + value + ","
        output_string = output_string.rstrip(",")
        output_string += "\n"
    with open("mini_project_folder\orders.txt","w") as orders_db:
        orders_db.write(output_string)


def update_order_status():
    os.system("cls")
    while True:
        orders = compile_orders()
        for order in orders:
            print(orders.index(order) + 1,":",order)
        print("0:Back")
        try:
            user_selection = int(input("Select Order:"))
            if user_selection == 0:
                print_menu(orders_menu,orders_greeting)
            else:
                order = orders[user_selection - 1]              
                print(order)
                new_status = input("Enter New Status:")
                order.update({"Order Status":new_status})
                save_orders(orders)
                message("STATUS UPDATED",1.5)
                print_menu(orders_menu,orders_greeting)
        except Exception as error:
            print("INVALID SELECTION:",error)
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
                print_menu(orders_menu,orders_greeting)
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
                    category = "Order Status"
                    new_info = input("Replace Status With:")
            if new_info == "":
                message("NOTHING ENTERED NO CHANGES MADE",1.5)
                continue
            else:
                order[category] = new_info
                save_orders(orders)
                message("CUSTOMER INFORMATION UPDATED",1.5)
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
                print_menu(orders_menu,orders_greeting)       
            else:
                confirmation = input("Are You Sure? y/n:")
                if confirmation.lower() == "n":
                    continue
                elif confirmation.lower() == "y":
                    orders.pop(user_selection - 1)
                    save_orders(orders)
                    message("ORDER DELETED",1.5)
                    print_menu(orders_menu,orders_greeting)
                else:
                    print("Select Yes Or No")
        except Exception as error:
                print("INVALID SELECTION:",error)
                time.sleep(1)
                continue


def menu_logic(current_menu):
     while True:
          try:
              user_selection = int(input("Select Your Option:"))
          except:
             print("INVALID SELECTION")
             continue
           #MAIN MENU
          if current_menu == main_menu:
             if user_selection == 0:
                    message("GOODBYE",1.5)
                    os.system("cls")
                    quit()
             elif user_selection == 1:
                    print_menu(products_menu,products_menu_greeting)
                    break 
             elif user_selection == 2:
                    print_menu(orders_menu,orders_greeting)
           #PRODUCTS MENU
          if current_menu == products_menu:
            if user_selection == 0:
                    print_menu(main_menu,main_menu_greeting)
                    break
            elif user_selection == 1:
                    print_menu(product_list,product_list_greeting) 
                    break
            elif user_selection == 2:
                    print_menu(edit_menu,edit_menu_greeting)
                    break              
           #PRODUCTS LIST
          if current_menu == product_list:
            if user_selection == 0:
                    print_menu(products_menu,products_menu_greeting)
                    break
            else:
                print("0 to go back")
           #EDIT MENU
          if current_menu == edit_menu:
            if user_selection == 0:
                    print_menu(products_menu,products_menu_greeting)
                    break
            elif user_selection == 1:
                add_new_item()
                
            elif user_selection == 2:
                edit_current_item()
              
            elif user_selection == 3:
                delete_item()
            else:
                print("INVALID SELECTION") 
           #ORDERS MENU     
          if current_menu == orders_menu:
                if user_selection == 0:
                    print_menu(main_menu,main_menu_greeting)
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
          else:
                    print("INVALID SELECTION")  
            

print_menu(main_menu,main_menu_greeting)
