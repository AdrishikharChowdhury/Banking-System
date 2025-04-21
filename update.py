from utils import getEmail,acc_type
from auth import uid_verification

def updateInfo(account,infor):
    while True:
        print("What do you want to update: ")
        print("1. Name")
        print("2. Email")
        print("3. Contact")
        print("4. Account Type")
        print("5. Password")
        print("6. Unique ID")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Wrong type of input")
            return True
        match choice:
            case 1:
                account.name=input("Enter your updated name: ")
                print("Name updated successfully")
                return
            
            case 2:
                account.email=getEmail()
                print("Email updated successfully")
                return
            
            case 3:
                account.contact=input("Enter your updated contact no.: ")
                print("Name updated successfully")
                return
            
            case 4:
                account.type=acc_type()
                print("Name updated successfully")
                return
            
            case 5:
                account.__acc_pass=input("Enter the updated password: ")
                print("Password updated successfully")
                return
            
            case 6:
                uid = input("Enter your unique ID: ")
                if not uid_verification(uid, infor):
                    print("This UID already exists. Try again with a new one.")
                    continue
                print("Unique ID updated successfully")
                return
            
            case 7:
                print("Returning back to main menu.....")
                return
            
            case _:
                print("Wrong input try again........")
                continue