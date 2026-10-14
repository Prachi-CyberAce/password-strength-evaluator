"""
Password Strength Evaluator - a beginner cybersecurity project.

Run it:   python password_evaluator.py
Needs:    Python 3.8+ (no extra libraries)

Nothing you type is saved or sent anywhere.
"""

import math
import string
from getpass import getpass  # hides what you type, like real login forms

# A tiny list of very common passwords. Real tools use lists with millions.
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "letmein",
    "admin", "welcome", "iloveyou", "monkey", "dragon", "football",
    "password1", "123456789", "111111", "login", "passw0rd",
}

# Patterns attackers try first.
SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl"]


def estimate_entropy(password):
    """Estimate 'bits of entropy': roughly how hard it is to guess.
    More bits = harder. Formula: length * log2(size of character pool)."""
    pool = 0
    if any(c in string.ascii_lowercase for c in password):
        pool += 26
    if any(c in string.ascii_uppercase for c in password):
        pool += 26
    if any(c in string.digits for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    return len(password) * math.log2(pool) if pool else 0


def has_sequence(password, run=4):
    """Detect runs like 'abcd', '1234', or 'qwer' (forwards or backwards)."""
    p = password.lower()
    for seq in SEQUENCES:
        for i in range(len(seq) - run + 1):
            chunk = seq[i:i + run]
            if chunk in p or chunk[::-1] in p:
                return True
    return False


def has_repeats(password, run=3):
    """Detect things like 'aaa' or '111'."""
    return any(len(set(password[i:i + run])) == 1
               for i in range(len(password) - run + 1))


def evaluate(password):
    """Return (score out of 100, label, list of feedback tips)."""
    tips = []
    score = 0

    # 1. Length matters most.
    n = len(password)
    score += min(n, 16) * 3  # up to 48 points
    if n < 12:
        tips.append("Use at least 12 characters (longer is better).")

    # 2. Character variety.
    checks = [
        (any(c.islower() for c in password), "lowercase letters"),
        (any(c.isupper() for c in password), "uppercase letters"),
        (any(c.isdigit() for c in password), "numbers"),
        (any(c in string.punctuation for c in password), "symbols (!@#$...)"),
    ]
    for present, name in checks:
        if present:
            score += 8  # up to 32 points
        else:
            tips.append(f"Add {name}.")

    # 3. Entropy bonus (up to 20 points).
    bits = estimate_entropy(password)
    score += min(bits / 4, 20)

    # 4. Penalties for known-bad habits.
    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 5)
        tips.insert(0, "This is one of the most common passwords. Attackers try it first!")
    if has_sequence(password):
        score -= 15
        tips.append("Avoid sequences like 'abcd', '1234' or 'qwer'.")
    if has_repeats(password):
        score -= 10
        tips.append("Avoid repeated characters like 'aaa' or '111'.")

    score = max(0, min(100, round(score)))

    if score < 30:
        label = "Very weak"
    elif score < 50:
        label = "Weak"
    elif score < 70:
        label = "Okay"
    elif score < 85:
        label = "Strong"
    else:
        label = "Very strong"

    return score, label, tips, bits


def main():
    print("=== Password Strength Evaluator ===")
    print("Type a password to test (press Enter with nothing to quit).\n")
    while True:
        pw = getpass("Password: ")
        if not pw:
            print("Goodbye!")
            break
        score, label, tips, bits = evaluate(pw)
        bar = "#" * (score // 5) + "-" * (20 - score // 5)
        print(f"\n[{bar}] {score}/100 - {label}")
        print(f"Estimated entropy: {bits:.0f} bits")
        for tip in tips:
            print(f"  - {tip}")
        print()


if __name__ == "__main__":
    main()
