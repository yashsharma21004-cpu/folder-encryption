import os
from cryptography.fernet import Fernet

with open("key.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)
user_home = os.path.expanduser('~')
target_folder = os.path.join(user_home, 'testing_folder')

if os.path.exists(target_folder):
    for filename in os.listdir(target_folder):
        if filename == "key.key" or filename.endswith(".py"):
            continue
        file_path = os.path.join(target_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                data = file.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as file:
                file.write(decrypted_data)
            print(f"Unlocked: {filename}")
    print("Success: All files in 'yash_proj' are now decrypted.")
else:
    print(f"Folder not found at: {target_folder}")
