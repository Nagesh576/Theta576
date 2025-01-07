def validate_password(password):
    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        # Check if the password contains a digit
        if any(char.isdigit() for char in password):
            # Check if the password contains a letter
            if any(char.isalpha() for char in password):
                # Check if the password contains a special character
                if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
                    print("Password is valid.")
                else:
                    print("Password is invalid. It must contain at least one special character.")
            else:
                print("Password is invalid. It must contain at least one letter.")
        else:
            print("Password is invalid. It must contain at least one digit.")
    else:
        print("Password is invalid. It must be at least 8 characters long.")
# Input password
password = input("Enter your password: ")
# Validate the password
validate_password(password)