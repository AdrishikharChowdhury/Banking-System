# constants.py

import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

# master key generation
__master_key = os.getenv("MASTER_KEY")

# cryptography key generation
# Generate the key from key generator.py and add it to .env file
key = os.getenv("FERNET_KEY").encode() 
f = Fernet(key)

# database connection
hostname = os.getenv("HOSTNAME")
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")
port_id = os.getenv("PORT_ID")
# Create the Bank table with acc_no as primary key
create_script1 = '''CREATE TABLE IF NOT EXISTS Bank(
    acc_no TEXT PRIMARY KEY,
    uid TEXT NOT NULL,
    acc_name TEXT NOT NULL,
    acc_bal NUMERIC(12, 2) NOT NULL,
    acc_pass TEXT NOT NULL,
    acc_type TEXT NOT NULL,
    acc_email TEXT,
    acc_contact TEXT
);'''
# Create the Transactions table, ensuring account_number is linked to acc_no
create_script2 = '''CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id UUID PRIMARY KEY, 
    account_number TEXT NOT NULL,
    transaction_date TIMESTAMP NOT NULL,
    transaction_type TEXT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    balance NUMERIC(12, 2) NOT NULL,
    FOREIGN KEY (account_number) REFERENCES Bank(acc_no) ON DELETE CASCADE
);'''
# Insert query for the Bank table
insert_script1 = '''
INSERT INTO Bank(acc_no, uid, acc_name, acc_bal, acc_pass, acc_type, acc_email, acc_contact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (acc_no) DO NOTHING;
'''
insert_script2 = '''INSERT INTO Transactions (transaction_id, account_number, transaction_date, transaction_type, amount, balance) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (transaction_id) DO NOTHING'''

conn = None

if __master_key is None:
    raise ValueError("MASTER_KEY not found in environment variables!")

if key is None:
    raise ValueError("FERNET_KEY not found in environment variables!")

