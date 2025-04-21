# bank_core.py
from database import updateBalance
import os
import uuid
import datetime
from utils import encrypt
from html_generator import generateBankStatement
import webbrowser

class Bank:
    def __init__(self, acc_name, acc_no, acc_bal, acc_pass, acc_uid, acc_type, acc_email, acc_contact):
        self.name = acc_name
        self.acc_no = acc_no
        self.acc_bal = acc_bal
        self.__acc_pass = acc_pass
        self.uid = acc_uid
        self.type = acc_type
        self.email = acc_email
        self.contact = acc_contact
        self.transactions = []  # List of Transaction objects

    def debit(self, debit_amt, note=""):
        self.acc_bal -= debit_amt
        tid = str(uuid.uuid4())
        transaction = self.Transaction(
            datetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            type="Debit",
            amount=debit_amt,
            balance=self.acc_bal,
            tid=tid,
            bank_id=self.acc_no
        )
        self.transactions.append(transaction)
        print(debit_amt, "has been debited")
        updateBalance(self)
        return self.acc_bal

    def credit(self, credit_amt, note=""):
        self.acc_bal += credit_amt
        tid = str(uuid.uuid4())
        transaction = self.Transaction(
            datetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            type="credit",
            amount=credit_amt,
            balance=self.acc_bal,
            tid=tid,
            bank_id=self.acc_no
        )
        self.transactions.append(transaction)
        print(credit_amt, "has been credited")
        updateBalance(self)
        return self.acc_bal

    def balance(self):
        return self.acc_bal

    def getpass(self):
        return self.__acc_pass

    def details(self):
        print("\nAccount Details")
        print(f"ID: #{self.uid}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contact No.: {self.contact}")
        print(f"Account type: {self.type}")
        print(f"Account No.: {self.acc_no}")
        print(f"Account Balance: ₹{self.acc_bal}")

    def printTransactionHistory(self):
        if not self.transactions:
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "transaction history")
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, f"acc_holder_log_{self.acc_no}.csv")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("DateTime,Type,Amount,Balance,TID\n")
            for transaction in self.transactions:
                file.write(f"{transaction.datetime},{transaction.type},{transaction.amount},{transaction.balance},{transaction.transactionId}\n")

    def printToFile(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "accounts")
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, f"acc_holder_{self.acc_no}.csv")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Name,Email,Contact,Acc_type,Acc_No.,Password,Balance,UID\n")
            file.write(f"{self.name},{self.email},{self.contact},{self.type},{self.acc_no},{encrypt(self.getpass())},{self.acc_bal},{self.uid}\n")

    def printStatement(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "bank statements")
        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, f"bank_statement_acc_holder_{self.acc_no}.html")

        with open(file_path, "w", encoding="utf-8") as file:
            generateBankStatement(self,file)
        webbrowser.open(file_path)

    def deleteFile(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directories = {
            "bank_statement": os.path.join(base_dir, "bank statements"),
            "transaction_log": os.path.join(base_dir, "transaction history"),
            "account": os.path.join(base_dir, "accounts"),
        }

        file_paths = [
            os.path.join(directories["bank_statement"], f"bank_statement_acc_holder_{self.acc_no}.csv"),
            os.path.join(directories["transaction_log"], f"acc_holder_log_{self.acc_no}.csv"),
            os.path.join(directories["account"], f"acc_holder_{self.acc_no}.csv"),
        ]

        for path in file_paths:
            if os.path.exists(path):
                os.remove(path)
                print(f"Deleted: {path}")
            else:
                print(f"File not found: {path}")

    class Transaction:
        def __init__(self, datetime, type, amount, balance, tid, bank_id):
            self.datetime = datetime
            self.type = type
            self.amount = amount
            self.balance = balance
            self.transactionId = tid
            self.bank_id = bank_id  # Reference to Bank.uid or Bank.acc_no


        def __str__(self):
            "+" if self.type == "Credit" else "-"
            return f"{self.datetime:<20} | {self.amount:<7.1f} | {self.type:<7}     | TID: {self.transactionId:<36} | ₹{self.balance:<8.1f} |"
