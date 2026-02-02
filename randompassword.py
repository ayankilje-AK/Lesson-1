import random
import string

def generate_random_password(length=12):
    """
    Generates a random password of a specified length using letters and numbers.

    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: A randomly generated password.
    """
    if length < 4:
        print("Warning: Password length should be at least 4 characters for security.")
        length = 4

    # Define the possible characters for the password
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Ensure at least one of each character type is present
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    # Fill the rest of the password length with random choices from all characters
    for _ in range(length - 3):
        password.append(random.choice(characters))

    # Shuffle the list of characters to ensure true randomness
    random.shuffle(password)

    # Join the list of characters into a single string and return it
    return "".join(password)

# --- Example Usage ---
# Generate a password with the default length (12 characters)
password_default = generate_random_password()
print(f"Generated password (default length): {password_default}")

# Generate a password with a specific length (e.g., 16 characters)
password_custom = generate_random_password(length=16)
print(f"Generated password (custom length): {password_custom}")
