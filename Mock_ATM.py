account_details = {"Name": "Kevin Jovita",
                  "Balance": 5000,
                  "Account Type": "Savings",
                  "Pin": 1234}

def withdraw(x):
    account_details["Balance"] = account_details["Balance"] - x
    print(account_details)


def deposit(x):
    account_details["Balance"] = account_details["Balance"] + x
    print(account_details)


def check_balance():
    print(account_details["Balance"])


def change_pin(p):
    account_details['Pin'] = p
    print(account_details)


p = input("What is yur name?: ")

if p in account_details["Name"]:
    Pin = int(input("Pin: "))
    if Pin == account_details["Pin"]:
        print("1: Withdraw\n 2: Deposit\n 3: Change Pin")
        selection = int(input("Input Selection: "))
        if selection == 1:
            amount = int(input("Amount: "))
            withdraw(amount)
        elif selection == 2:
            amount = int(input("Amount: "))
            deposit(amount)
        elif selection == 3:
            new_pin = int(input("New Pin: "))
            change_pin(new_pin)
        else:
            print("Fill a selection")
    else:
        print("Wrong Pin")
else:
    print("Wrong Name")

# if account_details["Balance"] < 6000:
#     print("Welcome to Mock ATM")
# else:
#     print("Try again")
