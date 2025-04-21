from constants import hostname, database, username, pwd, port_id,create_script1,create_script2,insert_script1,insert_script2,conn
import psycopg2
import psycopg2.extras
from utils import encrypt,decrypt
from auth import passAuthenticator

def loadFromDatabase():
    from bank_core import Bank
    bank_list=[]
    if not passAuthenticator():
        return bank_list
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM BANK")
                accounts=cur.fetchall()
                for acc in accounts:
                    bank_obj = Bank(
                        acc_name=acc["acc_name"],
                        acc_no=acc["acc_no"],
                        acc_bal=float(acc["acc_bal"]),
                        acc_pass=decrypt(acc["acc_pass"]),
                        acc_uid=acc["uid"],
                        acc_type=acc["acc_type"],
                        acc_email=acc["acc_email"],
                        acc_contact=acc["acc_contact"]
                    )
                    cur.execute(
                        "SELECT * FROM Transactions WHERE account_number = %s ORDER BY transaction_date ASC",
                        (acc["acc_no"],)
                    )
                    transactions=cur.fetchall()
                    for row in transactions:
                        txn = Bank.Transaction(
                            datetime=row["transaction_date"],
                            type=row["transaction_type"],
                            amount=float(row["amount"]),
                            balance=float(row["balance"]),
                            tid=row["transaction_id"],
                            bank_id=row["account_number"]
                        )
                        bank_obj.transactions.append(txn)
                    
                    bank_list.append(bank_obj)
                print(f"Loaded {len(bank_list)} account(s) from the database.")
                return bank_list
    except Exception as e:
        print(f"Failed to load the data from the database to program: {e}")
        return bank_list

def loadSingleAccount(bank):
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(create_script1)        
                cur.execute(create_script2)
                loadSingleAccountData(bank,cur)
                # Insert transaction history for each bank object
                if bank.transactions:  # Ensure we have transactions before inserting
                    loadTransactionHistoryData(bank,cur)
                else:
                    print("No transaction history found")
                conn.commit()
                print("Account is inserted into the table")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def loadSingleAccountData(bank,cur):
    data = (
        bank.acc_no,         # acc_no as primary key
        bank.uid,            # Store uid, not unique
        bank.name,           # acc_name
        bank.acc_bal,        # acc_bal
        encrypt(bank.getpass()),  # acc_pass (private field, encrypted)
        bank.type,           # acc_type
        bank.email,          # acc_email
        bank.contact         # acc_contact
    )
    cur.execute(insert_script1, data)

def loadTransactionHistoryData(bank,cur):
    for transaction in bank.transactions:
        if not transaction.transactionId:
            print(f"Skipping transaction with missing ID for account {bank.acc_no}")
            continue
        if not transaction.bank_id:
            print(f"Skipping transaction with missing bank_id for account {bank.acc_no}")
            continue
        # Ensuring that the transaction account_number matches acc_no from the Bank table
        transaction_data = (
            transaction.transactionId,  # UUID
            transaction.bank_id,        # account_number (linked to acc_no)
            transaction.datetime,       # transaction_date
            transaction.type,           # transaction_type ('Debit'/'Credit')
            transaction.amount,         # amount
            transaction.balance         # balance after transaction
        )
        cur.execute(insert_script2, transaction_data)

def loadDatabase(information):
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(create_script1)        
                cur.execute(create_script2)
                for bank in information:
                    # Bank data insertion, acc_no is primary key
                    loadSingleAccountData(bank,cur)
                    # Insert transaction history for each bank object
                    if bank.transactions:  # Ensure we have transactions before inserting
                        loadTransactionHistoryData(bank,cur)
                conn.commit()
                print("Data Inserted")
    except Exception as error:
        print(f"Error: {error}")
    
    finally:
        if conn is not None:
            conn.close()

def updateBalance(bank):
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE Bank SET acc_bal = %s WHERE acc_no = %s;",
                    (bank.acc_bal, bank.acc_no)
                )
                conn.commit()
    except Exception as e:
        print(f"Failed to update balance: {e}")

def updateInfoDB(bank):
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE Bank
                    SET 
                        acc_name = %s,
                        acc_email = %s,
                        acc_contact= %s,
                        acc_type = %s,
                        uid = %s,
                        acc_pass = %s
                    WHERE acc_no = %s;
                    """,
                    (
                        bank.name,
                        bank.email,
                        bank.contact,
                        bank.type,
                        bank.uid,
                        encrypt(bank.getpass()),
                        bank.acc_no
                    )
                )
                conn.commit()
    except Exception as e:
        print(f"Failed to update account info: {e}")


def deleteAccount(bank):
    try:
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            port=port_id,
            password=pwd
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM Bank WHERE acc_no = %s", (bank.acc_no,)
                    )
            conn.commit()

    except Exception as e:
        print(f"Failed to delete account: {e}")