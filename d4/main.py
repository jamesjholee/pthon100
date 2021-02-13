import random

# D4 Exercise 1
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
# heads = 1 

# random_num = random.randint(1,2)

# if (random_num == heads) :
#     print('Heads')
# else:
#     print('Tails')

# D4 Exercise 2
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# total_num = len(names) - 1
# random_num = random.randint(0, total_num)
# selected_name = names[random_num]
# print(selected_name)

# D4 Exercise 3
# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# y = int(position[0]) - 1
# x = int(position[1]) - 1

# map[x][y] = 'X'




# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# D4 Project Janken
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
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
picks = [rock, paper, scissors]
if player_choice > 2:
    print('Stop cheating!! You lose for trying to cheat!')
else:   
    print(picks[player_choice])

computer_random_int = random.randint(0, 2)
print(picks[computer_random_int])

if picks[player_choice] == picks[computer_random_int]:
    print("Its a Draw!!!")
elif picks[player_choice] == rock:
    if picks[computer_random_int] == paper:
        print("You Lose D:")
    else:
        print("YOU WONNNNNNNN~")
elif picks[player_choice] == paper:
    if picks[computer_random_int] == scissors:
        print("You Lose D:")
    else:
        print("YOU WONNNNNNNN~")
else:
    if picks[computer_random_int] == rock:
        print("You Lose D:")
    else:
        print("YOU WONNNNNNNN~")
