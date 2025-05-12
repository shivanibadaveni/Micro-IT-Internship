import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the program
if __name__ == "__main__":
    main()
