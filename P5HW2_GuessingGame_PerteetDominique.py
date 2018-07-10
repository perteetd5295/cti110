## CTI-110 
## P5HW2 - Random Number Guessing Game   
## Dominique Perteet
## 7/9/2018

# Guess what the Number is!!!

import random

guesses = 6
number = random.randint(1,100)
win = False

while guesses > 0:
    guess = int(input("Guess: "))

    guesses -= 1

    if guess > number:
        print(" Your guessed too high, you have", guesses, "left")
    elif guess < number:
        print("Your guessed too low , you have", guesses, "left")
    else:
        print("Congrats, you guessed the right!!!, and won the game!")
        win = True
        guesses = 0

if win == False:
    print("Sorry, you guessed wrong D: The number was,", number)
