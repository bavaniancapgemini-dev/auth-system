def username_exists(users, username):

    for user in users:

        if user[0] == username:

            return True

    return False

def valid_password(password):

    if len(password) < 6:

        return False

    has_letter = False

    has_number = False

    for character in password:

        if character.isalpha():

            has_letter = True

        if character.isdigit():

            has_number = True

    if has_letter and has_number:

        return True

    return False

def valid_username(username):

    if len(username) < 3:

        return False

    if not username.replace("_", "").isalnum():

        return False

    return True