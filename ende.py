from cryptography.fernet import Fernet
import os

SECRET_FILE = "secret"
KEY_FILE = "key"

action = input("You want to encrypt or decrypt? YES for encrypt, NO for decrypt, else for exit\nFor Decryption your secret and key should be exist here ")
if action == "YES":
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    secret_text = input("Enter the secret to encrypt: ").encode()
    encrypted = fernet.encrypt(secret_text)
    with open(SECRET_FILE, "wb") as f:
        f.write(encrypted)
    print(f"Secret encrypted and saved to {SECRET_FILE}.")

elif action == "NO":
    if not os.path.exists(KEY_FILE) or not os.path.exists(SECRET_FILE):
        print("Key or secret file missing. Cannot decrypt!")
        exit(1)
    with open(KEY_FILE, "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    with open(SECRET_FILE, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    print("Decrypted secret: ", decrypted.decode())
else:
    exit(0)
