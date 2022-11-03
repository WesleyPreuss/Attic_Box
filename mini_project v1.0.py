import os
import time
main_menu_greeting ="Main Menu"
main_menu = ["Exit","Products"]
products_menu_greeting = "Product Menu"
products_menu = ["Back To Main Menu","Show Products","Edit Products"]
product_list_greeting = "Product List : Press 0 To Go Back"
product_list = ["Coke","Burger","Fries"]
edit_menu_greeting = "EDIT MENU"
edit_menu = ["Back","Create New","Edit","Delete"]



def print_menu(menu_name,greeting,current_menu):
    os.system("cls")
    print(greeting)
    for option in menu_name:
        print(menu_name.index(option),":",option)
    menu_logic(current_menu)

def add_new_item():
    os.system("cls")
    print("Create New\ntype back to cancel")
    new_product_input = input("Enter New Product:")
    if new_product_input.lower() == "back":
        print_menu(edit_menu,edit_menu_greeting,edit_menu)
    else:
        product_list.append(new_product_input)
        os.system("cls")
        print(f"New Product Added:{new_product_input}")
        time.sleep(2)
        print_menu(edit_menu,edit_menu_greeting,edit_menu) 

def edit_current_item():
    os.system("cls")
    print("Amend\ntype back to cancel")
    for product in product_list:
        print(product_list.index(product),":",product)
    
    editable = input("Select Product To Edit:")
    if editable.lower() == "back":
        print_menu(edit_menu,edit_menu_greeting,edit_menu)
    else:
        replacement = input("Replace With:")
        replaced_item = product_list[(int(editable))]
    try:
        product_list.pop(int(editable))
        product_list.insert(int(editable),replacement)
        os.system("cls")
        print(f"PRODUCT:{replaced_item} REPLACED WITH:{replacement}")
        time.sleep(2)
        print_menu(edit_menu,edit_menu_greeting,edit_menu)
    except:
        print("INVALID OPTION")
        print_menu(edit_menu,edit_menu_greeting,edit_menu)

def delete_item():
    os.system("cls")
    print("Delete\ntype back to cancel")
    for product in product_list:
        print(product_list.index(product),":",product)
    try:
        deletable_item = input("Select Product To Delete:")
        if deletable_item.lower() == "back":
            print_menu(edit_menu,edit_menu_greeting,edit_menu)
        else:
            deleted_item = product_list[(int(deletable_item))]
            product_list.pop(int(deletable_item))
            os.system("cls")
            print(f"PRODUCT:{deleted_item} DELETED")
            time.sleep(2)
            print_menu(edit_menu,edit_menu_greeting,edit_menu)

    except:
            print("INVALID OPTION")
            print_menu(edit_menu,edit_menu_greeting,edit_menu)
    

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
                    print("EXITING")
                    quit()
             elif user_selection == 1:
                    print_menu(products_menu,products_menu_greeting,products_menu)
                    break 
             else:
                    print("INVALID SELECTION")

           #PRODUCTS MENU
          if current_menu == products_menu:
            if user_selection == 0:
                    print_menu(main_menu,main_menu_greeting,main_menu)
                    break
            elif user_selection == 1:
                    print_menu(product_list,product_list_greeting,product_list) 
                    break
            elif user_selection == 2:
                    print_menu(edit_menu,edit_menu_greeting,edit_menu)
                    break
            else:
                    print("INVALID SELECTION")        
           #PRODUCTS LIST
          if current_menu == product_list:
            if user_selection == 0:
                    print_menu(products_menu,products_menu_greeting,products_menu)
                    break
            else:
                print("0 to go back")
           #EDIT MENU
          if current_menu == edit_menu:
            if user_selection == 0:
                    print_menu(products_menu,products_menu_greeting,products_menu)
                    break
            elif user_selection == 1:
                add_new_item()
                
            elif user_selection == 2:
                edit_current_item()
              
            elif user_selection == 3:
                delete_item()
               
          else:
                    print("INVALID SELECTION")  
            

print_menu(main_menu,main_menu_greeting,main_menu)
