import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets for the password
    characters = string.ascii_letters  # Alphabetic characters (uppercase and lowercase)
    
    if use_digits:
        characters += string.digits  # Include digits (0-9)
    
    if use_special_chars:
        characters += string.punctuation  # Include special characters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits (yes/no)? ").lower() == "yes"
    include_special_chars = input("Include special characters (yes/no)? ").lower() == "yes"

    password = generate_password(password_length, include_digits, include_special_chars)
    print("Generated Password:", password)
