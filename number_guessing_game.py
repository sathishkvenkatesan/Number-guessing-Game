#Number Guessing Game
#created by Sathish Kumar

import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome To The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Guess a number between 1-100: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    
    elif guess > secret_number:
        print("Too High!")
        
    else:
        print("Too Low!")