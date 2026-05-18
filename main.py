from database import add_user, get_users
from validation import username_exists
from auth import login
from utils import title


while True:

    title()

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")


    if choice == "1":

        users = get_users()

        username = input("Username: ")

        if username_exists(users, username):

            print("Username already exists")

        else:

            password = input("Password: ")

            add_user(username, password)

            print("Registration Successful")


    elif choice == "2":

        username = input("Username: ")

        password = input("Password: ")

        if login(username, password):

            print("Login Successful")

        else:

            print("Invalid Credentials")


    elif choice == "3":

        break


    else:

        print("Invalid Choice")