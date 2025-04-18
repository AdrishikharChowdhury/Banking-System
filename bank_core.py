# bank_core.py
import os
from utils import encrypt
class Bank:
    def __init__(self,acc_name, acc_no, acc_bal, acc_pass,acc_uid,acc_type,acc_email,acc_contact):
        self.name=acc_name
        self.acc_no = acc_no
        self.acc_bal = acc_bal
        self.__acc_pass = acc_pass
        self.uid=acc_uid
        self.type=acc_type
        self.email=acc_email
        self.contact=acc_contact
        self.transactions=[]

    def debit(self, debit_amt):
        self.acc_bal -= debit_amt
        debit=f"-{debit_amt}"
        self.transactions.append(debit)
        print(debit_amt, "has been debited")
        return self.acc_bal

    def credit(self, credit_amt):
        self.acc_bal += credit_amt
        credit=f"+{credit_amt}"
        self.transactions.append(credit)
        print(credit_amt, "has been credited")
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
        print("Account No. :", self.acc_no)
        print("Account Balance :", self.acc_bal)
    
    def printTransactionHistory(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "transaction history")

        if self.transactions==[]:
            return

        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, f"acc_holder_log_{self.acc_no}.csv")

        with open (file_path, "w", encoding="utf-8") as file:
            for transaction in self.transactions:
                file.write(f"{transaction},")

    def printToFile(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "accounts")
        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, f"acc_holder_{self.acc_no}.csv")


        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Name,Email,Contact,Acc_type,Acc_No.,Password,Balance,UID\n")
            file.write(f"{self.name},{self.email},{self.contact},{self.type},{self.acc_no},{encrypt(self.__acc_pass)},{self.acc_bal},{self.uid}\n")

    def printStatement(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, "bank statements")
        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, f"bank_statement_acc_holder_{self.acc_no}.csv")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"""
    ========== BANK STATEMENT ==========
    Account Holder : {self.name}
    Account No.    : {self.acc_no}
    Account Type   : {self.type}
    Email          : {self.email}
    Contact        : {self.contact}
    UID            : {self.uid}
    Current Balance: ₹{self.acc_bal}
    ========================================
                Transactions
    """)
            if self.transactions == []:
                file.write("No Transactions History\n")
            else:
                for transaction in self.transactions:
                    file.write(f"""\n
                                    {transaction}""")
                file.write(f"""
    \n      Final Balance:                 {self.acc_bal}
    ==========================================\n""")
                
    def deleteFile(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory1 = os.path.join(base_dir, "bank statements")
        directory2 = os.path.join(base_dir, "transaction history")
        directory3 = os.path.join(base_dir, "accounts")
        file_paths=[os.path.join(directory1, f"bank_statement_acc_holder_{self.acc_no}.csv"),
                    os.path.join(directory2, f"acc_holder_log_{self.acc_no}.csv"),
                    os.path.join(directory3, f"acc_holder_{self.acc_no}.csv")]
        for path in file_paths:
            if os.path.exists(path):
                os.remove(path)
                print(f"Deleted: {path}")
            else:
                print(f"File not found: {path}")
