rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

gameImages = [rock, paper, scissors]
playChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
compChoice = random.randint(0, 2)

if playChoice > 2 or playChoice < 0:
    print('You typed an invalid number, you lose!')
else:
    print(gameImages[playChoice])
    print('Computer chose: ')
    print(gameImages[compChoice])

    if playChoice == 0 and compChoice == 2:
        print('You win!')
    elif playChoice == 1 and compChoice == 0:
        print('You win!')
    elif playChoice == 2 and compChoice == 1:
        print('You win!')
    elif playChoice == compChoice:
        print('Draw')
    else:
        print('You lose!')
