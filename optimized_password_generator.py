import secrets
import string
from typing import Set

class PasswordGenerator:
    """Optimized password generator with improved performance and security."""
    
    def __init__(self):
        # Pre-compute character sets for better performance
        self.char_sets = {
            'upper': string.ascii_uppercase,
            'lower': string.ascii_lowercase, 
            'digits': string.digits,
            'special': string.punctuation
        }
    
    def generate_password(self, length: int, char_types: Set[str]) -> str:
        """
        Generate a secure password using cryptographically secure random generator.
        
        Args:
            length: Desired password length
            char_types: Set of character types to include ('upper', 'lower', 'digits', 'special')
        
        Returns:
            Generated password string
        """
        if length <= 0:
            raise ValueError("Password length must be positive")
        
        if not char_types:
            raise ValueError("At least one character type must be selected")
        
        # Build character pool efficiently
        character_pool = ''.join(self.char_sets[char_type] 
                                for char_type in char_types 
                                if char_type in self.char_sets)
        
        if not character_pool:
            raise ValueError("Invalid character types provided")
        
        # Use secrets module for cryptographically secure randomness
        # More efficient than random.choice() in a loop
        return ''.join(secrets.choice(character_pool) for _ in range(length))
    
    def generate_multiple_passwords(self, count: int, length: int, char_types: Set[str]) -> list:
        """Generate multiple passwords efficiently."""
        return [self.generate_password(length, char_types) for _ in range(count)]

def get_user_preferences():
    """Get user preferences with input validation."""
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError("Length must be positive")
        
        char_types = set()
        if input("Include uppercase letters? (y/n): ").lower().startswith('y'):
            char_types.add('upper')
        if input("Include lowercase letters? (y/n): ").lower().startswith('y'):
            char_types.add('lower')
        if input("Include numbers? (y/n): ").lower().startswith('y'):
            char_types.add('digits')
        if input("Include special characters? (y/n): ").lower().startswith('y'):
            char_types.add('special')
        
        return length, char_types
    
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

def main():
    """Main program with error handling and multiple password generation option."""
    print("=== Optimized Password Generator ===")
    
    generator = PasswordGenerator()
    
    try:
        length, char_types = get_user_preferences()
        
        # Option to generate multiple passwords
        count_input = input("How many passwords to generate (default 1): ").strip()
        count = int(count_input) if count_input else 1
        
        if count == 1:
            password = generator.generate_password(length, char_types)
            print(f"\nGenerated Password: {password}")
        else:
            passwords = generator.generate_multiple_passwords(count, length, char_types)
            print(f"\nGenerated {count} Passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i:2d}: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()