from cryptography.fernet import Fernet
import os

# Generate the key
key = Fernet.generate_key()

# Get the correct directory path for "Banking System"
directory = os.path.join(os.getcwd(), "Banking System")  # Ensure you are joining with the current working directory

# Define the file path for the constant.py file
filepath = os.path.join(directory, "constants.py")

# Write the key to the constant.py file (appending it)
with open(filepath, 'a') as file:
    file.write(f"key = {key!r}\n")
