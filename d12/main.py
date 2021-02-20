#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

# global vars
EASY = 10
HARD = 5

# functions
def check_ans(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! the asnwer was ${answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or hard: ")
    if level == "easy":
        return EASY
    else:
        return HARD
# game
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0 

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_ans(guess, answer, turns)
        if turns == 0:
            print("You lose 🥺")
            return

game()
