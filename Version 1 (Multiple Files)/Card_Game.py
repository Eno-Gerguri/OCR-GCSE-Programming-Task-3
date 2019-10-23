# ======================================================================================================================
# ======================================================================================================================
# Initialise Deck and all the cards within it
import sqlite3
import Database_Manager

class Card:
    """
    This class Initialises the card
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


conn_users = sqlite3.connect("users.db")
cur_users = conn_users.cursor()

Database_Manager.Login_System_Database_Manager().enter_account_details("Eno", "Gerguri", "testemail")
