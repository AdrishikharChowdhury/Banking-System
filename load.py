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
    files = [f for f in os.listdir(directory) if f.startswith("acc_holder_log_") and f.endswith(".csv")]
    if not files:
        print("No transaction history found.")
        return []
    
    filename = f"acc_holder_log_{bank_obj.acc_no}.csv"
    path = os.path.join(directory, filename)

    if not os.path.exists(path):
        print(f"No transaction log found for account {bank_obj.acc_no}.")
        return []

    try:
        with open(path, "r") as file:
            line = file.readline().strip()
            bank_obj.transactions = [t.strip() for t in line.split(",") if t.strip()]

    except Exception as e:
        print(f"Failed to load {filename}: {e}")

    print(f"Loaded {len(bank_obj.transactions)} transaction log(s) successfully.")

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

            transactionLogLoader(bank_obj)

            bank_object_list.append(bank_obj)

        except Exception as e:
            print(f"Failed to load {filename}: {e}")

    print(f"Loaded {len(bank_object_list)} account(s) successfully.")
    return bank_object_list
