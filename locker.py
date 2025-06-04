import os
import hashlib
import getpass
import shutil
import stat

CONFIG_DIR = 'config'
HASH_FILE = os.path.join(CONFIG_DIR, 'hash.txt')
PROTECTED_FOLDER = 'protected'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    password = getpass.getpass("Set master password: ")
    with open(HASH_FILE, 'w') as f:
        f.write(hash_password(password))
    print("Master password set successfully.\n")

def verify_password():
    if not os.path.exists(HASH_FILE):
        print("No master password found.")
        return False
    password = getpass.getpass("Enter master password: ")
    with open(HASH_FILE, 'r') as f:
        saved_hash = f.read()
    return saved_hash == hash_password(password)

def lock_folder(folder_name):
    source = os.path.join(PROTECTED_FOLDER, folder_name)
    target = os.path.join(PROTECTED_FOLDER, f".{folder_name}")
    if not os.path.exists(source):
        print("❌ Folder not found.")
        return
    if os.path.exists(target):
        print("❌ Folder is already locked.")
        return
    shutil.move(source, target)
    print(f"✅ Folder '{folder_name}' locked successfully.")

def unlock_folder(folder_name):
    source = os.path.join(PROTECTED_FOLDER, f".{folder_name}")
    target = os.path.join(PROTECTED_FOLDER, folder_name)
    if not os.path.exists(source):
        print("❌ Locked folder not found.")
        return
    shutil.move(source, target)
    print(f"✅ Folder '{folder_name}' unlocked successfully.")

def main():
    if not os.path.exists(HASH_FILE):
        set_master_password()

    print("\n==== FILE LOCKER ====")
    print("1. Lock Folder")
    print("2. Unlock Folder")
    choice = input("Enter your choice: ")

    folder_name = input("Enter the folder name inside 'protected/' to target: ")

    if verify_password():
        if choice == '1':
            lock_folder(folder_name)
        elif choice == '2':
            unlock_folder(folder_name)
        else:
            print("❌ Invalid choice.")
    else:
        print("❌ Wrong password!")

if __name__ == '__main__':
    main()
