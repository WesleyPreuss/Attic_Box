import json

from misc_functions import clear_screen,message,fancy_message




#This function loads the items JSON and returns the contents
def open_item_db():
    with open("items.json","r") as items_db:
        input_data = items_db.read()
        output_data = json.loads(input_data)
        return(output_data)

#This function takes an input and saves it to the items JSON the arg is the input data
def save_item_db(input):
    with open("items.json","w") as item_db:
        input_data = json.dumps(input)
        item_db.write(input_data)

#Takes input from user and creates a new item for the item DB
def add_new_item():
    while True:
        try:
            new_item = {}
            clear_screen()
            print("Create New\n``````````")
            print("0:Back")
            new_product_input = input("Enter New Product:")
            if new_product_input == "0":
                break
            elif new_product_input == "":
                message("INPUT BLANK NO ITEM ADDED",1.5)
                continue
            else:
                while True:
                    try:
                        new_price_input = float(input("Price:"))
                        if new_price_input < 0:
                            print("Please Enter A Positive Numerical Value")
                            continue
                        else:
                            break
                    except:
                        print("Please Enter A Numerical Value")
                        continue
                if new_price_input == 0:
                    break
                else:
                    new_item.update({"Product":new_product_input,"Price":new_price_input})
                    try:
                        item_db = open_item_db()
                        item_db.append(new_item)
                        save_item_db(item_db)
                    except:
                        new_db = []
                        new_db.append(new_item)
                        save_item_db(new_db)
                    
                    message(f"New Product Added:{new_product_input}: {new_price_input}",1.5)
                    break 
        except Exception as error:
            message(f"ERROR:{error}",5)

#Prints item DB and takes user selection and overwrites the item DB
def edit_current_item():
    while True:
        clear_screen()
        print("Edit Item\n`````````")
        product_list = open_item_db()
        for product in product_list:
            print(product_list.index(product)+1,":",product.get("Product")," £","{:.2f}".format(product.get("Price")))
        print("0:Back") 
        try:
            editable = int(input("Select Product To Edit:"))
            if editable == 0:
                break
            else:
                replacement = input("Replace With:")
                while True:
                        try:
                            new_price_input = float(input("Price:"))
                            if new_price_input < 0:
                                print("Please Enter A Positive Numerical Value")
                                continue
                            else:
                                break
                        except:
                            print("Please Enter A Numerical Value")
                            continue
                replaced_item = product_list[(editable-1)].get("Product")
            product_list[(editable-1)].update({"Product":replacement,"Price":new_price_input})
            message(f"PRODUCT: {replaced_item}\nREPLACED WITH: {replacement}",2)
            save_item_db(product_list)
            break
        except Exception as error:
            print(f"INVALID OPTION\n{error}")
            continue

#Prints item DB,takes user selection for deletion and confirms before removing the item and overwriting the DB
def delete_item():
    while True:
        clear_screen()
        product_list = open_item_db()
        print("Delete\n``````")
        for product in product_list:
            print(product_list.index(product)+1,":",product.get("Product"))
        print("0:Back")
        try:
            deletable_item = int(input("Select Product To Delete:"))
            if deletable_item == 0:
                break
            else:
                deleted_item = product_list[(deletable_item)-1].get("Product")
                product_list.pop(deletable_item - 1)
                save_item_db(product_list)
                message(f"PRODUCT:{deleted_item} DELETED",1.5)
                continue
        except Exception as error:
                message(f"INVALID OPTION\n{error}",2)
                continue
#Prints items and takes user selection displaying selection made and total
#outputs a tuple (list[dict{"Product":product-name,"Price":price}],total)
def select_items():
    new_order = []
    while True:
        clear_screen()
        if new_order == []:
            pass
        else:
            print("\nNEW ORDER\n`````````")
            total = float(0)
            for item in new_order:
                print(item.get("Product"),": £","{:.2f}".format(item.get("Price")))
                total += item.get("Price")
            print("`````````")
            print(f"Total: £","{:.2f}".format(total))
            print("`````````\n\n")
        item_db = open_item_db()
        for item in item_db:
            print(item_db.index(item)+1,": ",item.get("Product"),"  £","{:.2f}".format(item.get("Price")))
        print("0:Cancel")
        print("Type Confirm To Continue")
        
        try:
            user_selection = input("Add An Item:")
            if user_selection == "0":
                message("ORDER CANCELLED",1.5)
                break
            elif user_selection.lower() == "confirm":
                return new_order,total
            elif int(user_selection) in range(1,len(item_db)+1):
                new_entry ={}
                new_entry.update({"Product":item_db[int(user_selection)-1].get("Product")})
                new_entry.update({"Price":item_db[int(user_selection)-1].get("Price")})
                new_order.append(new_entry)
            else:
                message("INVALID SELECTION",1.5)
                continue
        except Exception as error:
            message(f"ERROR{error}",3)
            continue


#prints products from db and takes user input for back
def products_list():
    product_list_title = "PRODUCT LIST\n````````````"
    while True:
        clear_screen()
        print(product_list_title)
        product_list = open_item_db()
        for product in product_list:
            print(product_list.index(product) + 1,":",product.get("Product"),"  £","{:.2f}".format(product.get("Price")))
        print("0:Back")
        try:
            user_selection = int(input("Select Option:"))
            if user_selection == 0:
                break
            else:
                continue
        except Exception as error:
            message(f"INVALID SELECTION\n{error}",1.5)
            continue
