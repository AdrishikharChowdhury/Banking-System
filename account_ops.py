# account_ops.py

from constants import infor, __master_key
from bank_core import Bank

def acc_verification(num):
    for elem in infor:
        if elem['Bank_obj'].acc_no == num:
            return False
    return True

def create_accounts():
    name = input("Enter the Account Holder name: ")
    acc_number = input("Enter the account number: ")

    if not acc_verification(acc_number):
        print("Account number is already in use, please change it.")
        return create_accounts()

    try:
        acc_balance = float(input("Enter the account balance: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return create_accounts()

    if acc_balance < 0 or acc_balance > 50000:
        print("Invalid amount entered")
        return create_accounts()

    pas = input("Register your password: ")
    if pas == __master_key:
        print("Can't use this as a password, try again....")
        return create_accounts()

    person = Bank(acc_number, acc_balance, pas)
    info = {
        "ID : #": len(infor) + 1,
        "Name": name,
        "Bank_obj": person
    }
    return info

def authenticator(account):
    count = 0
    while count < 3:
        pas = input(f"Enter your password (Holder: {account.acc_no}): ")
        if pas == account.getpass() or pas == __master_key:
            print("Successfully logged in.....")
            return True
        else:
            print("Wrong password,", 2 - count, "tries left")
        count += 1
    return False
