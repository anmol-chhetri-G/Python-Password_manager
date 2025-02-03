import random
import string

# Function to generate a strong random password
def generate_password(length=12):
    if length < 8:  # Ensure minimum length for security
        print("Password length should be at least 8 characters.")
        return None

    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char in string.punctuation for char in password)):
            return password

# Function to save the password securely
def save_password(service, username, password, email):
    if not service or not username or not password or not email:
        print("Input Error: Please enter all fields.")
        return

    try:
        # Save the password details to a file
        with open("passwords.txt", "a") as f:
            f.write(f"Service: {service}\nUsername: {username}\nPassword: {password}\nEmail: {email}\n\n")
        print("Password saved successfully!")
    except Exception as e:
        print(f"Error saving password: {e}")

# Function to display saved passwords
def display_saved_passwords():
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.read()
            if passwords.strip():
                print("Stored Passwords:\n")
                print(passwords)
            else:
                print("No passwords stored.")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"Error reading passwords: {e}")

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter desired password length (minimum 8): "))
    password = generate_password(password_length)
    
    if password:  # Only save if a valid password was generated
        save_password("Service1", "user1", password, "user1@example.com")
    
    # Optionally display saved passwords
    display_saved_passwords()
