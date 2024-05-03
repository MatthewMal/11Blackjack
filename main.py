import random
import os


def draw_card(how_many, deck):
    for i in range(0, how_many):
        deck.append(random.choice(cards))
    if sum(deck) > 21:
        for i in range(0, len(deck)):
            if deck[i] == 11:
                deck[i] = 1


play_again = True
defeats = 0
wins = 0
draws = 0

while play_again:
    print("Welcome to a game of Blackjack!\n\n")
    print(f"Your current score is {wins} wins, {draws} draws and {defeats} defeats\n")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    dealer = []
    decision = "y"
    you_lost = False

    draw_card(2, player)
    draw_card(1, dealer)

    if sum(player) == 21:
        print(f"Your cards are {player}, you have a blackjack!")
    else:
        print(f"Dealer's first card is {dealer}")
        while decision == "y":
            print(f"Your cards are {player}")
            decision = input("Do you want to draw another card? type 'y' or 'n' ").lower()

            if decision == "y":
                draw_card(1, player)

            if sum(player) > 21:
                print(f"Your cards are {player}, you went over 21, you lost")
                you_lost = True
                decision = "n"
                defeats = defeats + 1
    if not you_lost:
        while sum(dealer) < 17:
            draw_card(1, dealer)
        print(f"Dealers cards are {dealer}")
        if sum(dealer) > 21:
            print("Dealer went over 21. You won!")
            wins = wins + 1
        elif sum(player) > sum(dealer):
            print("You won")
            wins = wins + 1
        elif sum(player) == sum(dealer):
            print("It's a draw")
            draws = draws + 1
        else:
            print("You lost")
            defeats = defeats + 1
    repeat = input("Do you wish to play again? Type 'y' or 'n' ").lower()
    if repeat != 'y':
        os.system('cls')
        repeat2 = input("Are you SURE you want to quit? Type 'q' to quit ").lower()
        if repeat2 == "q":
            play_again = False
        else:
            os.system('cls')
    else:
        os.system('cls')
