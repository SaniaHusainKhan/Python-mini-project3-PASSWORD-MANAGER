Python-mini-project3-PASSWORD-MANAGER
A Python terminal-based password manager that securely stores and retrieves account passwords using Fernet encryption, with simple add and view modes.
🔐 Simple Password Manager (Python + Fernet Encryption)

This is a basic command-line password manager written in Python.  
It uses the **cryptography** library (Fernet) to encrypt and decrypt stored passwords securely.  

Passwords are saved in `passwords.txt`, and an encryption key is stored in `key.key`.

---

⚙️ Features
- Add new account passwords (encrypted)
- View existing account passwords (decrypted)
- Automatically generates a key file if not present
- Secure storage using **Fernet symmetric encryption**

---

🚀 How to Run
1. Clone this repository or download the script.
2. Install dependencies:
   bash
   pip install cryptography
Run the program:

bash
Copy code
python pmr.py
📝 Example Usage
pgsql
Copy code
Would you like to add a new password or view existing ones? (view, add) Or press q to quit: add
Account Name: Gmail
Password: mySuperSecret123

Would you like to add a new password or view existing ones? (view, add) Or press q to quit: view
User: Gmail | Password: mySuperSecret123
