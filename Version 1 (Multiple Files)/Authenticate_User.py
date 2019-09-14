import sqlite3
from Database_Manager import check_if_username_exists, username_exists, check_if_password_exists, password_exists
from Database_Manager import create_account


# ======================================================================================================================
# ======================================================================================================================

def starting_menu():
    option_to_sign_in_or_create_account = input("Sign in\nor\nCreate an account\n\n")
    print("\n\n")

    if option_to_sign_in_or_create_account.lower().strip().replace(" ", "") == "signin":
        print("Sign In Page\n\n")

        entered_username = input("Enter your Username: ")
        check_if_username_exists(entered_username)

        if username_exists:
            entered_password = input("Enter your Password: ")
            print("\n\n")
            check_if_password_exists(entered_password)

            if password_exists:
                print("Successfully Logged In!\n\n")
                # Login here

            elif password_exists is False:
                print("\n\nSorry that is invalid. Please check your spelling!\n\n")
                starting_menu()
                return

        elif username_exists is False:
            print("\n\nSorry that is invalid. Please check your spelling!\n\n")
            starting_menu()
            return

    elif option_to_sign_in_or_create_account.lower().strip().replace(" ", "") == "createanaccount":
        print("Create An Account Page\n\n")

        username = input("Username: ")
        password = input("Password: ")
        re_entered_password = input("Re-Enter your Password: ")
        print("\n\n")

        if password == re_entered_password:
            create_account(username, password)
            print("Account Successfully created!\n\n")
            starting_menu()

        else:
            print("Sorry Passwords do not match. Please check your spelling!\n\n")
            starting_menu()
            return


# ======================================================================================================================
# ======================================================================================================================

starting_menu()
