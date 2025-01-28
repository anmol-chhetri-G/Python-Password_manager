import random
import string

# Function to generate a strong random password
def generate_password(length=12):
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char in string.punctuation for char in password) and
            len(password) >= 8):
            return password

# Function to save the password securely
def save_password(service, username, password, email):
    if not service or not username or not password or not email:
        print("Input Error: Please enter all fields.")
        return

    # Save the password details to a file
    with open("passwords.txt", "a") as f:
        f.write(f"Service: {service}\nUsername: {username}\nPassword: {password}\nEmail: {email}\n\n")

    print("Password saved successfully!")

# Example usage
password = generate_password()
save_password("Service1", "user1", password, "user1@example.com")
