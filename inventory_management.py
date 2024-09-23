stock = {}

def add_stock(product, cost, amount):
    stock[product] = ("₹" + str(cost), amount)

def modify_quantity(sold_product, sold_amount, available_amount):
    stock[sold_product] = ("₹" + str(cost), available_amount - sold_amount)

m = int(input("Enter number of products: "))

for i in range(m):
    product = input("Enter product: ")
    cost = int(input("Enter cost: "))
    amount = int(input("Enter available amount: "))
    print()
    add_stock(product, cost, amount)
    print(f"Stock: {stock}")
    print()

sold_product = input("Enter product to modify quantity: ")
sold_amount = int(input("Enter sold amount: "))
modify_quantity(sold_product, sold_amount, amount)

print(stock)
