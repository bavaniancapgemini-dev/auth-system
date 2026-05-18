import sqlite3


connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    username TEXT,
    password TEXT

)
""")

connection.commit()

connection.close()

def add_user(username, password):

    connection = sqlite3.connect("users.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (username, password)
    )

    connection.commit()

    connection.close()

def get_users():

    connection = sqlite3.connect("users.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    connection.close()

    return users

