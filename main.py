# main.py

from account_ops import create_accounts
from constants import infor
from bank_menu import bank_menu

def main():
    try:
        n = int(input("Enter the number of bank accounts you want to create initially: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return main()

    for _ in range(n):
        info = create_accounts()
        infor.append(info)

    while True:
        if not bank_menu():
            break

if __name__ == "__main__":
    main()
