def starting_menu():
    option_to_sign_in_or_create_account = input("Sing in\nor\nCreate an account\n\n")

from Database_Manager import init, check_if_user_exists, close

init()
check_if_user_exists(None)
close()