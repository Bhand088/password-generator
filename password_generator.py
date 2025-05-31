import random
import string

def generate_password(length=12, use_symbols=True):
    # Prepare the list of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Add symbols if user wants them
    if use_symbols:
        characters += string.punctuation

    # Randomly pick characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Strong Password Generator\n")

    # Ask user for the desired password length
    while True:
        try:
            length = int(input("Enter password length (at least 6): "))
            if length < 6:
                print("Please choose a length of 6 or more for better security.")
                continue
            break
        except ValueError:
            print("Oops! That doesn't look like a number. Try again.")

    # Ask if user wants symbols included
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_symbols)
    print(f"\nHere is your new password: {password}")
    print("Make sure to keep it safe!")

if __name__ == "__main__":
    main()
