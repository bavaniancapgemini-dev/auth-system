from database import add_user, get_users, update_password, delete_user
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
        print("4. View Profile")
        print("5. Change Password")
        print("6. Delete Account")
        
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
        
    elif choice == "4":

        if current_user:

            print("\n--- User Profile ---")

            print(f"Username: {current_user}")

        else:

            print("Please login first.")
            
    elif choice == "5":

        if current_user:

            users = get_users()

            current_password = getpass("Current Password: ")

            if login(current_user, current_password):

                new_password = getpass("New Password: ")

                confirm_password = getpass("Confirm New Password: ")

                if new_password != confirm_password:

                    print("Passwords do not match.")

                elif valid_password(new_password):

                    update_password(current_user, new_password)

                    print("Password changed successfully.")

                else:

                    print(
                        "Password must be at least 6 characters "
                        "and contain at least one letter and one number"
                    )

            else:

                print("Current password is incorrect.")
                
    elif choice == "6":

        if current_user:

            current_password = getpass("Enter your current password: ")

            if login(current_user, current_password):

                confirmation = input(
                    "Are you sure you want to delete your account? (yes/no): "
                )

                if confirmation.lower() == "yes":

                    delete_user(current_user)

                    current_user = None

                    print("Account deleted successfully.")

                else:

                    print("Account deletion cancelled.")

            else:

                print("Incorrect password. Account was not deleted.")

    else:

        print("Invalid Choice")
