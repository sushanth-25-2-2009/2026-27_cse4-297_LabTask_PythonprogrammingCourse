balance = 1000

def deposit(amount):
    global balance
    balance += amount

def show_local_balance():
    balance = 500
    print("Local balance:", balance)

deposit(200)
show_local_balance()
print("Account balance:", balance)
