# bank_core.py

class Bank:
    def __init__(self, acc_no, acc_bal, acc_pass):
        self.acc_no = acc_no
        self.acc_bal = acc_bal
        self.__acc_pass = acc_pass

    def debit(self, debit_amt):
        self.acc_bal -= debit_amt
        print(debit_amt, "has been debited")
        return self.acc_bal

    def credit(self, credit_amt):
        self.acc_bal += credit_amt
        print(credit_amt, "has been credited")
        return self.acc_bal

    def balance(self):
        return self.acc_bal

    def getpass(self):
        return self.__acc_pass

    def details(self):
        print("Account No. :", self.acc_no)
        print("Account Balance :", self.acc_bal)
