import os
import csv
from auth import passAuthenticator
from bank_core import Bank
from utils import decrypt

def transactionLogLoader(bank_obj):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "transaction history")
    
    if not os.path.exists(directory):
        print("No transaction history directory found.")
        return
    
    filename = f"acc_holder_log_{bank_obj.acc_no}.csv"
    path = os.path.join(directory, filename)

    if not os.path.exists(path):
        print(f"No transaction log found for account {bank_obj.acc_no}.")
        return

    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = Bank.Transaction(
                    datetime=row["DateTime"],
                    type=row["Type"],
                    amount=float(row["Amount"]),
                    balance=float(row["Balance"]),
                    tid=row["TID"],
                    bank_id=bank_obj.acc_no
                )
                bank_obj.transactions.append(transaction)

        print(f"Loaded {len(bank_obj.transactions)} transaction log(s) for account {bank_obj.acc_no}.")

    except Exception as e:
        print(f"Failed to load transaction log {filename}: {e}")

def loadFromFile():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "accounts")

    if not os.path.exists(directory):
        print("No account directory found.")
        return []

    files = [f for f in os.listdir(directory) if f.startswith("acc_holder_") and f.endswith(".csv")]

    if not files:
        print("No saved accounts found.")
        return []

    if not passAuthenticator():
        return []

    bank_object_list = []

    for filename in files:
        path = os.path.join(directory, filename)
        try:
            with open(path, "r") as file:
                reader = csv.DictReader(file)
                data = next(reader)
            
            bank_obj = Bank(
                acc_name=data["Name"],
                acc_no=data["Acc_No."],
                acc_bal=float(data["Balance"]),
                acc_pass=decrypt(data["Password"]),
                acc_uid=data["UID"],
                acc_type=data["Acc_type"],
                acc_email=data["Email"],
                acc_contact=data["Contact"]
            )

            # Load transaction history
            transactionLogLoader(bank_obj)
            bank_object_list.append(bank_obj)

        except Exception as e:
            print(f"Failed to load {filename}: {e}")

    print(f"Loaded {len(bank_object_list)} account(s) successfully.")
    return bank_object_list