def debit_balance(account, amount):
    """Debits the specified amount from the given account if sufficient funds are available."""
    if amount <= account.balance():  # Use account.balance() to check balance
        new_balance = account.debit(amount)  # Call the debit method on the Bank object
        print(f"{amount} has been debited from Account No.: {account.acc_no}")
        print("New balance:", new_balance)
        return True
    else:
        print("Insufficient Balance")
        return False

def credit_balance(account, amount):
    """Credits the specified amount to the given account."""
    if amount <= 0 or amount >= 10000:  # Ensure the amount is within valid limits
        print("Invalid amount")
        return False
    new_balance = account.credit(amount)  # Call the credit method on the Bank object
    print(f"{amount} has been credited to Account No.: {account.acc_no}")
    print("New balance:", new_balance)
    return True
