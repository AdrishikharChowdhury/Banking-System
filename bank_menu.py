from constants import infor,__master_key
from bank_core import Bank
from account_ops import authenticator, create_accounts
from transactions import debit_balance, credit_balance

def bank_menu():
    print("\nWelcome to the Bank")
    print("1. Debit from account")
    print("2. Credit to account")
    print("3. Check Balance")
    print("4. View a specific account")
    print("5. View all accounts")
    print("6. Transfer money between accounts")
    print("7. Create a new account")
    print("8. Exit")
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:  # Debit
            accno = input("Enter Account No. to debit from: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to debit: "))
            if debit_balance(account['Bank_obj'], amount):
                print("Deduction successful!")
            else:
                print("Deduction failed.")
            return True

        case 2:  # Credit
            accno = input("Enter Account No. to credit to: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to credit: "))
            if credit_balance(account['Bank_obj'], amount):
                print("Transaction successful!")
            else:
                print("Transaction failed.")
            return True

        case 3:  # Check Balance
            accno = input("Enter Account No. to check balance: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            print(f"The balance of account {accno} is: {account['Bank_obj'].balance()}")
            return True

        case 4:  # View a specific account
            accno = input("Enter Account No. to view details: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            print("\nAccount Details")
            print(f"ID: #{account['ID : #']}")
            print(f"Name: {account['Name']}")
            account['Bank_obj'].details()
            return True

        case 5:  # View all accounts
            pas = input("Enter the Master Key: ")
            if pas != __master_key:
                print("Wrong Master Key, returning to menu.")
                return True

            for account in infor:
                print("\nAccount Details")
                print(f"ID: #{account['ID : #']}")
                print(f"Name: {account['Name']}")
                account['Bank_obj'].details()
            return True

        case 6:  # Transfer money
            acc_no1 = input("Enter the account number to transfer FROM: ")
            acc_no2 = input("Enter the account number to transfer TO: ")

            from_acc = None
            to_acc = None

            for acc in infor:
                if acc['Bank_obj'].acc_no == acc_no1:
                    from_acc = acc
                if acc['Bank_obj'].acc_no == acc_no2:
                    to_acc = acc

            if not from_acc:
                print(f"Account {acc_no1} not found, returning to menu.")
                return True
            if not to_acc:
                print(f"Account {acc_no2} not found, returning to menu.")
                return True

            if not authenticator(from_acc['Bank_obj']):
                print("Authentication failed for FROM account, returning to menu.")
                return True
            if not authenticator(to_acc['Bank_obj']):
                print("Authentication failed for TO account, returning to menu.")
                return True

            amount = float(input("Enter amount to transfer: "))
            if amount <= from_acc['Bank_obj'].balance():
                # Debit from FROM account
                from_acc['Bank_obj'].debit(amount)
                # Credit to TO account
                to_acc['Bank_obj'].credit(amount)
                print("\nTransfer successful!")
                print(f"From Account {acc_no1} - New balance: {from_acc['Bank_obj'].balance()}")
                print(f"To Account {acc_no2} - New balance: {to_acc['Bank_obj'].balance()}")
            else:
                print("Insufficient balance in FROM account!")
            return True

        case 7:  # Create a new account
            info = create_accounts()
            infor.append(info)
            print("New account created successfully!")
            return True

        case 8:  # Exit
            print("Thank you for using our banking system.")
            return False

        case _:  # Default case
            print("Invalid input, try again.")
            return True