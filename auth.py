from database import get_users


def login(username, password):

    users = get_users()

    for user in users:

        if user[0] == username and user[1] == password:

            return True

    return False