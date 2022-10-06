from art import logo
from replit import clear
import random


def blackjack():
    userChoice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if userChoice == "y":
        # playAgain = True

        # while playAgain:
        clear()
        print(logo)

        def deal_card(cards):
            return random.choice(cards)

        def calc_score(cards):
            total = sum(cards)
            if len(cards) == 2 and total == 21:
                return 0
            if 11 in cards and total > 21:
                cards.remove(11)
                cards.append(1)
                return (total)

            return total

        def compare(playerTotal, dealerTotal):
            print(f"\tYour final hand {playerCards}, final score: {playerTotal}")
            print(f"\tComputer's final hand: {dealerCards}, final score: {dealerTotal}")
            if playerTotal == dealerTotal:
                return "It's a draw!"
            if dealerTotal == 0:
                return "You lose"
            if playerTotal == 0:
                return "You win!"
            if playerTotal > 21:
                return "You lose!"
            if dealerTotal > 21:
                return "You win!"
            if playerTotal > dealerTotal:
                return "You win!"
            else:
                return "You lose!"

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        playerCards = []
        dealerCards = []

        playerTotal = 0
        dealerTotal = 0

        for card in range(2):
            playerCards.append(deal_card(cards))

        playerTotal = calc_score(playerCards)

        for card in range(2):
            dealerCards.append(deal_card(cards))

        dealerTotal = calc_score(dealerCards)

        print(f"\tYour cards: {playerCards}, current score: {playerTotal}")
        print(f"\tComputer's first card: {dealerCards[0]}")

        if playerTotal == 0:
            print("Player wins!")
        elif dealerTotal == 0:
            print("Dealer wins!")
        else:
            hitPass = input("Type 'y' to get another card, type 'n' to pass: ")

        while hitPass == "y" and playerTotal <= 21:
            playerCards.append(deal_card(cards))
            playerTotal = calc_score(playerCards)
            print(f"\tYour cards: {playerCards}, current score: {playerTotal}")
            print(f"\tComputer's first card: {dealerCards[0]}")

        while dealerTotal < 17:
            dealerCards.append(deal_card(cards))
            dealerTotal = calc_score(dealerCards)

        print(compare(playerTotal, dealerTotal))

    blackjack()


blackjack()
