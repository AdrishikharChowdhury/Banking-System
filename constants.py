# constants.py

import os
from dotenv import load_dotenv

load_dotenv()  # loads .env variables into the environment

infor = []
__master_key = os.getenv("MASTER_KEY")

if __master_key is None:
    raise ValueError("MASTER_KEY not found in environment variables!")
