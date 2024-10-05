def add_excitement(strings):
    new_list = []
    for s in strings:
        new_list.append(s+"!")
    return new_list
        
strings = ["Apple", "Samsung", "OnePlus", "Oppo", "Vivo"]
new_strings = add_excitement(strings)
print(f"{new_strings}")