from Database_Manager import Login_System_Database_Manager


class Authenticate_User(Login_System_Database_Manager):
    """
    This class manages how the user is logged in.
    """

    # ==================================================================================================================
    # ==================================================================================================================

    def starting_page(self, player_logging_in):
        """
        Is the first page that opens when the program is run. Returns a string, "login" or "createanaccount" depending
        on what they typed in.
        :param player_logging_in: STRING
        :return: STRING or BOOLEAN
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

    # ==================================================================================================================
    # ==================================================================================================================

    def login_in_players(self, player_logging_in):
        """
        Logs Player 1 and 2 into the game by checking if their typed username and password exists from an SQL Database.
        :param player_logging_in: STRING
        :return: BOOLEAN
        """

        print("Login Page\n")
        print("Player " + player_logging_in + ":\n\n")  # Prints title to show user which user is logging in
        entered_username = input("Enter your Username: ")

        if Login_System_Database_Manager.check_if_username_exists(self, entered_username)[0]:
            username_tuple = Login_System_Database_Manager.check_if_username_exists(self, entered_username)[1]
            # The second value that is returned is either NONE or "tuple_line" variable

            entered_password = input("Enter your Password: ")

            if Login_System_Database_Manager.check_if_password_exists(self, entered_password, username_tuple):
                return True

            else:
                print("\n\nSorry that Password is incorrect. Please check your spelling.\n\n")
                return False

        else:
            print("\n\nSorry that Username does not exist. Please check your spelling.\n\n")
            return False

    # ==================================================================================================================
    # ==================================================================================================================

    def create_player_account(self):
        """
        Creates the user an account by asking them for a: username, password and email address(optional)
        """

        print("Create Account Page\n")
        new_username = input("Please enter a Username: ")

        if Login_System_Database_Manager().check_if_username_exists(new_username)[0] is not True:
            # If username is not taken

            new_password = input("Please enter your Password: ")
            new_password_check = input("Please Re-enter your Password: ")

            if new_password == new_password_check:
                new_email_address = input("Please enter your Email Address (optional, type 'no' if you do not want "
                                          "to do so): ")

        else:
            print("\nSorry that username is already taken. Please try a different one.\n\n")
            self.create_player_account()
            return

Authenticate_User().create_player_account()
