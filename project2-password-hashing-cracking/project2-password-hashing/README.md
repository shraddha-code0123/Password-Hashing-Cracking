# Password Cracking and Hashing Algorithms

A hands-on exploration of how passwords are hashed, why **salting** matters, and how dictionary and brute-force attacks actually work — built entirely from scratch in Python to understand the mechanics, not just to run someone else's tool.

> ⚠️ **Ethics & Scope:** Every "attack" in this project targets a password hash generated **inside the same script, by the script itself** — there is no real victim, account, or external system involved anywhere in this code. Never run cracking tools against accounts, systems, or hashes you don't own or don't have explicit written authorization to test. Unauthorized access attempts are illegal in most jurisdictions regardless of intent.

## Objective

Analyze and implement brute-force/dictionary password cracking techniques while understanding hash functions and salting, to internalize *why* certain password practices (length, uniqueness, salting) actually matter from a defender's perspective.

## Project Structure

```
project2-password-hashing/
├── hashing_basics.py       # Salted vs unsalted hashing + verification
├── dictionary_attack.py    # Cracks a self-generated hash using a wordlist
├── brute_force_attack.py   # Cracks a self-generated hash by trying all combinations
├── wordlist.txt            # Small list of common passwords for the demo
├── main.py                 # Interactive menu tying it all together
├── requirements.txt
└── README.md
```

## How to Run

No external dependencies — pure Python standard library.

```bash
python main.py
```

Or run each demo individually:
```bash
python hashing_basics.py
python dictionary_attack.py
python brute_force_attack.py
```

## What Each Script Demonstrates

| Script | Concept | Key Takeaway |
|---|---|---|
| `hashing_basics.py` | Salting | Two users with the *same* password get *identical* hashes if unsalted — a huge leak. A random per-user salt makes identical passwords produce completely different stored hashes. |
| `dictionary_attack.py` | Common-password exploitation | A ~30-word list cracks a common password almost instantly. Real attacker wordlists contain billions of entries from past data breaches. |
| `brute_force_attack.py` | Exhaustive search | Shows the search space growing exponentially with password length (36 possibilities at length 1 → 2.8 trillion at length 8) — the mathematical reason "make your password longer" is the single best piece of password advice. |

## Tools Used
- Python 3 (`hashlib`, `itertools`, `os`, `time`, `string` — all standard library)
- Concepts informed by how real tools like **Hashcat** and **John the Ripper** operate (this project re-implements their core logic for learning purposes; the real tools are far more optimized and support many more hash types)

## Skills Learned
- How password hashing actually works under the hood (and why hashing ≠ encryption)
- Why salting defeats rainbow-table and cross-account pattern attacks
- The real-world time/cost trade-off behind dictionary vs. brute-force attacks
- Why password **length** beats password **complexity** for resisting brute force
- How to verify a login attempt against a stored salted hash, the same way a real authentication system does

## Suggested Next Step
For a production system, you'd use a purpose-built password-hashing algorithm like **bcrypt**, **scrypt**, or **Argon2** instead of plain SHA-256 — these are deliberately slow and have built-in salting, which makes large-scale cracking attempts far more expensive for an attacker. This project uses SHA-256 specifically because it's transparent and easy to learn from; production code should not use raw SHA-256 for password storage.
