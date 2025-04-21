from account_ops import create_accounts
from bank_menu import bank_menu
from load import loadFromFile
from database import loadFromDatabase

def main():
    information=loadFromDatabase()
    if information==[]:
        try:
            n = int(input("Enter the number of bank accounts you want to create initially: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return main()

        for _ in range(n):
            bank_account = create_accounts(information)
            information.append(bank_account)
    while True:
            if not bank_menu(information):
                break


if __name__ == "__main__":
    main()
