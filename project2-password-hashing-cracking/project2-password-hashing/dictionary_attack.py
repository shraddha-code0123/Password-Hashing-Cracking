

import hashlib
import time


def crack_hash_with_wordlist(target_hash: str, wordlist_path: str, algorithm: str = "sha256"):
    """Try every word in the wordlist file against the target hash.

    Returns the matching password if found, else None.
    """
    with open(wordlist_path, "r") as f:
        candidates = [line.strip() for line in f if line.strip()]

    attempts = 0
    start = time.time()

    for candidate in candidates:
        attempts += 1
        h = hashlib.new(algorithm)
        h.update(candidate.encode())
        if h.hexdigest() == target_hash:
            elapsed = time.time() - start
            return candidate, attempts, elapsed

    elapsed = time.time() - start
    return None, attempts, elapsed


if __name__ == "__main__":
    print("=" * 70)
    print("DICTIONARY ATTACK DEMO (against a self-generated test hash only)")
    print("=" * 70)

    # We create our OWN target password and hash it ourselves, purely
    # so we have something safe and legal to demonstrate cracking.
    secret_password = "password123"
    target_hash = hashlib.sha256(secret_password.encode()).hexdigest()

    print(f"\n[Simulated] A leaked database contains this SHA-256 hash:")
    print(f"  {target_hash}")
    print("\nWe do NOT know the password — only the hash. Let's try to recover")
    print("it using a wordlist of common passwords...\n")

    found, attempts, elapsed = crack_hash_with_wordlist(target_hash, "wordlist.txt")

    if found:
        print(f"SUCCESS! Password found: '{found}'")
        print(f"   Tried {attempts} candidates in {elapsed:.6f} seconds.")
    else:
        print(f"Password not in wordlist. Tried {attempts} candidates in {elapsed:.6f}s.")

    print("\nLesson: this is why security guidance always says 'don't use common")
    print("passwords' — a 30-word list cracked it almost instantly. Real attacker")
    print("wordlists contain BILLIONS of leaked real-world passwords.")
