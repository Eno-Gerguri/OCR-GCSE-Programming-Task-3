from random import shuffle
import sqlite3


# ======================================================================================================================
# ======================================================================================================================
# Initialise Deck

class Card:
    """
    This class Initialises the deck and all of the cards within it.
    """

    def __init__(self, card_number, card_colour):
        self.card_number = card_number
        self.card_colour = card_colour


red_card_1 = Card(1, "red")
red_card_2 = Card(2, "red")
red_card_3 = Card(3, "red")
red_card_4 = Card(4, "red")
red_card_5 = Card(5, "red")
red_card_6 = Card(6, "red")
red_card_7 = Card(7, "red")
red_card_8 = Card(8, "red")
red_card_9 = Card(9, "red")
red_card_10 = Card(10, "red")
black_card_1 = Card(1, "black")
black_card_2 = Card(2, "black")
black_card_3 = Card(3, "black")
black_card_4 = Card(4, "black")
black_card_5 = Card(5, "black")
black_card_6 = Card(6, "black")
black_card_7 = Card(7, "black")
black_card_8 = Card(8, "black")
black_card_9 = Card(9, "black")
black_card_10 = Card(10, "black")
yellow_card_1 = Card(1, "yellow")
yellow_card_2 = Card(2, "yellow")
yellow_card_3 = Card(3, "yellow")
yellow_card_4 = Card(4, "yellow")
yellow_card_5 = Card(5, "yellow")
yellow_card_6 = Card(6, "yellow")
yellow_card_7 = Card(7, "yellow")
yellow_card_8 = Card(8, "yellow")
yellow_card_9 = Card(9, "yellow")
yellow_card_10 = Card(10, "yellow")

deck = [red_card_1, red_card_2, red_card_3, red_card_4, red_card_5,
        red_card_6, red_card_7, red_card_8, red_card_9, red_card_10,

        black_card_1, black_card_2, black_card_3, black_card_4, black_card_5,
        black_card_6, black_card_7, black_card_8, black_card_9, black_card_10,

        yellow_card_1, yellow_card_2, yellow_card_3, yellow_card_4, yellow_card_5,
        yellow_card_6, yellow_card_7, yellow_card_8, yellow_card_9, yellow_card_10]


# ======================================================================================================================
# ======================================================================================================================
# Manages Everything to do with the SQL Database

conn_users = sqlite3.connect("users.db")
cur_users = conn_users.cursor()


class Database_Manager:
    """
    This class manages everything to do with the SQL Databases.
    """

    def __init__(self):
        """
        Creates SQL tables if they do not exist.
        """

        with conn_users:
            cur_users.execute("CREATE TABLE IF NOT EXISTS users(usernames TEXT, passwords TEXT)")

    def create_account(self, username, password):
        pass

    def check_if_username_exists(self, username):
        """
        Checks if the username is in the list. Returns, "True" if it is and, "False" if it is not.
        :param username: STRING
        :return: BOOLEAN
        """

        with conn_users:
            cur_users.execute("SELECT * FROM users")

            for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
                if tuple_line[0] == username:  # tuple[0] gives the first value in the database, which is the username
                    return True, tuple_line
                    # Return the tuple line and it being true for the password check to detect if it is the same user
                    # This is as the username and password will be on in the same tuple in the SQL Database

            return False, None  # Returns "None" as we need the return in a tuple format

    def check_if_password_exists(self, password, username_tuple):
        """
        Checks if the password is in the list. Returns, "True" if it is and, "False" if it is not.
        :param password: STRING
        :param username_tuple: INT
        :return: BOOLEAN
        """

        with conn_users:
            cur_users.execute("SELECT * FROM users")

            for i, tuple_line in enumerate(cur_users.fetchall()):  # Each record in the database comes in a tuple
                if username_tuple[1] == password:  # tuple[1] gives the second value in the tuple, which is the password
                    # We use the username_tuple as we need to make sure it is the same username
                    # This is so users can have the same passwords but cannot have the same usernames
                    return True

            return False


# ======================================================================================================================
# ======================================================================================================================

class Authenticate_User(Database_Manager):

    def starting_page(self, player_logging_in):
        """
        Is the first page that opens when the program is run. Returns a string, "login" or "createanaccount" depending
        on what they typed in.
        :param player_logging_in: STRING
        :return: STRING
        """

        print("Welcome, Player " + player_logging_in + "\n\n")  # Prints title to show user which user is logging in
        option_picked = input("Log In\n\nCreate an Account\n\n")  # Gets the option from user input
        print("\n\n")

        if option_picked.lower().strip().replace(" ", "") == "login":
            return option_picked.lower().strip().replace(" ", "")  # Returns "login"

        elif option_picked.lower().strip().replace(" ", "") == "createanaccount":
            return option_picked.lower().strip().replace(" ", "")  # Returns "createanaccount"

        else:
            print("\n\nSorry that is invalid. Please check your spelling.\n\n")
            return False  # If the input is not an option it returns False

    def login_in_players(self, player_logging_in):
        """
        Logs Player 1 and 2 into the game by checking if their typed username and password exists from an SQL Database.
        :param player_logging_in: STRING
        :return: BOOLEAN
        """

        print("Login Page\n")
        print("Player " + player_logging_in + ":\n\n")  # Prints title to show user which user is logging in
        entered_username = input("Enter your Username: ")

        if Database_Manager.check_if_username_exists(self, entered_username)[0]:
            username_tuple = Database_Manager.check_if_username_exists(self, entered_username)[1]

            entered_password = input("Enter your Password: ")

            if Database_Manager.check_if_password_exists(self, entered_password, username_tuple):
                return True

            else:
                print("\n\nSorry that Password is incorrect. Please check your spelling.\n\n")
                return False

        else:
            print("\n\nSorry that Username does not exist. Please check your spelling.\n\n")
            return False


# ======================================================================================================================
# ======================================================================================================================
# Initialisation

Authenticate_User = Authenticate_User()


# ======================================================================================================================
# ======================================================================================================================
# Main Loop

logged_in_users = False

while logged_in_users is False:
    if Authenticate_User.starting_page("1") == "login":

        if Authenticate_User.login_in_players("1"):

            if Authenticate_User.starting_page("2") == "login":

                if Authenticate_User.login_in_players("2"):
                    pass
                    # Start the game menu

            elif Authenticate_User.starting_page("2") == "createanaccount":
                pass

    elif Authenticate_User.starting_page("1") == "createanaccount":
        pass


# ======================================================================================================================
# ======================================================================================================================

cur_users.close()
conn_users.close()


