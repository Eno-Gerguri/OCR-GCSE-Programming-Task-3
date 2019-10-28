from cryptography.fernet import Fernet

key = b'OpCateaps-CgcH-lyx0s1XX_QTg51mdT9hIFzMR2iwU='  # Holds key that is used to safely secure the details of a user
# Generated with, "Fernet.generate_key()" so you can secure it by yourself
# DO NOT share the key with others you do not trust as the same key is used to both encrypt and decrypt user information
global fer  # Global fer because it will be used in multiple functions
fer = Fernet(key)  # Generate the Fernet using the key


class Login_System_Database_Manager:
    """
    This class manages everything to do with the "users.db" database.
    """

    # ==================================================================================================================
    # ==================================================================================================================

    def __init__(self, conn_users, cur_users):
        """
        Creates SQL, "usernames_and_passwords" database if it does not exist.
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :return: NONE
        """

        with conn_users:
            cur_users.execute("CREATE TABLE IF NOT EXISTS users(usernames TEXT, passwords TEXT, email_address TEXT)")

    # ==================================================================================================================
    # ==================================================================================================================

    def enter_account_details(self, conn_users, cur_users, username, password, email_address):
        """
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :param username: STRING
        :param password: STRING
        :param email_address: STRING
        :return: NONE
        """

        encrypted_username = fer.encrypt(username.encode())
        encrypted_password = fer.encrypt(password.encode())
        encrypted_email_address = fer.encrypt(email_address.encode())

        with conn_users:
            cur_users.execute("INSERT INTO users (usernames, passwords, email_address) VALUES (?, ?, ?)",
                              (encrypted_username, encrypted_password, encrypted_email_address))

    # ==================================================================================================================
    # ==================================================================================================================

    def check_if_username_exists(self, conn_users, cur_users, username):
        """
        Checks if the username is in the list. Returns, "True" if it is and, "False" if it is not.
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :param username: STRING
        :return: BOOLEAN
        """

        with conn_users:
            cur_users.execute("SELECT * FROM users")

            for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
                if (fer.decrypt(tuple_line[0])).decode() == username:
                    # tuple[0] gives the first value in the database, which is the username
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

                if (fer.decrypt(username_tuple[1])).decode() == password:
                    # tuple[1] gives the second value in the tuple, which is the password
                    # We use the username_tuple as we need to make sure it is the same username
                    # This is so users can have the same passwords but cannot have the same usernames
                    print("\n\n")
                    return True

            return False

    # ==================================================================================================================
    # ==================================================================================================================

    def check_if_email_address_exists(self, email_address):
        pass
