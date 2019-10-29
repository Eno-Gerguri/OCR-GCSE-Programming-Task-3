from Authenticate_User import Authenticate_User
import sqlite3

# ======================================================================================================================
# ======================================================================================================================
# Initialisation


conn_users = sqlite3.connect("users.db")
cur_users = conn_users.cursor()

Authenticate_User = Authenticate_User(conn_users, cur_users)

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# Main Loop

# ======================================================================================================================
# ======================================================================================================================
# Logs in both players

logged_in_player_1 = False
logged_in_player_2 = False
player_logging_in = "1"

while logged_in_player_1 is False:

    if Authenticate_User.starting_page(player_logging_in) == "login":

        if Authenticate_User.login_in_players(conn_users, cur_users, player_logging_in):
            # If player 1 logs in successfully
            player_logging_in = "2"  # Sets the new player logging in
            logged_in_player_1 = True  # Breaks out of loop

        # Otherwise, the while loop will begin again

    else:  # If it returns "createanaccount"
        Authenticate_User.create_player_account(conn_users, cur_users)

        # Loop will begin again to allow the user to create another account or to login with one

while logged_in_player_2 is False:

    if Authenticate_User.starting_page(player_logging_in) == "login":

        if Authenticate_User.login_in_players(conn_users, cur_users, player_logging_in):
            # If player 2 logs in successfully
            logged_in_player_2 = True  # Breaks out of loop

        # Otherwise, the while loop will begin again

    else:  # If it returns "createanaccount"
        Authenticate_User.create_player_account(conn_users, cur_users)

        # Loop will begin again to allow the user to create another account or to login with one

# ======================================================================================================================
# ======================================================================================================================
# Does whatever happens after player is logged in

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# Termination

cur_users.close()
conn_users.close()
