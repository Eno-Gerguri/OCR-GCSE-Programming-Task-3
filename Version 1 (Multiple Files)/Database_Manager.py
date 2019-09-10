import sqlite3
from config import user_exists


# ======================================================================================================================
# ======================================================================================================================

def init():
    conn_users = sqlite3.connect("users.db")
    cur_users = conn_users.cursor()


# ======================================================================================================================
# ======================================================================================================================

def initialise_users_database():
    with conn_users:
        cur_users.execute("CREATE TABLE IF NOT EXISTS users(usernames TEXT, passwords TEXT)")


# ======================================================================================================================
# ======================================================================================================================

def add_user(username, password):
    with conn_users:
        cur_users.execute("INSERT INTO users (usernames, passwords) VALUES (?, ?)",
                          (username, password))


# ======================================================================================================================
# ======================================================================================================================

# ======================================================================================================================
# ======================================================================================================================

def check_if_user_exists(username):
    cur_users.execute("SELECT * FROM users")

    for i, tuple_line in enumerate(cur_users.fetchall()):
        if tuple_line[0] == username:
            user_exists = True


# ======================================================================================================================
# ======================================================================================================================

def close():
    cur_users.close()
    conn_users.close()
