

import hashlib
import itertools
import string
import time


def brute_force_crack(target_hash: str, charset: str, max_length: int, algorithm: str = "sha256"):
    """Try every possible combination of `charset` up to `max_length`."""
    attempts = 0
    start = time.time()

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            attempts += 1
            candidate = "".join(combo)
            h = hashlib.new(algorithm)
            h.update(candidate.encode())
            if h.hexdigest() == target_hash:
                elapsed = time.time() - start
                return candidate, attempts, elapsed

    elapsed = time.time() - start
    return None, attempts, elapsed


if __name__ == "__main__":
    print("=" * 70)
    print("BRUTE-FORCE ATTACK DEMO (against a self-generated test hash only)")
    print("=" * 70)

    secret_password = "ab9"          # intentionally short for a fast demo
    charset = string.ascii_lowercase + string.digits   # a-z and 0-9
    max_length = 4

    target_hash = hashlib.sha256(secret_password.encode()).hexdigest()

    print(f"\nTarget hash (SHA-256): {target_hash}")
    print(f"Character set: a-z, 0-9 ({len(charset)} characters)")
    print(f"Trying every combination up to {max_length} characters long...\n")

    found, attempts, elapsed = brute_force_crack(target_hash, charset, max_length)

    if found:
        print(f"SUCCESS! Password found: '{found}'")
        print(f"   Tried {attempts:,} combinations in {elapsed:.4f} seconds")
        print(f"   ({attempts/elapsed:,.0f} attempts/second on this single CPU thread)")
    else:
        print(f"Not found within {max_length} characters. Tried {attempts:,} combinations.")

    print("\n--- Why password LENGTH matters more than you'd think ---")
    for length in range(1, 9):
        space = len(charset) ** length
        print(f"  Length {length}: {space:,} possible passwords")

    print("\nLesson: the search space grows EXPONENTIALLY with length. A 3-character")
    print("password might crack in milliseconds; an 8+ character password with")
    print("mixed case, numbers, and symbols can take attackers years on the same hardware.")
