# D10 Exercise 1
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#         else:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     idx = month - 1
#     if if_leap(year) and month == 2:
#         return 29
#     else:
#         return month_days[idx]
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# D10 Project Calculator
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second  number?: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
calc_function = operations[operation_symbol]
answer = calc_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")