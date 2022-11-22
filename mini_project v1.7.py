#IMPORTS
#--------------------------------------------------------------------------------------------------
from misc_functions import clear_screen,message,fancy_message
from courier_functions import delete_courier,update_courier,create_courier,print_couriers
from order_functions import print_orders,create_order,delete_orders,edit_orders,update_order_status
from product_functions import add_new_item,edit_current_item,delete_item,products_list
#--------------------------------------------------------------------------------------------------


#MAIN MENU
#---------
def main_menu():
    main_menu_title ="MAIN MENU\n`````````"
    main_menu_list = ["Products","Orders","Couriers"]
    while True:
        clear_screen()
        print(main_menu_title)
        for option in main_menu_list:
            print(main_menu_list.index(option) + 1,":",option)
        print("0:Exit")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                fancy_message("GOODBYE",1.5)
                clear_screen()
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


#PRODUCT MENU
#------------
def product_menu():
    product_menu_title = "PRODUCT MENU\n````````````"
    product_menu_list = ["Show Products","Edit Products"]
    while True:
        clear_screen()
        print(product_menu_title)
        for option in product_menu_list:
            print(product_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                    break
            elif user_selection == 1:
                    products_list() 
            elif user_selection == 2:
                    product_edit_menu()
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",1.5)
            continue


#PRODUCT EDIT MENU
#-----------------
def product_edit_menu():
    edit_menu_greeting = "EDIT MENU\n`````````"
    edit_menu_list = ["Create New","Edit","Delete"]
    while True:
        clear_screen()
        print(edit_menu_greeting)
        for option in edit_menu_list:
            print(edit_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                break
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


#ORDER MENU
#----------
def order_menu():
    order_menu_list = ["Show Orders","Create Order","Edit Order Status","Edit Order","Delete Order"]
    order_menu_title = "ORDERS MENU\n```````````"
    while True:
        clear_screen()
        print(order_menu_title)
        for option in order_menu_list:
            print(order_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                break
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


#COURIER MENU
#------------
def courier_menu():
    courier_menu_list = ["Show Couriers","Create New Courier","Edit Couriers","Delete Couriers"]
    courier_menu_title = "COURIER MENU\n````````````"
    while True:
        clear_screen()
        print(courier_menu_title)
        for option in courier_menu_list:
            print(courier_menu_list.index(option) + 1,":",option)
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                break
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


#GREETING
#--------
fancy_message("Shop Programme",1)

#START OF PROGRAMME
#------------------
main_menu()