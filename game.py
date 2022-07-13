# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot! Welcome Player One to my Rock-Paper-Scissors game...Please choose either 'rock', 'paper', or 'scissors':")


import random

user = input("Enter a choice (rock, paper, scissors): ")
possible_choices = ["rock", "paper", "scissors"]
computer = random.choice(possible_choices)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock crushes scissors. You win! Thanks for playing. Please play again!")
    else:
        print("Paper covers rock. You lose. It's ok. Please play again!")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock. You win! Thanks for playing. Please play again!")
    else:
        print("Scissors cuts paper. You lose. It's ok. Please play again!")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper. You win! Thanks for playing. Please play again!")
    else:
        print("Rock crushes scissors. You lose. It's ok. Please play again!")
