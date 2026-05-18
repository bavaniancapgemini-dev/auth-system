def username_exists(users, username):

    for user in users:

        if user[0] == username:

            return True

    return False