# import json

# my_list = [1, 2, 3, "four", "five"]

# json_string = json.dumps(my_list)

# print(json_string)



import json

# serialize Python object and write to JSON file
python_obj = {'name': 'John', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(python_obj, file)
