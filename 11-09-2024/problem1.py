def list_fruits():
    return ["Apple", "Banana", "Orange", "Mango"]

def build_fruit_statement(fruit):
    return f"{fruit} is a delicious fruit."

fruits = list_fruits()
for fruit in fruits:
    print(build_fruit_statement(fruit))