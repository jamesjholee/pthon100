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
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else: 
    print('Not Leap Year')