from database import add_user, get_users
from validation import username_exists, valid_password, valid_username
from auth import login
from utils import title
from getpass import getpass
import validation

while True:

    title()

    print("1. Register")
    print("2. Login")
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

            if valid_password(password):

                add_user(username, password)

                print("Registration Successful")

            else:

                print(
                    "Password must be at least 6 characters "
                    "and contain at least one letter and one number"
                )

    elif choice == "2":

        username = input("Username: ")

        password = getpass("Password: ")

        if login(username, password):
            
            print("Login Successful")
            
        else:
            
            print("Invalid username or password")

    elif choice == "3":

        break


    else:

        print("Invalid Choice")
