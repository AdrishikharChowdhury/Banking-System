import random
import hashlib
from auth import acc_verification
from constants import f,key

def getEmail():
    while True:
        email=input("Enter your email: ")
        if email.find("@")!=-1:
            return email
        else:
            print("Invalid email try again...")

def acc_type():
    while True:
        print("Enter the type of account you want to make: ")
        print("1. Savings Account\n2. Current Account\n3. Fixed deposit\n")
        try:
            choice=int(input("Enter your operation: "))
        except ValueError:
            print("Invalid input try again....")
            continue
        match choice:
            case 1:
                return "Savings"
            case 2:
                return "Current"
            case 3:
                return "Fixed Deposit"
            case _:
                print("Invalid input try again")
                continue

def hash_name(name):
    """Hash the name to a 6-digit value using SHA256"""
    hashed = hashlib.sha256(name.encode()).hexdigest()
    return str(int(hashed, 16) % 1000000).zfill(6)



def accountNoGenerator(name, infor):
    base = hash_name(name)  # 6-digit hashed base
    while True:
        acc_no = ''.join(str(random.randint(0, 9)) for _ in range(10))  # 10 random digits
        acc_number = base + acc_no  # Final account number
        if acc_verification(acc_number, infor):
            return acc_number

def encrypt(msg):
    # Ensure the msg is in bytes before encrypting
    msg_bytes = msg.encode('utf-8')  # Convert the message to bytes
    return f.encrypt(msg_bytes)

def decrypt(msg):
    try:
        if isinstance(msg, str):
            if msg.startswith('\\x'):
                # Decode PostgreSQL hex bytea format
                msg = bytes.fromhex(msg[2:])
            else:
                msg = msg.encode('utf-8')

        decrypted_msg = f.decrypt(msg).decode('utf-8')
        return decrypted_msg
    except Exception as e:
        print(f"Decryption failed: {type(e).__name__} - {e}")
        return None
