import sqlite3
username_exists = False
password_exists = False

# ======================================================================================================================
# ======================================================================================================================

def initialise_users_database():
    conn_users = sqlite3.connect("users.db")
    cur_users = conn_users.cursor()

    cur_users.execute("CREATE TABLE IF NOT EXISTS users(usernames TEXT, passwords TEXT)")
    conn_users.commit()

    cur_users.close()
    conn_users.close()


# ======================================================================================================================
# ======================================================================================================================

def create_account(username, password):
    conn_users = sqlite3.connect("users.db")
    cur_users = conn_users.cursor()

    cur_users.execute("INSERT INTO users (usernames, passwords) VALUES (?, ?)",
                      (username, password))
    conn_users.commit()

    cur_users.close()
    conn_users.close()


# ======================================================================================================================
# ======================================================================================================================

def check_if_username_exists(username):
    global username_exists

    conn_users = sqlite3.connect("users.db")
    cur_users = conn_users.cursor()

    cur_users.execute("SELECT * FROM users")

    for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
        if tuple_line[0] == username:  # tuple[0] gives the first value in the database, which is the username
            username_exists = True
            return username_exists

    cur_users.close()
    conn_users.close()


# ======================================================================================================================
# ======================================================================================================================

def check_if_password_exists(password):
    global password_exists

    conn_users = sqlite3.connect("users.db")
    cur_users = conn_users.cursor()

    cur_users.execute("SELECT * FROM users")

    for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
        if tuple_line[1] == password:  # tuple[1] gives the second value in the database, which is the password
            password_exists = True

            if password_exists:
                break

    cur_users.close()
    conn_users.close()


# ======================================================================================================================
# ======================================================================================================================
