import random
import art
from os import system


def draw_card(hand):
    hand.append(random.choice(cards))


still_play = True
while still_play == True:
    if input("Do you wanna play game of blackjack, 'y' for yes, 'n' for no: ") == "y":
        system("cls")
        print(art.logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        dealer_hand = []

        player_hand = []

        for i in range(0, 2):
            draw_card(dealer_hand)
            draw_card(player_hand)

        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer first cards: {dealer_hand[0]}")
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_card == "y":
            draw_card(player_hand)
            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")

        if sum(dealer_hand) < 17:
            draw_card(dealer_hand)
            print(f"Computer cards: {dealer_hand} current score: {sum(dealer_hand)}")
        else:
            print(f"Computer cards: {dealer_hand} current score: {sum(dealer_hand)}")

        if sum(player_hand) > 21:
            print("Player lost")
        elif sum(dealer_hand) > 21:
            print("Player won")
        elif sum(player_hand) == sum(dealer_hand):
            print("Draw")
        elif sum(player_hand) > sum(dealer_hand):
            print("Player won")
        elif sum(player_hand) < sum(dealer_hand):
            print("Player lost")
    else:
        print("Ok see you later")
        still_play = False
