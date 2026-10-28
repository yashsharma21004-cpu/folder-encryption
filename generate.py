from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Success: 'key.key' file created.")

def load_key():
    if os.path.exists("key.key"):
        return open("key.key", "rb").read()
    else:
        print("Error: key.key file not found!")
        return None
generate_key()
load_key()    
    
