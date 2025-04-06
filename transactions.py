# transactions.py

def debit_balance(account, amount):
    if amount <= account.acc_bal:
        new_balance = account.debit(amount)
        print(f"{amount} has been debited from Account No.: {account.acc_no}")
        print("New balance:", new_balance)
        return True
    else:
        print("Insufficient Balance")
        return False

def credit_balance(account, amount):
    if amount <= 0 or amount >= 10000:
        print("Invalid amount")
        return False
    new_balance = account.credit(amount)
    print(f"{amount} has been credited to Account No.: {account.acc_no}")
    print("New balance:", new_balance)
    return True
