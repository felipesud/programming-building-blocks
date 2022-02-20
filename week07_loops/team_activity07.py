# Week 3 Team Activity
# Reference: https://byui-cse.github.io/cse110-course/lesson07/teach.html
import random

magic_number = random.randint(1, 100)
guess_number = ""
stop_playing = False
guesses = 0

while stop_playing == False:
    
    guess_number = int(input("What is your guess? ") or 0)
    guesses = guesses + 1

    if guess_number < magic_number:
        print("Higher")
    elif guess_number > magic_number:
        print("Lower")
    else:
        print(f"You guessed it! You tried {guesses} times.")
        
        guesses = 0
        
        still = input("Still playing? (yes/no) ").lower()
        
        if still == "no":
            stop_playing = True