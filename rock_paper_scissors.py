import random
computer_guess = random.randint(1,3)
print("Welcome to the Rock, Paper, Scissors Game!")
player_choice = str(input("Enter your choice (Rock, Paper or Scissors. Please enter your choice in uppercase.)")).upper()
if player_choice == "ROCK":
    if computer_guess == 1:
        print("Draw! The computer chose Rock!")
    if computer_guess == 2:
            print("You Lose! The computer chose Paper!")
    if computer_guess == 3:
            print("You Win! The computer chose Scissors!")
if player_choice == "PAPER":
    if computer_guess == 1:
        print("You Win! The computer chose Rock!")
    if computer_guess == 2:
            print("Draw! The computer chose Paper!")
    if computer_guess == 3:
            print("You Lose! The computer chose Scissors!")
if player_choice == "SCISSORS":
    if computer_guess == 1:
        print("You Lose! The computer chose Rock!")
    if computer_guess == 2:
            print("You Win! The computer chose Paper!")
    if computer_guess == 3:
            print("Draw! The computer chose Scissors!")


