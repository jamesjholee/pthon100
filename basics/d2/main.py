# D2 Exercise 1
# two_digit_number = input('Type a two digit number:')
# num1 = two_digit_number[0]
# num2 = two_digit_number[1]
# print(int(num1) + int(num2))

# D2 Exercise 2
# height = input('enter your height in m: ')
# weight = input('enter your weight in kg: ')

# bmi = int(weight) / float(height) ** 2

# print(int(bmi))

# D2 Exercise 3
# age = input("What is our current age? ")

# remaining_years = 90 - int(age)
# remaining_days = remaining_years * 365
# remaining_weeks = remaining_years * 52
# remaining_months = remaining_years * 12
# msg = f'You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left...'
# print(msg)

# D2 Final Project Tip calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? "))
num_of_ppl = int(input("How many people to split the bill? "))

bill_with_tip = tip_percent / 100 * bill + bill
final_ammount = round(bill_with_tip / num_of_ppl,2)
formated_ammount = "{:.2f}".format(final_ammount)

print(f"Each person should pay: ${formated_ammount}")
