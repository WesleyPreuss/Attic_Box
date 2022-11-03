import json


def open_courier_db():
    with open("mini_project_folder/test.json","r") as test_db:
        input_data = test_db.read()
        output_data = json.loads(input_data)
        return(output_data)

