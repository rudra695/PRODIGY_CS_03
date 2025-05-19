import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    # Strength meter
    if strength == 5:
        status = "Strong"
    elif 3 <= strength < 5:
        status = "Moderate"
    else:
        status = "Weak"

    return status, feedback

# === USAGE ===
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, messages = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if messages:
        print("Suggestions to improve your password:")
        for msg in messages:
            print(" -", msg)
    else:
        print("Your password is strong! ✅")
