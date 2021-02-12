# D3 Exercise 1
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# D3 Exercise 2
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(height/weight**2)

# if bmi <= 18.5:
#     print("underweight")
# elif bmi <= 25:
#     print("normal weight")
# elif bmi <= 30: 
#     print("overweight") 
# elif bmi <= 35:
#     print("obese") 
# else:
#     print("clinically obese") 

# D3 Exercise 3
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else: 
#     print('Not Leap Year')

# D3 Exercise 4
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# total = 0
# if size == "S":
#     total += 15
#     if add_pepperoni == "Y":
#         total += 2
#         if extra_cheese == "Y":
#             total +=1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")
#     else:
#         if extra_cheese == "Y":
#             total +=1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")
# elif size == "M":
#     total += 20
#     if add_pepperoni == "Y":
#         total += 3
#         if extra_cheese == "Y":
#             total +=1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")
#     else:
#         if extra_cheese == "Y":
#             total +=1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")
# else:
#     total += 25
#     if add_pepperoni == "Y":
#         total += 3
#         if extra_cheese == "Y":
#             total += 1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")
#     else:
#         if extra_cheese == "Y":
#             total += 1
#             print(f"Your Final bill is: ${total}")
#         else: 
#             print(f"Your Final bill is: ${total}")

# D3 Exercise 5