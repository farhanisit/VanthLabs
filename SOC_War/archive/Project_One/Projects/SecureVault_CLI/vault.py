  
# IMPORTS
					
import os
import json
import base64
import getpass

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Constants
VAULT_FILE = "vault.json"
SALT = b"vanth-secret-salt"  # Static salt (okay for now; will improve later)


# KEY DERIVATION FUNCTION

def derive_key(password: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def load_vault():
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    return {}

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f)



# VAULT INITIALIZATION

def init_vault():
    if os.path.exists(VAULT_FILE):
        print("Vault already exists.")
        return

    password = getpass.getpass("Set your master password: ")
    key = derive_key(password)

    empty_data = {}
    with open(VAULT_FILE, "w") as f:
        json.dump(empty_data, f)

    print("🔐 Vault initialized. Ready to store secrets.")


from cryptography.fernet import Fernet

# add-entry function
def add_entry():
    password = getpass.getpass("Enter master password: ")
    key = derive_key(password)
    fernet = Fernet(key)

    label = input("Label for the secret (e.g. gmail): ").strip()
    secret = getpass.getpass("Enter the secret: ").strip()

    encrypted = fernet.encrypt(secret.encode()).decode()

    vault = load_vault()
    vault[label] = encrypted
    save_vault(vault)

    print(f"✅ Secret stored under label: '{label}'")

def view_entry():
    password = getpass.getpass("Enter master password: ")
    key = derive_key(password)
    fernet = Fernet(key)

    vault = load_vault()

    label = input("Which label do you want to view? ").strip()

    if label not in vault:
        print("❌ Label not found in vault.")
        return

    encrypted = vault[label]
    try:
        decrypted = fernet.decrypt(encrypted.encode()).decode()
        print(f"🔓 Secret for '{label}': {decrypted}")
    except Exception as e:
        print("⚠️ Failed to decrypt. Wrong password?")


def list_labels():
    vault = load_vault()
    
    if not vault:
        print("📭 Vault is empty.")
        return

    print("📚 Stored Labels:")
    for label in vault.keys():
        print(f"• {label}")


# CLI ENTRY POINT


if __name__ == "__main__":
    print("🧠 Secure Vault CLI")
    print("1. Init Vault")
    print("2. Add Secret")
    print("3. View Secret")
    print("4. List Labels")
    choice = input("Select option: ")

    if choice == "1":
        init_vault()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        view_entry()
    elif choice == "4":
        list_labels()

