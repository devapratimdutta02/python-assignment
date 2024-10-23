def fetch_account_data():
    account_data = {}
    with open('accounts.txt', 'r') as file:
        for line in file:
            account_number, balance = line.split(',')
            account_data[account_number] = float(balance)
    return account_data

def transfer_funds(from_acc, to_acc, amount):
    accounts = fetch_account_data()

    if from_acc not in accounts or to_acc not in accounts:
        raise ValueError("Error: Invalid Account Number!")

    if accounts[from_acc] < amount:
        raise ValueError("Error: Insufficient Funds!")

    accounts[from_acc] -= amount
    accounts[to_acc] += amount

    print(f"Transferred {amount} from account {from_acc} to account {to_acc}.")
    print(f"New balance for {from_acc}: {accounts[from_acc]}")
    print(f"New balance for {to_acc}: {accounts[to_acc]}")

try:
    transfer_funds('1001', '1004', 500)
except ValueError as e:
    print(e)
