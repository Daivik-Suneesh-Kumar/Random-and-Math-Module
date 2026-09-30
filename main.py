import random
playing = True
number = random.randint(0,9)

while playing:
    guess = int(input("Give your best guess! You will guess a number from 0 to 9.\n"))
    if number == guess:
        print("You won the game.")
        print("The number was:",number)
        break
    else:
        print("That was not my number. Guess again!")