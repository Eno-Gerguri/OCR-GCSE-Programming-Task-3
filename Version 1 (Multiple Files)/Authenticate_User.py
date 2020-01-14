from Database_Manager import Login_System_Database_Manager
from validate_email import validate_email
from getpass import getpass


class Authenticate_User(Login_System_Database_Manager):
    """
    This class manages how the user is logged in.
    """

    # ==================================================================================================================
    # ==================================================================================================================

    @staticmethod
    def starting_page(player_logging_in):
        """
        Is the first page that opens when the program is run. Returns a string, "login" or "createanaccount" depending
        on what they typed in.
        :param player_logging_in: STRING
        :return: STRING or BOOLEAN
        """

        print(f"Welcome, Player {player_logging_in}\n\n")  # Prints title to show user which user is logging in
        option_picked = input("Log In\n\nCreate an Account\n\n")  # Gets the option from user input
        print("\n\n")

        if option_picked.lower().strip().replace(" ", "") == "login":
            return option_picked.lower().strip().replace(" ", "")  # Returns "login"

        elif option_picked.lower().strip().replace(" ", "") == "createanaccount":
            return option_picked.lower().strip().replace(" ", "")  # Returns "createanaccount"

        else:
            print("\n\nSorry that is invalid. Please check your spelling.\n\n")
            return False  # If the input is not an option it returns False

    # ==================================================================================================================
    # ==================================================================================================================

    def login_in_players(self, conn_users, cur_users, player_logging_in):
        """
        Logs Player 1 and 2 into the game by checking if their typed username and password exists from an SQL Database.
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :param player_logging_in: STRING
        :return: BOOLEAN
        """

        print("Login Page\n")
        print(f"Player {player_logging_in}:\n\n")  # Prints title to show user which user is logging in
        entered_username = input("Enter your Username: ")

        username_exists = Login_System_Database_Manager.check_if_username_exists(self, conn_users, cur_users,
                                                                                 entered_username)
        # 'username_exists' takes up more memory but reduces amount of calculations done in 'check_if_username_exists'

        if username_exists[0]:
            # The second value that is returned is either NONE or "tuple_line" variable

            entered_password = getpass("Enter your Password: ")  # Will not be able to see the password they are typing

            if Login_System_Database_Manager.check_if_password_exists(self, conn_users, cur_users, entered_password,
                                                                      username_exists[1]):

                return True

            else:
                print("\n\nSorry that Password is incorrect. Please check your spelling.\n\n")
                return False

        else:
            print("\n\nSorry that Username does not exist. Please check your spelling.\n\n")
            return False

    # ==================================================================================================================
    # ==================================================================================================================

    def create_player_account(self, conn_users, cur_users):
        """
        Creates the user an account by asking them for a: username, password and email address(optional)
        :param conn_users: SQL CONNECTION
        :param cur_users: SQL CURSOR
        :return: NONE
        """

        print("Create Account Page\n")
        new_username = input("Please enter a Username: ")

        if Login_System_Database_Manager(conn_users, cur_users).check_if_username_exists(conn_users, cur_users,
                                                                                         new_username)[0] is not True:
            # If username is not taken

            new_password = getpass("Please enter your Password: ")
            new_password_check = getpass("Please Re-enter your Password: ")

            if new_password == new_password_check:  # If the passwords match
                new_email_address = input("Please enter your Email Address (optional, hit, 'Enter'): ")
                # Gets email address

                if not validate_email(new_email_address):  # If it is not a valid email address
                    new_email_address = "None"

                print("\nThank you for entering your details!\n")

                # Creates the, "corrected" variables, which will be the final variables passed into
                # the, "enter_account_details" database function
                corrected_username = new_username
                corrected_password = new_password
                corrected_email_address = new_email_address
                # This makes them easier to modify if the user miss typed their details

                while 1:  # Quicker than using the, "True" keyword

                    check_for_details = input("Are these details correct?:\n\n"
                                              f"Username: {corrected_username}"
                                              f"\nPassword: {'*' * len(corrected_password)}"
                                              f"\nEmail Address: {corrected_email_address}\n\n")
                    # Asks user if their details are correct

                    if check_for_details.strip().lower().replace(" ", "") == "yes":  # If details are correct
                        Login_System_Database_Manager(conn_users, cur_users).enter_account_details\
                            (conn_users, cur_users, corrected_username,
                             corrected_password,
                             corrected_email_address)

                        print("\n\nSuccessfully created account!\n\n")
                        return

                    else:
                        incorrect_detail = input("\n\nWhich detail is incorrect?\n\nusername\npassword"
                                                 "\nemail address\n\n")  # Gets the incorrect detail
                        print("\n")

                        # Gets the correct detail respectively and changes the respective, "corrected" variable
                        if incorrect_detail.strip().lower().replace(" ", "") == "username":
                            corrected_username = input("Please enter your new username: ")

                        elif incorrect_detail.strip().lower().replace(" ", "") == "password":
                            corrected_password = getpass("Please enter your new password: ")

                        elif incorrect_detail.strip().lower().replace(" ", "") == "emailaddress":
                            while 1:  # Quicker than using the, "True" keyword
                                # Loops until the user gives a valid email address

                                corrected_email_address = input("Please enter your new email address: ")

                                if validate_email(corrected_email_address):
                                    break

                                else:
                                    print("\n\nThat email address is not valid please enter a new one.\n\n")

        else:
            print("\nSorry that username is already taken. Please try a different one.\n\n")
            self.create_player_account(conn_users, cur_users)
            return
