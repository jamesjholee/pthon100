# D5 Exercise 1
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# #Write your code below this row 👇
# total_height = 0
# for height in student_heights:
#     total_height += height
# count = 0
# for student in student_heights:
#     count += 1
# average_height = round(total_height / count)
# print(average_height)

# D5 Exercise 2
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
# #Write your code below this row 👇
# hightest_score = 0
# for score in student_scores:
#     if score > hightest_score:
#         hightest_score = score
# print(hightest_score)

# D5 Exercise 3
# #Write your code below this row 👇
# sum = 0 
# for num in range(1, 101):
#     if num % 2 == 0:
#         sum += num
# print(sum)

# # this one takes another param in range function that defines the what the next number gets added to the current number
# # sum = 0 
# # for num in range(2, 101, 2):
# #     sum += num
# # print(sum)

# D5 Exercise 4
# #Write your code below this row 👇
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# D5 Project
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ''
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
password = ''
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)
