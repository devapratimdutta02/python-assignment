from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

accounts = {
    "1001": {"pin": "1234", "balance": 5000.0, "transactions": []},
    "1002": {"pin": "2345", "balance": 3000.0, "transactions": []},
    "1003": {"pin": "3456", "balance": 7000.0, "transactions": []}
}

current_account = None

#functions
def login_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.geometry("484x480")
    root.config(bg='lavender')
    global photo
    photo = PhotoImage(file='bpb_img1.png')
    label = Label(image=photo).grid(row=0)

    Label(root, text="Welcome to Blue Peak Bank",bg="lavender", fg="purple", font="comicsansms 16 bold",padx=15, pady=15).grid(row=1, column=0)
    
    ac_no = Label(root, text="Account Number :", font=("Helvetica", 10),bg="lavender")
    pin = Label(root, text="PIN :",bg="lavender")
    
    ac_no.grid(row=2, column=0)
    pin.grid(row=4, column=0)

    ac_no_value = StringVar()
    pin_value = StringVar()

    ac_no_entry = Entry(root, textvariable = ac_no_value)
    pin_entry = Entry(root, textvariable=pin_value, show="*")

    ac_no_entry.grid(row=3, column=0, pady=7)
    pin_entry.grid(row=5, column=0, pady=7)

    Button(text="Login", bg="purple", fg="white", command=lambda: authenticate(ac_no_entry.get(), pin_entry.get())).grid(row = 6, column=0)

def authenticate(ac_no, pin):
    global current_account
    if ac_no in accounts and accounts[ac_no]["pin"] == pin:
        current_account = ac_no
        messagebox.showinfo(" Success", "Login Successfull")
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid Account Number or PIN")


def main_menu():
    for widget in root.winfo_children():
        widget.destroy()
        
    root.geometry("360x360")
    root.title('BPB')
    root.config(bg='lavender')
    
    Label(root, text=f"Account Number : {current_account}", bg="lavender", fg="purple", font="comicsansms 14 bold").pack(pady=30)
    Button(root, text="Deposit", bg="violet", fg="black", command=deposit).pack(pady=5)
    Button(root, text="Withdraw",bg="violet", fg="black", command=withdraw).pack(pady=5)
    Button(root, text="Check Balance",bg="violet", fg="black", command=check_balance).pack(pady=5)
    Button(root, text="Mini Statement",bg="violet", fg="black", command=mini_statement).pack(pady=5)
    Button(root, text="Logout",bg="purple", fg="white", command=login_screen).pack(pady=25)

def deposit():
    amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
    
    if amount and amount > 0:
        accounts[current_account]["balance"] += amount
        accounts[current_account]["transactions"].append(f"Deposited: ${amount:.2f}")
        messagebox.showinfo("Success", f"Deposited: ${amount:.2f}")
    else:
        messagebox.showerror("Error", "Invalid amount")

def withdraw():
    amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
    if amount and amount > 0:
        if accounts[current_account]["balance"] >= amount:
            accounts[current_account]["balance"] -= amount
            accounts[current_account]["transactions"].append(f"Withdrew: ${amount:.2f}")
            messagebox.showinfo("Success", f"Withdrew: ${amount:.2f}")
        else:
            messagebox.showerror("Error", "Insufficient funds")
    else:
        messagebox.showerror("Error", "Invalid amount")
    
def check_balance():
    balance = accounts[current_account]["balance"]
    messagebox.showinfo("Balance", f"Current balance: ${balance:.2f}")
    
def mini_statement():
    global current_account
    transactions = accounts[current_account]["transactions"][-5:]  # Last 5 transactions
    if transactions:
        statement = "\n".join(transactions)
    else:
        statement = "No transactions yet."
    messagebox.showinfo("Mini Statement", statement)
    
root = Tk()
root.geometry("484x480")
root.title('BPB')
root.wm_iconbitmap("bpb_icon.ico")

login_screen()

root.mainloop()
