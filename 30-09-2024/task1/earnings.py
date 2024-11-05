total_earnings = 0

def add_earning(amount):
    global total_earnings
    total_earnings +=amount
    
def calculate_earnings():
    print(f"Total rental earnings: {total_earnings}")