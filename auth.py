from getpass import getpass
from constants import __master_key

def authenticator(account):
    count = 0
    while count < 3:
        pas = getpass(f"Enter your password (Holder: {account.acc_no}): ")
        if pas == account.getpass() or pas == __master_key:
            print("Successfully logged in.....")
            return True
        else:
            print("Wrong password,", 2 - count, "tries left")
        count += 1
    return False

def uid_verification(id, infor):
    for bank_obj in infor:
        if bank_obj.uid == id:
            return False
    return True

def acc_verification(num, infor):
    """Check if the account number already exists in the list of Bank objects"""
    for bank_obj in infor:
        if bank_obj.acc_no == num:
            return False
    return True

def passAuthenticator():
    for attempt in range(3):
        password = getpass("Enter the master key: ")
        if password == __master_key:
            print("Access granted.")
            return True
        print(f"Incorrect password. {2 - attempt} tries left.")
    print("Access denied.")
    return False