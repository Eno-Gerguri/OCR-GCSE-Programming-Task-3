from random import shuffle

game_has_finished = False

drawn_card_player_1 = None
drawn_card_player_2 = None

player_points_1 = 0
player_points_2 = 0

players_turn = 1

player_1_won_cards = []
player_2_won_cards = []

player_who_won = None


class card:

    def __init__(self, card_number, card_colour):
        self.card_number = card_number
        self.card_colour = card_colour


red_card_1 = card(1, "red")
red_card_2 = card(2, "red")
red_card_3 = card(3, "red")
red_card_4 = card(4, "red")
red_card_5 = card(5, "red")
red_card_6 = card(6, "red")
red_card_7 = card(7, "red")
red_card_8 = card(8, "red")
red_card_9 = card(9, "red")
red_card_10 = card(10, "red")
black_card_1 = card(1, "black")
black_card_2 = card(2, "black")
black_card_3 = card(3, "black")
black_card_4 = card(4, "black")
black_card_5 = card(5, "black")
black_card_6 = card(6, "black")
black_card_7 = card(7, "black")
black_card_8 = card(8, "black")
black_card_9 = card(9, "black")
black_card_10 = card(10, "black")
yellow_card_1 = card(1, "yellow")
yellow_card_2 = card(2, "yellow")
yellow_card_3 = card(3, "yellow")
yellow_card_4 = card(4, "yellow")
yellow_card_5 = card(5, "yellow")
yellow_card_6 = card(6, "yellow")
yellow_card_7 = card(7, "yellow")
yellow_card_8 = card(8, "yellow")
yellow_card_9 = card(9, "yellow")
yellow_card_10 = card(10, "yellow")

deck = [red_card_1, red_card_2, red_card_3, red_card_4, red_card_5,
        red_card_6, red_card_7, red_card_8, red_card_9, red_card_10,

        black_card_1, black_card_2, black_card_3, black_card_4, black_card_5,
        black_card_6, black_card_7, black_card_8, black_card_9, black_card_10,

        yellow_card_1, yellow_card_2, yellow_card_3, yellow_card_4, yellow_card_5,
        yellow_card_6, yellow_card_7, yellow_card_8, yellow_card_9, yellow_card_10]


# ======================================================================================================================
# ======================================================================================================================

def draw_card():
    global drawn_card_player_1, drawn_card_player_2

    if players_turn == 1:
        print("It is Player 1's turn!\n")
        input()
        drawn_card_player_1 = deck[0]
        deck.remove(drawn_card_player_1)
        print("Player 1 drew, '" + drawn_card_player_1.card_colour + " " + str(drawn_card_player_1.card_number) + "'")

    elif players_turn == 2:
        print("It is Player 2's turn!\n")
        input()
        drawn_card_player_2 = deck[0]
        deck.remove(drawn_card_player_2)
        print("Player 2 drew, '" + drawn_card_player_2.card_colour + " " + str(drawn_card_player_2.card_number) + "'\n")

    if drawn_card_player_1 is not None and drawn_card_player_2 is not None:
        print("\n'" + drawn_card_player_1.card_colour + " " + str(drawn_card_player_1.card_number) + "'"
              + " vs " +
              "'" + drawn_card_player_2.card_colour + " " + str(drawn_card_player_2.card_number) + "'")

    print("\n")


# ======================================================================================================================
# ======================================================================================================================

def change_turn():
    global players_turn

    if players_turn == 1:
        players_turn = 2

    elif players_turn == 2:
        players_turn = 1


# ======================================================================================================================
# ======================================================================================================================

def compare_cards():
    global player_points_1, player_points_2

    if drawn_card_player_1.card_colour == drawn_card_player_2.card_colour:
        if drawn_card_player_1.card_number > drawn_card_player_2.card_number:
            print("Player 1 won that battle by higher number!")

            player_points_1 += 2

            player_1_won_cards.append(drawn_card_player_1)
            player_1_won_cards.append(drawn_card_player_2)

        elif drawn_card_player_1.card_number < drawn_card_player_2.card_number:
            print("Player 2 won that battle by higher number!")

            player_points_2 += 2

            player_2_won_cards.append(drawn_card_player_1)
            player_2_won_cards.append(drawn_card_player_2)

    elif drawn_card_player_1.card_colour != drawn_card_player_2.card_colour:
        if drawn_card_player_1.card_colour == "red" and drawn_card_player_2.card_colour == "black":
            print("Player 1 won that battle by colour!\nRed beats Black!")

            player_points_1 += 2

            player_1_won_cards.append(drawn_card_player_1)
            player_1_won_cards.append(drawn_card_player_2)

        elif drawn_card_player_1.card_colour == "yellow" and drawn_card_player_2.card_colour == "red":
            print("Player 1 won that battle by colour!\nYellow beats Red!")

            player_points_1 += 2

            player_1_won_cards.append(drawn_card_player_1)
            player_1_won_cards.append(drawn_card_player_2)

        elif drawn_card_player_1.card_colour == "black" and drawn_card_player_2.card_colour == "yellow":
            print("Player 1 won that battle by colour!\nBlack beats Yellow!")

            player_points_1 += 2

            player_1_won_cards.append(drawn_card_player_1)
            player_1_won_cards.append(drawn_card_player_2)

        if drawn_card_player_2.card_colour == "red" and drawn_card_player_1.card_colour == "black":
            print("Player 2 won that battle by colour!\nRed beats Black!")

            player_points_2 += 2

            player_2_won_cards.append(drawn_card_player_1)
            player_2_won_cards.append(drawn_card_player_2)

        elif drawn_card_player_2.card_colour == "yellow" and drawn_card_player_1.card_colour == "red":
            print("Player 2 won that battle by colour!\nYellow beats Red!")

            player_points_2 += 2

            player_2_won_cards.append(drawn_card_player_1)
            player_2_won_cards.append(drawn_card_player_2)

        elif drawn_card_player_2.card_colour == "black" and drawn_card_player_1.card_colour == "yellow":
            print("Player 2 won that battle by colour!\nBlack beats Yellow!")

            player_points_2 += 2

            player_2_won_cards.append(drawn_card_player_1)
            player_2_won_cards.append(drawn_card_player_2)

    print("\n")


# ======================================================================================================================
# ======================================================================================================================

def play_card_game():
    global game_has_finished, player_who_won

    while game_has_finished is False:
        for i in range(2):
            draw_card()

            change_turn()

        compare_cards()

        if not deck:
            game_has_finished = True

    if player_points_1 > player_points_2:
        player_who_won = 1

    elif player_points_1 < player_points_2:
        player_who_won = 2

    if player_who_won == 1:
        print("Player 1 won with " + str(len(player_1_won_cards)) + " cards!\n")
        for i, line in enumerate(player_1_won_cards):
            print(line.card_colour + " " + str(line.card_number) + "\n")

    elif player_who_won == 2:
        print("Player 2 won with " + str(len(player_2_won_cards)) + " cards!\n")
        for i, line in enumerate(player_2_won_cards):
            print(line.card_colour + " " + str(line.card_number) + "\n")


# ======================================================================================================================
# ======================================================================================================================

shuffle(deck)

play_card_game()
