from Authenticate_User import Authenticate_User
import sqlite3

# ======================================================================================================================
# ======================================================================================================================
# Initialisation

conn_users = sqlite3.connect("users.db")
cur_users = conn_users.cursor()

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
# Termination

cur_users.close()
conn_users.close()
