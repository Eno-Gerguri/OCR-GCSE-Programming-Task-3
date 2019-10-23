import sqlite3


class Login_System_Database_Manager:
    """
    This class manages everything to do with the "users.db" database.
    """

    # ==================================================================================================================
    # ==================================================================================================================

    def __init__(self, conn_users, cur_users):
        """
        Creates SQL tables if they do not exist.
        """

        with conn_users:
            cur_users.execute("CREATE TABLE IF NOT EXISTS users(usernames TEXT, passwords TEXT, email_address TEXT)")

    # ==================================================================================================================
    # ==================================================================================================================

    def enter_account_details(self, conn_users, cur_users, username, password, email_address):

        with conn_users:
            cur_users.execute("INSERT INTO users (usernames, passwords, email_address) VALUES (?, ?, ?)",
                              (username, password, email_address))

    # ==================================================================================================================
    # ==================================================================================================================

    def check_if_username_exists(self, conn_users, cur_users, username):
        """
        Checks if the username is in the list. Returns, "True" if it is and, "False" if it is not.
        :param username: STRING
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :return: BOOLEAN
        """

        with conn_users:
            cur_users.execute("SELECT * FROM users")

            for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
                if tuple_line[0] == username:  # tuple[0] gives the first value in the database, which is the username
                    return True, tuple_line  # tuple_line is only used when logging the player in
                    # Return the tuple line and it being true for the password check to detect if it is the same user
                    # This is as the username and password will be in the same tuple in the SQL Database

        return False, None  # Returns "None" as we need the return in a tuple format

    # ==================================================================================================================
    # ==================================================================================================================

    def check_if_password_exists(self, conn_users, cur_users, password, username_tuple):
        """
        Checks if the password is in the list. Returns, "True" if it is and, "False" if it is not.
        Takes in the username_tuple to check if we are checking the password for the correct user
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :param password: STRING
        :param username_tuple: INT
        :return: BOOLEAN
        """

        with conn_users:
            cur_users.execute("SELECT * FROM users")

            for i, _ in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple

                if username_tuple[1] == password:  # tuple[1] gives the second value in the tuple, which is the password
                    # We use the username_tuple as we need to make sure it is the same username
                    # This is so users can have the same passwords but cannot have the same usernames
                    return True

            return False

    # ==================================================================================================================
    # ==================================================================================================================

    def check_if_email_address_exists(self, email_address):
        pass
