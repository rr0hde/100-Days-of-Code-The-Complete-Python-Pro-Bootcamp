import random
from art import logo

def compare(NUMBER_TO_GUESS, player_guess):
    if player_guess == NUMBER_TO_GUESS:
        return f"You got it! The answer was {NUMBER_TO_GUESS}"
    elif player_guess > NUMBER_TO_GUESS:
        return "Too high!"
    elif player_guess < NUMBER_TO_GUESS:
        return "Too low!"


NUMBER_TO_GUESS = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    tries = 5
elif difficulty == "easy":
    tries = 10

player_guess = None

while tries > 0 and player_guess != NUMBER_TO_GUESS:
    print(f"You have {tries} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    print(compare(NUMBER_TO_GUESS, player_guess))
    tries -= 1

if tries == 0:
    print("You've run out of guesses, you lose.")