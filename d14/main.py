from game_data import data
from art import  logo, vs
import random

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account

            print(f"Compare A: {format_data(account_a)}.") 
            print(vs)
            print(f"Compare B: {format_data(account_b)}.") 

            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_follwer_count = account_a["follower_count"]
            b_follwer_count = account_b["follower_count"]

            is_correct = check_answer(guess, a_follwer_count, b_follwer_count)
            print(chr(27) + "[2J")
            print(logo)
            if is_correct:
                score+=1
                print(f"You're right! Current Score: {score}.")
            else:
                game_should_continue = False
                print(f"Sorry, You lose. Final Score: {score}")
game()


