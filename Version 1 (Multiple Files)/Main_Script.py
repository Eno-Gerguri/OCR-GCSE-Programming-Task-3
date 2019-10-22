from Authenticate_User import Authenticate_User

# ======================================================================================================================
# ======================================================================================================================
# Initialisation

Authenticate_User = Authenticate_User()


# ======================================================================================================================
# ======================================================================================================================
# Main Loop

logged_in_player_1 = False
logged_in_player_2 = False
player_logging_in = "1"

while logged_in_player_1 is False:

    if Authenticate_User.starting_page(player_logging_in) == "login":

        if Authenticate_User.login_in_players(player_logging_in):  # If player 1 logs in successfully
            player_logging_in = "2"
            logged_in_player_1 = True  # Breaks out of loop

        # Otherwise, the while loop will begin again

    elif Authenticate_User.starting_page(player_logging_in) == "createanaccount":
        pass


# ======================================================================================================================
# ======================================================================================================================
