
import hashing_basics
import dictionary_attack
import brute_force_attack


def main():
    while True:
        print("\n" + "=" * 60)
        print("PASSWORD CRACKING & HASHING TOOLKIT")
        print("=" * 60)
        print("1. Salted vs Unsalted Hashing Demo")
        print("2. Dictionary Attack Demo")
        print("3. Brute-Force Attack Demo")
        print("4. Hash your own password (SHA-256, with salt)")
        print("5. Exit")
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            run_module(hashing_basics)
        elif choice == "2":
            run_module(dictionary_attack)
        elif choice == "3":
            run_module(brute_force_attack)
        elif choice == "4":
            hash_own_password()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


def run_module(module):
    """Re-run a module's __main__ demo block."""
    import importlib
    importlib.reload(module)


def hash_own_password():
    pw = input("Enter a password to hash securely: ").strip() or "ExamplePass1"
    salt_hex, hash_hex = hashing_basics.hash_password_salted(pw)
    print(f"\nSalt (store this): {salt_hex}")
    print(f"Hash (store this): {hash_hex}")
    print("\nIn a real system, you'd store BOTH the salt and hash in your database")
    print("(never the plain password), then re-hash login attempts with the same")
    print("salt to verify them.")


if __name__ == "__main__":
    main()
