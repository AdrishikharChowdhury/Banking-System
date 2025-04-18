# constants.py

import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

__master_key = os.getenv("MASTER_KEY")

key = os.getenv("FERNET_KEY").encode()
f = Fernet(key)

if __master_key is None:
    raise ValueError("MASTER_KEY not found in environment variables!")

if key is None:
    raise ValueError("FERNET_KEY not found in environment variables!")
