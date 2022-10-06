from art import logo, vs
from game_data import data
from random import choice
from replit import clear


def get_comparisons():
    return choice(data)


def follower_count():
    if a_follower > b_follower:
        return 'A'
    elif b_follower > a_follower:
        return 'B'


def restart():
    clear()
    print(logo)


score = 0

correct = True

restart()

while correct:
    a = get_comparisons()
    b = get_comparisons()

    a_follower = a['follower_count']
    b_follower = b['follower_count']

    print(f"Compare A: {a['name']}, a {b['description']}, from {a['country']}.")

    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

    print(follower_count())

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if guess == follower_count():
        restart()
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
        b = get_comparisons()
    else:
        restart()
        print(f"Sorry, that's wrong. Final score: {score}")
        correct = False
