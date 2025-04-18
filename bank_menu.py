from constants import __master_key
from account_ops import create_accounts,deleteAccounts
from transactions import debit_balance, credit_balance
from getpass import getpass
from auth import authenticator,passAuthenticator

def bank_menu(infor):
    print("\nWelcome to the Bank")
    print("1. Debit from account")
    print("2. Credit to account")
    print("3. Check Balance")
    print("4. View a specific account")
    print("5. View all accounts")
    print("6. Transfer money between accounts")
    print("7. Download a specific account information")
    print("8. Download all account informations")
    print("9. Download Bank Statement")
    print("10. Create a new account")
    print("11. Delete an account")
    print("12. Exit")
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:  # Debit
            accno = input("Enter Account No. to debit from: ")
            account = None
            for bank_obj in infor:
                if bank_obj.acc_no == accno:
                    account = bank_obj
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to debit: "))
            if debit_balance(account, amount):
                print("Deduction successful!")
            else:
                print("Deduction failed.")
            return True

        case 2:  # Credit
            accno = input("Enter Account No. to credit to: ")
            account = None
            for bank_obj in infor:
                if bank_obj.acc_no == accno:
                    account = bank_obj
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to credit: "))
            if credit_balance(account, amount):
                print("Transaction successful!")
            else:
                print("Transaction failed.")
            return True

        case 3:  # Check Balance
            accno = input("Enter Account No. to check balance: ")
            account = None
            for bank_obj in infor:
                if bank_obj.acc_no == accno:
                    account = bank_obj
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account):
                print("Authentication failed, returning to menu.")
                return True

            print(f"The balance of account {accno} is: {account.balance()}")
            return True

        case 4:  # View a specific account
            accno = input("Enter Account No. to view details: ")
            account = None
            for bank_obj in infor:
                if bank_obj.acc_no == accno:
                    account = bank_obj
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account):
                print("Authentication failed, returning to menu.")
                return True
            bank_obj.details()
            return True

        case 5:  # View all accounts
            pas = getpass("Enter the Master Key: ")
            if pas != __master_key:
                print("Wrong Master Key, returning to menu.")
                return True

            for bank_obj in infor:
                bank_obj.details()
            return True

        case 6:  # Transfer money
            acc_no1 = input("Enter the account number to transfer FROM: ")
            acc_no2 = input("Enter the account number to transfer TO: ")

            from_acc = None
            to_acc = None

            for bank_obj in infor:
                if bank_obj.acc_no == acc_no1:
                    from_acc = bank_obj
                if bank_obj.acc_no == acc_no2:
                    to_acc = bank_obj

            if not from_acc:
                print(f"Account {acc_no1} not found, returning to menu.")
                return True
            if not to_acc:
                print(f"Account {acc_no2} not found, returning to menu.")
                return True

            if not authenticator(from_acc):
                print("Authentication failed for FROM account, returning to menu.")
                return True
            if not authenticator(to_acc):
                print("Authentication failed for TO account, returning to menu.")
                return True

            amount = float(input("Enter amount to transfer: "))
            if amount <= from_acc.balance():
                # Debit from FROM account
                from_acc.debit(amount)
                # Credit to TO account
                to_acc.credit(amount)
                print("\nTransfer successful!")
                print(f"From Account {acc_no1} - New balance: {from_acc.balance()}")
                print(f"To Account {acc_no2} - New balance: {to_acc.balance()}")
            else:
                print("Insufficient balance in FROM account!")
            return True
        
        case 7:
            accno=input("Enter the account number to print their account information: ")
            for bank_obj in infor:
                if bank_obj.acc_no==accno:
                    account=bank_obj
                    break
            if not account:
                print("Account not found, Returning to menu....")
            else:
                isLogin=authenticator(account)
                if not isLogin:
                    print("Access Denied, Returning to main menu.....")
                else:
                    account.printToFile()
                    print("Filed saved to system successfully")
            return True
        
        case 8:
            if not passAuthenticator():
                print("Returning to main menu")
            else:
                for bankInfo in infor:
                    bankInfo.printToFile()
                print("All accounts are saved in the system successfully")
            return True
        
        case 9:
            account=None
            accno=input("Enter the account number to download/show the bank statement: ")
            for bank_obj in infor:
                if bank_obj.acc_no==accno:
                    account=bank_obj
                    break
            if not account:
                print("Account not found, Returning to menu....")
            else:
                account.printStatement()           
            return True

        case 10:  # Create a new account
            info = create_accounts(infor)
            infor.append(info)
            print("New account created successfully!")
            return True
        
        case 11:
            deleteAccounts(infor)
            print("Account deleted successfully")
            return True

        case 12:  # Exit
            choice=input("Do you want to save the informations (y/n): ")
            if choice=='y' or choice=='Y':
                for bankInfo in infor:
                    bankInfo.printToFile()
                    bankInfo.printTransactionHistory()
            print("Thank you for using our banking system.")
            return False

        case _:  # Default case
            print("Invalid input, try again.")
            return True