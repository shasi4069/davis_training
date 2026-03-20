Username = "admin" # Username for login
Password = "1234" # Password for login

# Login attempt counter
i = 1

# Login attempt loop
while i <= 3:
    username_input = input("Enter username: ")  # Get username input
    password_input = input("Enter password: ")  # Get password input

    # Check credentials
    if username_input == Username and password_input == Password:
        print("Login Successful!")
        break
    else:
        print(f"Login failed. {3 - i} attempts remaining.")
    i += 1

# Check if login attempts exceeded
if(i > 3):
    print("Account locked, after 3 failures.")