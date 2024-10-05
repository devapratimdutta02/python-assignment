def add_excitement(strings):
    n = len(strings)
    for i in range(n):
        strings[i]+="!"
        
strings = ["Apple", "Banana", "Kiwi", "Mango", "Orange"]
add_excitement(strings)
print(f"{strings}")