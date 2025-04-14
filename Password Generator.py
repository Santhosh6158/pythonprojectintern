import random
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    # Define character pools
    letters = string.ascii_letters if include_letters else ""
    numbers = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""

    # Combine all selected character pools
    all_characters = letters + numbers + symbols
    if not all_characters:
        return None  # Return None if no character types were selected

    # Generate the password
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    print("Welcome to the Command-Line Password Generator!")
    
    # Get user input
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
        
        include_letters = input("Include letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, include_letters, include_numbers, include_symbols)

        if password:
            print(f"\nYour generated password: {password}")
        else:
            print("Error: No character types selected. Please select at least one type.")
    except ValueError:
        print("Invalid input! Please enter numeric values for password length.")

if __name__ == "__main__":
    main()
