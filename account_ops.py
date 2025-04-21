from getpass import getpass
from constants import __master_key
from bank_core import Bank
from auth import uid_verification
from utils import accountNoGenerator,acc_type,getEmail
from database import deleteAccount

def create_accounts(infor):
    name = input("Enter the Account Holder name: ")
    acc_number = accountNoGenerator(name, infor)

    try:
        acc_balance = float(input("Enter the initial account balance: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return create_accounts(infor)

    if acc_balance < 0 or acc_balance > 50000:
        print("Invalid amount entered")
        return create_accounts(infor)

    pas = getpass("Register your password: ")

    if pas == __master_key:
        print("Can't use this as a password, try again....")
        return create_accounts(infor)
    
    uid = input("Enter your unique ID: ")
    if not uid_verification(uid, infor):
        print("This UID already exists. Try again with a new one.")
        return create_accounts(infor)
    
    type=acc_type();
    email=getEmail();
    contact=input("Enter your contact number: ")
    # Create a new Bank object and append it to the list
    person = Bank(name,acc_number, acc_balance, pas, uid,type,email,contact)
    print(f"Account created successfully with account number: {acc_number}")
    return person

def deleteAccounts(information):
    accno=input("Enter the account number you want to delete: ")
    for idx,bank_obj in enumerate(information):
        if bank_obj.acc_no==accno:
            information[idx].deleteFile()
            del information[idx]
            deleteAccount(bank_obj)
            return
    print("Account not found, Returning to menu........")
    return