import os
from cryptography.fernet import Fernet

def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("New key generated and saved as key.key")
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                try:
                    print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
                except Exception:
                    print(f"Could not decrypt password for {user}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("\nWould you like to add a new password or view existing ones? (view, add) Or press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
