############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# # the range function doenst reach 20 it goes to 19 change 20 to 21

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# # the index of 6 does exist so cahgne range the function from 0 to 5

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# # the number 1994 is not greater or less than any of the statemnts addd a equal statment to correct teh issue


# # Fix the Errors
# age = inf(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# # f string and indent error as well as change the age to an int

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # the word per page variable had double equals

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# # indent error for the code


number = int(input("Which number do you want to check?"))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
year = input("Which year do you want to check?")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        elif:
            print("Not leap year.")
        print("Leap year.")
    else:
        print("Not leap year.")
  

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])