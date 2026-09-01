from database import add_user, get_users
from validation import username_exists, valid_password, valid_username
from auth import login
from utils import title
from getpass import getpass
import validation

current_user = None

while True:

    title()

    print("1. Register")
    print("2. Login")
    
    if current_user:
        
        print("3. Logout")
        
    else:
        
        print("3. Exit")

    choice = input("Choose: ")


    if choice == "1":

        users = get_users()

        username = input("Username: ")

        if not valid_username(username):

            print(
                "Username must be at least 3 characters "
                "and contain only letters, numbers, or _"
            )

        elif validation.username_exists(users, username):

            print("Username already exists")

        else:

            password = getpass("Password: ")

            confirm_password = getpass("Confirm Password: ")

            if password != confirm_password:

                print("Passwords do not match")

            elif valid_password(password):

                add_user(username, password)

                print("Registration Successful")

            else:

                print(
                    "Password must be at least 6 characters "
                    "and contain at least one letter and one number"
                )
                
    elif choice == "2":

        username = input("Username: ")

        attempts = 0

        while attempts < 3:

            password = getpass("Password: ")

            if login(username, password):

                current_user = username

                print("Login Successful")

                print(f"Welcome, {current_user}!")

                break

            else:

                attempts += 1

                print("Invalid username or password")

                if attempts < 3:

                    print(f"Attempts remaining: {3 - attempts}")

                else:

                    print("Too many failed login attempts.")
                
    elif choice == "3":
        
        if current_user:
            
            current_user = None
            
            print("Logged out successfully.")
            
        else:

            break

    else:

        print("Invalid Choice")
