

import hashlib
import os


def hash_password_unsalted(password: str, algorithm: str = "sha256") -> str:
    """Hash a password with no salt — INSECURE, shown for comparison only."""
    h = hashlib.new(algorithm)
    h.update(password.encode())
    return h.hexdigest()


def hash_password_salted(password: str, salt: bytes = None, algorithm: str = "sha256") -> tuple[str, str]:
    """Hash a password WITH a random salt — the secure approach.

    Returns (salt_hex, hash_hex). Both must be stored in the database
    so the same salt can be used to verify a login attempt later.
    """
    if salt is None:
        salt = os.urandom(16)  # 16 random bytes, unique per user
    h = hashlib.new(algorithm)
    h.update(salt + password.encode())
    return salt.hex(), h.hexdigest()


def verify_salted_password(password_attempt: str, salt_hex: str, stored_hash: str, algorithm: str = "sha256") -> bool:
    """Check a login attempt against a stored salted hash."""
    salt = bytes.fromhex(salt_hex)
    _, computed_hash = hash_password_salted(password_attempt, salt=salt, algorithm=algorithm)
    return computed_hash == stored_hash


if __name__ == "__main__":
    print("=" * 70)
    print("SALTED vs UNSALTED HASHING DEMO")
    print("=" * 70)

    password = "Password123"

    print(f"\nTwo different users both choose the password: '{password}'")

    print("\n--- WITHOUT salting (insecure) ---")
    h1 = hash_password_unsalted(password)
    h2 = hash_password_unsalted(password)
    print(f"User A's hash: {h1}")
    print(f"User B's hash: {h2}")
    print(f"Identical hashes? {h1 == h2}  <-- This leaks that they share a password!")

    print("\n--- WITH salting (secure) ---")
    salt_a, hash_a = hash_password_salted(password)
    salt_b, hash_b = hash_password_salted(password)
    print(f"User A: salt={salt_a[:16]}...  hash={hash_a}")
    print(f"User B: salt={salt_b[:16]}...  hash={hash_b}")
    print(f"Identical hashes? {hash_a == hash_b}  <-- Same password, but hashes look totally different!")

    print("\n--- Verifying a correct login attempt ---")
    is_valid = verify_salted_password("Password123", salt_a, hash_a)
    print(f"Login with correct password: {is_valid}")

    print("\n--- Verifying an incorrect login attempt ---")
    is_valid = verify_salted_password("WrongPassword", salt_a, hash_a)
    print(f"Login with wrong password: {is_valid}")
